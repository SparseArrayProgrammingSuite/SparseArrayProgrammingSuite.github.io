---
title: "Benchmarks"
permalink: /benchmarks/
layout: single
author_profile: false
---

The suite adapts real applications to a portable array-programming style. This catalog is generated from [`metadata.json`](https://github.com/SparseArrayProgrammingSuite/SparseArrayProgrammingSuite/blob/main/metadata.json) in the main repository.

<style>
  .benchmark {
    margin: 0 0 1rem;
    padding: 0.25rem 1rem;
    border: 1px solid #d9d9e3;
    border-radius: 0.4rem;
  }

  .benchmark > summary {
    padding: 0.85rem 0;
    cursor: pointer;
    font-size: 1.2rem;
    font-weight: 700;
  }

  .generator-disclosure {
    margin: 1rem 0;
  }

  .generator-disclosure > summary {
    cursor: pointer;
    font-weight: 700;
  }

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
    display: grid;
    gap: 0.75rem;
    margin: 1rem 0 2rem;
  }

  .benchmark-generator {
    padding: 0.9rem 1rem;
    border-left: 3px solid #6f42c1;
    background: #f7f5fb;
  }

  .benchmark-generator h4 {
    margin: 0 0 0.35rem;
  }

  .benchmark-generator p:last-child {
    margin-bottom: 0;
  }
</style>

{% assign benchmarks = site.data.metadata.benchmarks %}
{% if benchmarks and benchmarks.size > 0 %}
  {% for benchmark in benchmarks %}
<details class="benchmark" markdown="1">
<summary>{{ benchmark.pretty_name | default: benchmark.name }}</summary>

{{ benchmark.description }}

{% if benchmark.authors and benchmark.authors.size > 0 %}**Authors:** {{ benchmark.authors | join: ", " }}  
{% endif %}**Source:** [`{{ benchmark.file }}`](https://github.com/SparseArrayProgrammingSuite/SparseArrayProgrammingSuite/blob/main/{{ benchmark.file }})

{% if benchmark.concepts contains "<concept>" %}**ACM Computing Classification System**

<div class="ccs-concepts">
{{ benchmark.concepts | replace: "~", " › " }}
</div>
{% endif %}

{% if benchmark.motivation and benchmark.motivation != "" %}
### Motivation

{{ benchmark.motivation }}
{% endif %}

{% if benchmark.generators and benchmark.generators.size > 0 %}
<details class="generator-disclosure">
<summary>Input generators ({{ benchmark.generators.size }})</summary>

<div class="benchmark-generators">
{% for generator in benchmark.generators %}
<section class="benchmark-generator">
  <h4>{{ generator.pretty_name | default: generator.name }}</h4>
  {{ generator.description | markdownify }}
  {% if generator.motivation and generator.motivation != "" %}{{ generator.motivation | markdownify }}{% endif %}
</section>
{% endfor %}
</div>
</details>
{% endif %}

{% if benchmark.references and benchmark.references.size > 0 %}
### References

<ol>
{% for reference in benchmark.references %}<li>{{ reference }}</li>{% endfor %}
</ol>
{% endif %}

</details>

  {% endfor %}
{% else %}
Benchmark metadata is unavailable in this local build. The deployed site fetches it automatically from the main repository.
{% endif %}
