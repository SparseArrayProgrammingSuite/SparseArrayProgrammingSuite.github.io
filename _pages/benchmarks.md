---
title: "Benchmarks"
permalink: /benchmarks/
layout: single
author_profile: false
---

The suite adapts real applications to a portable array-programming style. This catalog is generated from [`metadata.json`](https://github.com/SparseArrayProgrammingSuite/SparseArrayProgrammingSuite/blob/main/metadata.json) in the main repository.

<style>
  .ccs-concepts ccs2012,
  .ccs-concepts concept,
  .ccs-concepts concept_desc {
    display: block;
  }

  .ccs-concepts concept {
    margin: 0.35rem 0;
  }

  .ccs-concepts concept_desc::before {
    content: "• ";
  }

  .ccs-concepts concept_id,
  .ccs-concepts concept_significance {
    display: none;
  }

  .benchmark-generators {
    margin-left: 1rem;
  }
</style>

{% assign benchmarks = site.data.metadata.benchmarks %}
{% if benchmarks and benchmarks.size > 0 %}
  {% for benchmark in benchmarks %}
## {{ benchmark.pretty_name | default: benchmark.name }}

{{ benchmark.description }}

{% if benchmark.authors and benchmark.authors.size > 0 %}**Authors:** {{ benchmark.authors | join: ", " }}  
{% endif %}**Source:** [`{{ benchmark.file }}`](https://github.com/SparseArrayProgrammingSuite/SparseArrayProgrammingSuite/blob/main/{{ benchmark.file }})

{% if benchmark.concepts contains "<concept>" %}**ACM Computing Classification System**

<div class="ccs-concepts">
{{ benchmark.concepts }}
</div>
{% endif %}

{% if benchmark.motivation and benchmark.motivation != "" %}<details>
<summary>Motivation</summary>

{{ benchmark.motivation }}

</details>{% endif %}

{% if benchmark.generators and benchmark.generators.size > 0 %}
### Input generators

<div class="benchmark-generators">
{% for generator in benchmark.generators %}
#### {{ generator.pretty_name | default: generator.name }}

{{ generator.description }}

{% if generator.motivation and generator.motivation != "" %}{{ generator.motivation }}
{% endif %}
{% endfor %}
</div>
{% endif %}

{% if benchmark.references and benchmark.references.size > 0 %}
### References

<ol>
{% for reference in benchmark.references %}<li>{{ reference }}</li>{% endfor %}
</ol>
{% endif %}

  {% endfor %}
{% else %}
Benchmark metadata is unavailable in this local build. The deployed site fetches it automatically from the main repository.
{% endif %}
