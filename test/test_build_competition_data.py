import copy
import csv
import tempfile
import unittest
from pathlib import Path

from scripts.build_competition_data import DATASET_COLUMNS, RESULT_COLUMNS, build_tables, latest_results_path, write_csv


def measurement(framework, value, status="ok", metric="time"):
    return {"framework": framework, "result": value, "status": status, "metric": metric}


class TablesTest(unittest.TestCase):
    def setUp(self):
        self.results = {
            "run": "run_10",
            "frameworks": {"a": {"name": "Alpha"}, "b": {"name": "Beta"}},
            "benchmarks": [{"name": "A", "generators": [{"name": "g", "datasets": [
                {"name": "first", "results": [measurement("a", 4), measurement("b", 2)]},
                {"name": "failed", "results": [measurement("a", None, "failed")]},
            ]}]}],
        }
        self.metadata = copy.deepcopy(self.results)
        benchmark = self.metadata["benchmarks"][0]
        benchmark["tags"] = ["benchmark-tag"]
        benchmark["generators"][0]["topics"] = ["generator-tag"]
        benchmark["generators"][0]["datasets"][0]["tags"] = ["dense", "benchmark-tag"]

    def test_measurements_and_inherited_boolean_tag_columns(self):
        rows, benchmarks, tags = build_tables(self.results, self.metadata)
        self.assertEqual(len(rows), 2)
        self.assertEqual(tags, ["benchmark-tag", "dense", "generator-tag"])
        first = next(row for row in benchmarks if row["dataset"] == "first")
        failed = next(row for row in benchmarks if row["dataset"] == "failed")
        self.assertEqual(first, {"benchmark": "A", "generator": "g", "dataset": "first",
                                 "benchmark-tag": True, "dense": True, "generator-tag": True})
        self.assertFalse(failed["dense"])
        self.assertEqual(rows[0]["framework"], "Alpha")
        self.assertEqual(rows[0]["value"], 4)
        self.assertTrue(all(row["dataset"] == "first" for row in rows))
        self.assertNotIn("status", rows[0])

    def test_all_metrics_and_repeated_measurements_are_preserved(self):
        measurements = self.results["benchmarks"][0]["generators"][0]["datasets"][0]["results"]
        measurements += [measurement("a", 8), measurement("a", 1024, metric="memory")]
        rows, _, _ = build_tables(self.results, self.metadata)
        self.assertEqual(len(rows), 4)
        self.assertEqual([r["value"] for r in rows if r["metric"] == "memory"], [1024])
        self.assertEqual([r["value"] for r in rows if r["dataset"] == "first" and r["framework"] == "Alpha" and r["metric"] == "time"], [4, 8])

    def test_invalid_values_and_failed_status_are_omitted(self):
        measurements = self.results["benchmarks"][0]["generators"][0]["datasets"][0]["results"]
        measurements[:] = [measurement("a", value) for value in [None, True, "2", float("nan"), float("inf"), 0, -1]]
        measurements.append(measurement("a", 4, "failed"))
        rows, _, _ = build_tables(self.results, self.metadata)
        first = [row for row in rows if row["dataset"] == "first"]
        self.assertEqual([row["value"] for row in first], [0, -1])

    def test_all_failed_run_still_describes_every_dataset(self):
        for dataset in self.results["benchmarks"][0]["generators"][0]["datasets"]:
            dataset["results"] = [measurement("a", None, "failed")]
        rows, benchmarks, _ = build_tables(self.results, self.metadata)
        self.assertEqual(rows, [])
        self.assertEqual(len(benchmarks), 2)

    def test_same_dataset_name_in_different_generators_has_distinct_join_keys(self):
        other = copy.deepcopy(self.results["benchmarks"][0]["generators"][0])
        other["name"] = "other"
        self.results["benchmarks"][0]["generators"].append(other)
        self.metadata["benchmarks"][0]["generators"].append(copy.deepcopy(other))
        _, benchmarks, _ = build_tables(self.results, self.metadata)
        self.assertEqual(len(benchmarks), 4)
        self.assertEqual(len({tuple(row[column] for column in DATASET_COLUMNS) for row in benchmarks}), 4)

    def test_csv_round_trip_escapes_names_and_uses_explicit_true_false(self):
        self.results["benchmarks"][0]["name"] = self.metadata["benchmarks"][0]["name"] = 'A, "quoted"\nname'
        rows, benchmarks, tags = build_tables(self.results, self.metadata)
        with tempfile.TemporaryDirectory() as directory:
            result_path = Path(directory) / "results.csv"
            description_path = Path(directory) / "benchmarks.csv"
            write_csv(result_path, RESULT_COLUMNS, rows)
            write_csv(description_path, DATASET_COLUMNS + tags, benchmarks)
            with result_path.open(newline="") as handle:
                saved = list(csv.DictReader(handle))
            with description_path.open(newline="") as handle:
                saved_benchmarks = list(csv.DictReader(handle))
        self.assertEqual(saved[0]["benchmark"], 'A, "quoted"\nname')
        self.assertEqual({row["dense"] for row in saved_benchmarks}, {"true", "false"})
        self.assertEqual(saved[0]["value"], "4")
        self.assertNotIn("status", saved[0])

    def test_missing_metadata_and_empty_results_fail_visibly(self):
        with self.assertRaisesRegex(ValueError, "Missing tag metadata"):
            build_tables(self.results, {"benchmarks": []})
        self.results["benchmarks"] = []
        with self.assertRaisesRegex(ValueError, "no datasets"):
            build_tables(self.results, self.metadata)


class LatestRunTest(unittest.TestCase):
    def test_numeric_order_and_only_aggregated_result_files(self):
        tree = {"tree": [
            {"type": "blob", "path": "competition/run_9/results.json"},
            {"type": "blob", "path": "competition/run_10/results.json"},
            {"type": "tree", "path": "competition/run_12"},
            {"type": "blob", "path": "competition/run_11/task_0/results.json"},
        ]}
        self.assertEqual(latest_results_path(tree), "competition/run_10/results.json")

    def test_missing_and_truncated_trees_fail(self):
        with self.assertRaisesRegex(ValueError, "No competition"):
            latest_results_path({"tree": []})
        with self.assertRaisesRegex(ValueError, "truncated"):
            latest_results_path({"tree": [], "truncated": True})


if __name__ == "__main__":
    unittest.main()
