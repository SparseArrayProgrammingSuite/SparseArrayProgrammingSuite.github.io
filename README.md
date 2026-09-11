# SAPS website

The leaderboard uses the existing Observable performance profile in
[`docs/index.md`](docs/index.md), embedded in the Jekyll leaderboard page.

## Preview the plot

With Node.js 22 and Python 3.12 installed:

```sh
npm ci
npm run data
npm run dev
```

`npm run data` finds the highest numbered `competition/run_*/results.json` present
on the suite repository's `main` branch. It fetches that result and its referenced
tag metadata at the same commit, then generates the two CSVs below in `docs/data/`.
Observable reads those files. Run `npm run data` again to refresh the snapshot.

To use previously downloaded inputs:

```sh
python3 scripts/build_competition_data.py --results /path/to/results.json --metadata /path/to/metadata.json
```

`--metadata` is optional when the metadata path referenced by `results.json` exists
relative to that file. Use `--output-dir` to write the CSVs elsewhere.

## CSV schema

| File | Columns | Rows |
| --- | --- | --- |
| `results.csv` | `framework,benchmark,generator,dataset,metric,value` | One row per successful, finite numeric measurement; all metrics and repeated measurements are preserved. |
| `benchmarks.csv` | `benchmark,generator,dataset,<one column per tag>` | One row per dataset in the run, including datasets whose measurements all failed. Tag cells are `true` or `false`. |

Join the tables on **benchmark, generator, and dataset** together; dataset names
can repeat between generators or benchmarks. Values retain the source units.
Failed or invalid measurements are omitted from `results.csv`, so it needs no
status column. Tags combine the benchmark, generator, and dataset metadata.
A small `run.json` records the source commit, run, and framework names, including
frameworks with no successes.

The profile uses successful, finite, positive `time` results, normalized to the
best runtime per benchmark–generator–dataset problem. Repeated successful
measurements for one framework use their median. Failed problems remain in the
denominator, including problems where every framework failed. Each benchmark
has equal weight, split over its selected datasets, as in the original plot.
The controls list only tags attached to problems in the selected run.

## Build the website

```sh
npm test
npm run build
bundle exec jekyll build
```

Observable writes to `assets/leaderboard/`, which Jekyll copies to the site.
The GitHub Actions workflow fetches the latest competition snapshot and metadata
before building Observable and Jekyll. Generated data and chart assets are ignored
by Git. A new suite run appears on the next website build; use the workflow's
manual trigger to refresh without changing this repository.

The embedding follows [Observable Framework's iframe embedding support](https://observablehq.github.io/framework/embeds).
