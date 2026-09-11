#!/usr/bin/env python3
"""Convert a competition results.json and its metadata into plotting CSVs.

Without --results, fetch the latest competition run from the suite's main branch.
GitHub Actions runs this before Observable builds; no data is fetched by the plot.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import posixpath
import re
from pathlib import Path
from urllib.request import Request, urlopen

REPOSITORY = "SparseArrayProgrammingSuite/SparseArrayProgrammingSuite"
RUN_RESULTS = re.compile(r"competition/run_(\d+)/results\.json")
RESULT_COLUMNS = ["framework", "benchmark", "generator", "dataset", "metric", "value"]
DATASET_COLUMNS = ["benchmark", "generator", "dataset"]


def latest_results_path(tree: dict) -> str:
    if tree.get("truncated"):
        raise ValueError("GitHub returned a truncated file tree; cannot determine the latest run")
    candidates = [
        (int(match[1]), entry["path"])
        for entry in tree["tree"]
        if entry["type"] == "blob" and (match := RUN_RESULTS.fullmatch(entry["path"]))
    ]
    if not candidates:
        raise ValueError("No competition/run_*/results.json found on main")
    return max(candidates)[1]


def read_url(url: str) -> dict:
    request = Request(url, headers={"User-Agent": "SAPS-leaderboard-build"})
    with urlopen(request, timeout=120) as response:
        return json.load(response)


def record_tags(record: dict) -> set[str]:
    return {tag for field in ("tags", "suites", "statistics", "topics") for tag in record.get(field) or []}


def dataset_tags(metadata: dict) -> dict[tuple[str, str, str], set[str]]:
    tags = {}
    for benchmark in metadata["benchmarks"]:
        for generator in benchmark.get("generators", []):
            for dataset in generator.get("datasets", []):
                key = (benchmark["name"], generator["name"], dataset["name"])
                tags[key] = record_tags(benchmark) | record_tags(generator) | record_tags(dataset)
    return tags


def build_tables(results: dict, metadata: dict) -> tuple[list[dict], list[dict], list[str]]:
    """Preserve successful measurements and describe every problem in the run.

    The shared join key is (benchmark, generator, dataset). Failed measurements
    and missing/nonfinite values are omitted from results, but not descriptions.
    Numeric values retain their original units, including zero and negative values.
    """
    tags = dataset_tags(metadata)
    names = {key: framework["name"] for key, framework in results["frameworks"].items()}
    if len(set(names.values())) != len(names):
        raise ValueError("Framework names must be unique within a competition run")
    result_rows = []
    descriptions = {}
    for benchmark in results["benchmarks"]:
        for generator in benchmark.get("generators", []):
            for dataset in generator.get("datasets", []):
                key = (benchmark["name"], generator["name"], dataset["name"])
                if key not in tags:
                    raise ValueError(f"Missing tag metadata for {key!r}")
                descriptions.setdefault(key, set()).update(
                    tags[key] | record_tags(benchmark) | record_tags(generator) | record_tags(dataset)
                )
                for measurement in dataset.get("results", []):
                    value = measurement.get("result")
                    if measurement["status"] != "ok" or type(value) not in (int, float) or not math.isfinite(value):
                        continue
                    result_rows.append({
                        "framework": names[measurement["framework"]],
                        **dict(zip(DATASET_COLUMNS, key)),
                        "metric": measurement["metric"],
                        "value": value,
                    })
    if not descriptions:
        raise ValueError("The competition run contains no datasets")
    tag_names = sorted({tag for problem_tags in descriptions.values() for tag in problem_tags})
    if set(tag_names) & set(DATASET_COLUMNS):
        raise ValueError("Tag names must not collide with benchmark, generator, or dataset columns")
    benchmark_rows = [
        dict(zip(DATASET_COLUMNS, key)) | {tag: tag in problem_tags for tag in tag_names}
        for key, problem_tags in sorted(descriptions.items())
    ]
    result_rows.sort(key=lambda row: tuple(row[column] for column in [*DATASET_COLUMNS, "framework", "metric"]))
    return result_rows, benchmark_rows, tag_names


def write_csv(path: Path, columns: list[str], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: str(value).lower() if isinstance(value, bool) else value for key, value in row.items()})


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, help="Use a local results.json instead of fetching main")
    parser.add_argument("--metadata", type=Path, help="Local metadata (defaults to the path referenced by --results)")
    parser.add_argument("--output-dir", type=Path, default=Path("docs/data"))
    parser.add_argument("--metadata-output", type=Path, help="Also save the fetched metadata for Jekyll")
    args = parser.parse_args()
    if args.metadata and not args.results:
        parser.error("--metadata requires --results")

    if args.results:
        results = json.loads(args.results.read_text(encoding="utf-8"))
        metadata_path = args.metadata or args.results.parent / results["metadata"]
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        source = {"resultsUrl": f"https://github.com/{REPOSITORY}/tree/main/competition/{results['run']}"}
    else:
        tree = read_url(f"https://api.github.com/repos/{REPOSITORY}/git/trees/main?recursive=1")
        path = latest_results_path(tree)
        commit = tree["sha"]
        raw = f"https://raw.githubusercontent.com/{REPOSITORY}/{commit}"
        results = read_url(f"{raw}/{path}")
        metadata_path = posixpath.normpath(posixpath.join(posixpath.dirname(path), results["metadata"]))
        metadata = read_url(f"{raw}/{metadata_path}")
        source = {"commit": commit, "resultsUrl": f"https://github.com/{REPOSITORY}/blob/{commit}/{path}"}

    result_rows, benchmark_rows, tags = build_tables(results, metadata)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(args.output_dir / "results.csv", RESULT_COLUMNS, result_rows)
    write_csv(args.output_dir / "benchmarks.csv", DATASET_COLUMNS + tags, benchmark_rows)
    # Small provenance record for the plot's source link; all plotting data is CSV.
    run = {"run": results["run"], "frameworks": sorted(f["name"] for f in results["frameworks"].values()), **source}
    (args.output_dir / "run.json").write_text(json.dumps(run, indent=2) + "\n", encoding="utf-8")
    if args.metadata_output:
        args.metadata_output.parent.mkdir(parents=True, exist_ok=True)
        args.metadata_output.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(result_rows)} measurements and {len(benchmark_rows)} problems with {len(tags)} tags to {args.output_dir}")


if __name__ == "__main__":
    main()
