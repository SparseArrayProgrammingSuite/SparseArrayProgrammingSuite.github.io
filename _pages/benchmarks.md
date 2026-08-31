---
title: "Benchmarks"
permalink: /benchmarks/
layout: single
author_profile: false
---

The suite adapts real applications to a portable array-programming style. This catalog is generated from [`metadata.json`](https://github.com/SparseArrayProgrammingSuite/SparseArrayProgrammingSuite/blob/main/metadata.json) in the main repository.

{% assign benchmarks = site.data.metadata.benchmarks %}
{% if benchmarks and benchmarks.size > 0 %}
  {% for benchmark in benchmarks %}
    {% include benchmark.html benchmark=benchmark %}
  {% endfor %}
{% else %}
Benchmark metadata is unavailable in this local build. The deployed site fetches it automatically from the main repository.
{% endif %}
