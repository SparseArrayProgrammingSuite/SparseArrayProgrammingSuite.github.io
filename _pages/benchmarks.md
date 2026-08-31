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
## {{ benchmark.pretty_name | default: benchmark.name }}

{{ benchmark.description }}

{% if benchmark.authors and benchmark.authors.size > 0 %}**Authors:** {{ benchmark.authors | join: ", " }}  
{% endif %}{% if benchmark.topics and benchmark.topics.size > 0 %}**Topics:** {{ benchmark.topics | join: ", " }}  
{% endif %}{% if benchmark.generators and benchmark.generators.size > 0 %}**Input generators:** {{ benchmark.generators.size }}  
{% endif %}**Source:** [`{{ benchmark.file }}`](https://github.com/SparseArrayProgrammingSuite/SparseArrayProgrammingSuite/blob/main/{{ benchmark.file }})

{% if benchmark.motivation and benchmark.motivation != "" %}<details>
<summary>Motivation</summary>

{{ benchmark.motivation }}

</details>{% endif %}

  {% endfor %}
{% else %}
Benchmark metadata is unavailable in this local build. The deployed site fetches it automatically from the main repository.
{% endif %}
