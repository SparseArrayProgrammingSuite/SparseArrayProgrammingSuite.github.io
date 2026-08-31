---
layout: home
title: "Sparse Array Programming Suite"
author_profile: false
---

Sparse array frameworks are becoming increasingly capable, but their performance depends heavily on input sparsity patterns and full application structure. The Sparse Array Programming Suite provides realistic applications for making informed design and implementation decisions.

The programs are adapted from real-world applications using a straightforward array-programming style. Each benchmark is plain Python built from [Array API](https://data-apis.org/array-api/latest/API_specification/) functions, collective operations such as `+`, `*`, `sum`, and `reduce`, minimal control flow, and no framework-specific shortcuts.

[Explore the benchmarks]({{ '/benchmarks/' | relative_url }}){: .btn .btn--primary }
[View the leaderboard]({{ '/leaderboard/' | relative_url }}){: .btn .btn--info }

## Run the suite

Install the project and its test dependencies with Poetry:

```bash
git clone https://github.com/SparseArrayProgrammingSuite/SparseArrayProgrammingSuite.git
cd SparseArrayProgrammingSuite
poetry install --with test
```

Run a quick CI-sized benchmark matrix:

```bash
poetry run ./bin/run_benchmark.py --tag test --quick --timeout 30
```

Run the canonical datasets with time and peak-memory metrics:

```bash
poetry run ./bin/run_benchmark.py --tag standard --metric time peakmem
```

Results and cached datasets are written beneath `.saps/outputs/`. See the [project README](https://github.com/SparseArrayProgrammingSuite/SparseArrayProgrammingSuite#readme) for configuration, custom framework, storage, tracing, and contribution instructions.
