---
title: "Leaderboard"
permalink: /leaderboard/
layout: single
author_profile: false
---

<style>
  #observablehq-main { min-height: 0; }
  .saps-observable {
    font: inherit;
    color: inherit;
  }
  .saps-observable p,
  .saps-observable li,
  .saps-observable figure,
  .saps-observable figcaption,
  .saps-observable h1,
  .saps-observable h2,
  .saps-observable h3,
  .saps-observable h4,
  .saps-observable h5,
  .saps-observable h6 {
    max-width: none;
  }
  .saps-observable a {
    color: inherit;
  }
  .saps-observable .observablehq--block {
    margin: 0;
  }
  .saps-observable .observablehq--block form {
    display: flex;
    flex-wrap: wrap;
    gap: 0.0rem;
    align-items: flex-start;
    margin: 0;
  }
  .saps-tag-menu {
    display: inline-block;
    min-width: 0;
    width: 9.7rem;
    max-width: 9.7rem;
    position: relative;
    vertical-align: top;
  }
  .saps-tag-count-left {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.35rem 0.65rem;
    margin-right: 0.2rem;
    font-size: 0.68rem;
    line-height: 1;
    color: #ffffff;
    background: #4f2f82;
    border-radius: 999px;
    font-weight: 700;
    box-shadow: 0 1px 2px rgba(0,0,0,0.06);
    box-sizing: border-box;
    position: relative;
    transform: translateY(1px);
  }
  .saps-tag-menu summary {
    list-style: none;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.45rem;
    width: 100%;
    padding: 0.4rem 0.75rem;
    border: 1px solid #d9d9e3;
    border-radius: 999px;
    background: #f6f3fb;
    font-size: 0.68rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: #4f2f82;
    font-weight: 700;
    line-height: 1.2;
    box-sizing: border-box;
  }
  .saps-tag-menu summary::-webkit-details-marker { display: none; }
  .saps-tag-menu summary::after {
    content: "▾";
    font-size: 0.72rem;
  }
  .saps-tag-menu[open] summary::after {
    content: "▴";
  }
  .saps-tag-menu__panel {
    margin-top: 0.25rem;
    padding: 0.35rem 0.5rem;
    border: 1px solid #d9d9e3;
    border-radius: 0.75rem;
    background: #fff;
    box-shadow: 0 0.5rem 1rem rgba(30, 30, 30, 0.06);
    position: absolute;
    left: 0;
    z-index: 20;
    box-sizing: border-box;
    width: 9.7rem;
    max-width: 9.7rem;
    min-width: 0;
    max-height: 15rem;
    overflow-y: auto;
    overflow-x: hidden;
  }
  .saps-tag-menu__actions {
    display: flex;
    gap: 0.2rem;
    margin-bottom: 0.2rem;
    position: relative;
    z-index: 30;
  }
  .saps-tag-menu__action {
    appearance: none;
    border: 1px solid #d9d9e3;
    border-radius: 999px;
    background: #f6f3fb;
    color: #4f2f82;
    font-size: 0.56rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    font-weight: 700;
    padding: 0.2rem 0.38rem;
    line-height: 1.2;
    cursor: pointer;
  }
  .saps-tag-menu .inputs-3a86ea-checkbox {
    display: flex;
    flex-direction: column;
    gap: 0.15rem;
    width: 100%;
    max-width: 100%;
    min-width: 0;
    background: transparent;
    border: 0;
    box-shadow: none;
    margin: 0;
    padding: 0;
    position: static;
    z-index: auto;
    box-sizing: border-box;
  }
  .saps-tag-menu__section {
    display: flex;
    flex-direction: column;
    gap: 0.1rem;
  }
  .saps-tag-menu__section + .saps-tag-menu__section {
    margin-top: 0.25rem;
  }
  .saps-tag-menu__section-label {
    font-size: 0.52rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #625b79;
    font-weight: 700;
    padding: 0.04rem 0;
  }
  .saps-tag-menu + .saps-tag-menu {
    margin-left: 0;
  }
  @media (min-width: 42rem) {
    .saps-tag-menu + .saps-tag-menu {
      margin-left: 0.2rem;
    }
  }
  .saps-tag-menu .inputs-3a86ea-checkbox label {
    display: inline-flex;
    align-items: flex-start;
    gap: 0.25rem;
    width: 100%;
    max-width: 100%;
    min-width: 0;
    margin-right: 0;
    font-size: 0.58rem;
    color: #2b2b2b;
    font-weight: 500;
    white-space: normal;
    overflow-wrap: anywhere;
    word-break: break-word;
    line-height: 1.2;
  }
  .saps-tag-menu .inputs-3a86ea-checkbox > label:first-child {
    display: none;
  }
  .saps-tag-menu input[type="checkbox"] {
    margin: 0 0.35rem 0 0;
  }
  @media (max-width: 42rem) {
    .saps-tag-menu { min-width: 100%; }
    .saps-tag-menu .inputs-3a86ea-checkbox { width: min(18rem, calc(100vw - 4rem)); }
  }
  .plot-d6a7b5-figure {
    justify-content: right;
    margin: 0.1rem 0.5rem;
  }
</style>
{%- assign inputs_file = site.static_files | where_exp: "f", "f.path contains '/assets/leaderboard/_observablehq/stdlib/inputs.'" | first -%}
{%- if inputs_file -%}
  <link rel="stylesheet" type="text/css" href="{{ inputs_file.path | relative_url }}">
{%- endif -%}

<div id="observablehq-center" class="saps-observable">
  <main id="observablehq-main" class="observablehq">
    <div class="observablehq observablehq--block" ><!--:03c27090:--></div>
    <div class="observablehq observablehq--block"><!--:7ebc449c:--></div>
    <div class="observablehq observablehq--block"><!--:2d01d479:--></div>
    <div class="observablehq observablehq--block"><observablehq-loading></observablehq-loading><!--:a415e9ad:--></div>
    <p>Results from <observablehq-loading></observablehq-loading><!--:7688b8fd:-->. Each benchmark has equal weight, divided among its selected datasets.
    At 1×, a framework matches the fastest runtime for a problem. At 2×, it takes at most twice as long. Failed measurements remain in the suite but do not contribute successes. Include tags match any selection; exclude tags must be absent.</p>
  </main>
</div>

<script type="module">
  {%- assign client_file = site.static_files | where_exp: "f", "f.path contains '/assets/leaderboard/_observablehq/client.'" | first -%}
  {%- assign stdlib_file = site.static_files | where_exp: "f", "f.path contains '/assets/leaderboard/_observablehq/stdlib.'" | first -%}
  {%- assign profile_import = site.static_files | where_exp: "f", "f.path contains '/assets/leaderboard/_import/components/profile.'" | first -%}
  {%- assign benchmarks_file = site.static_files | where_exp: "f", "f.path contains '/assets/leaderboard/_file/data/benchmarks.'" | first -%}
  {%- assign results_file = site.static_files | where_exp: "f", "f.path contains '/assets/leaderboard/_file/data/results.'" | first -%}
  {%- assign run_file = site.static_files | where_exp: "f", "f.path contains '/assets/leaderboard/_file/data/run.'" | first -%}

  {%- if client_file -%}
    import {define} from "{{ client_file.path | relative_url }}";
  {%- endif -%}
  {%- if stdlib_file -%}
    import {registerFile} from "{{ stdlib_file.path | relative_url }}";
  {%- endif -%}

  {%- if benchmarks_file -%}
    registerFile("./data/benchmarks.csv", {"name":"./data/benchmarks.csv","mimeType":"text/csv","path":"{{ benchmarks_file.path | relative_url }}"});
  {%- endif -%}
  {%- if results_file -%}
    registerFile("./data/results.csv", {"name":"./data/results.csv","mimeType":"text/csv","path":"{{ results_file.path | relative_url }}"});
  {%- endif -%}
  {%- if run_file -%}
    registerFile("./data/run.json", {"name":"./data/run.json","mimeType":"application/json","path":"{{ run_file.path | relative_url }}"});
  {%- endif -%}

  define({id: "03c27090", inputs: ["FileAttachment"], outputs: ["buildProfile","results","benchmarks","run","profile"], body: async (FileAttachment) => {
    {%- if profile_import -%}
      const {buildProfile} = await import("{{ profile_import.path | relative_url }}");
    {%- else -%}
      throw new Error('Observable profile component not found: /assets/leaderboard/_import/components/profile.*');
    {%- endif -%}
    const [results, benchmarks, run] = await Promise.all([
      FileAttachment("./data/results.csv").csv(),
      FileAttachment("./data/benchmarks.csv").csv(),
      FileAttachment("./data/run.json").json()
    ]);
    const profile = buildProfile(results, benchmarks, run.frameworks);
    return {buildProfile,results,benchmarks,run,profile};
  }});

  define({id: "7688b8fd", mode: "inline", inputs: ["html","run","display"], body: async (html,run,display) => {
    display(await (
      html`<a href=${run.resultsUrl} target="_blank" rel="noopener">${run.run}</a>`
    ))
  }});

  define({id: "7ebc449c", inputs: ["profile","view","Inputs"], outputs: ["allTags","keep","drop"], body: (profile,view,Inputs) => {
    const hiddenTags = new Set(["standard", "test", "trace"]);
    const allTags = [...new Set(profile.problems.flatMap((p) => p.tags))]
      .filter((tag) => !hiddenTags.has(tag))
      .sort();

    const workloadTags = new Set([
      "high-dimensional",
      "tensor",
      "large-query",
      "elementary-ops",
      "transcendental-ops",
      "shape-ops",
      "linalg-ops",
      "fancy-ops",
      "index-ops",
      "nonzero-fill",
      "iterative",
      "dense",
      "hypersparse",
      "dynamic-sparsity"
    ]);

    const keep = view(Inputs.checkbox(allTags, {label: "Include tags", value: []}));
    const drop = view(Inputs.checkbox(allTags, {label: "Exclude tags", value: []}));

    const updateCount = () => {
      const root = document.querySelector('#observablehq-main');
      if (!root) return;

      const keepForm = root.querySelector('.saps-tag-menu[data-menu-label="Include tags"] form');
      const dropForm = root.querySelector('.saps-tag-menu[data-menu-label="Exclude tags"] form');

      const getTags = (frm) => {
        if (!frm) return [];
        const checked = Array.from(frm.querySelectorAll('input[type="checkbox"]:checked'));
        return checked.map((cb) => cb.closest('label')?.textContent?.trim() || '');
      };

      const keep = getTags(keepForm);
      const drop = getTags(dropForm);

      const ok = profile.problems.map((p) =>
        (keep.length === 0 || p.tags.some((t) => keep.includes(t))) &&
        !p.tags.some((t) => drop.includes(t))
      );
      const kept = ok.filter(Boolean).length;
      const total = profile.problems.length || 0;

      const keepLeft = root.querySelector('.saps-tag-count-left[data-menu-label="Include tags"]');
      if (keepLeft) keepLeft.textContent = `${kept} problems`;
    };

    const wrapMenu = (form, labelText) => {
      if (!form || form.closest('.saps-tag-menu')) return;

      const wrapper = document.createElement('details');
      wrapper.className = 'saps-tag-menu';
      wrapper.open = false;

      const summary = document.createElement('summary');
      summary.textContent = labelText;

      // no inline pill badge; count shown to the left only

      const panel = document.createElement('div');
      panel.className = 'saps-tag-menu__panel';

      const sectionOrder = ['workload', 'concepts'];
      const sectionMap = new Map();
      sectionOrder.forEach((name) => {
        const section = document.createElement('div');
        section.className = 'saps-tag-menu__section';
        const heading = document.createElement('div');
        heading.className = 'saps-tag-menu__section-label';
        heading.textContent = name;
        section.appendChild(heading);
        sectionMap.set(name, section);
      });

      const labels = [...form.querySelectorAll('label')].filter((label) => {
        const text = (label.textContent || '').trim();
        return text && !/Include tags|Exclude tags/i.test(text);
      });

      labels.forEach((label) => {
        const tag = (label.textContent || '').trim();
        const sectionKey = workloadTags.has(tag) ? 'workload' : 'concepts';
        const section = sectionMap.get(sectionKey);
        if (section) section.appendChild(label);
      });

      form.innerHTML = '';
      sectionOrder.forEach((name) => {
        const section = sectionMap.get(name);
        if (section && section.childElementCount > 1) form.appendChild(section);
      });

      const parent = form.parentNode;
      if (!parent) return;

      parent.insertBefore(wrapper, form);
      wrapper.append(summary, panel);
      panel.append(form);

      // mark wrapper so we can find it later
      wrapper.dataset.menuLabel = labelText;

      // insert a left-side badge only for the Include tags menu so the
      // count appears to the left of that pill. Keep it if present.
      if (labelText === 'Include tags') {
        let leftBadge = parent.querySelector('.saps-tag-count-left[data-menu-label="' + labelText + '"]');
        if (!leftBadge) {
          leftBadge = document.createElement('span');
          leftBadge.className = 'saps-tag-count-left';
          leftBadge.dataset.menuLabel = labelText;
          parent.insertBefore(leftBadge, wrapper);
        }
      }

      // when the form changes, update the count
      form.addEventListener('change', () => {
        updateCount();
      });

      // set initial count after wrapping
      updateCount();
    };

    queueMicrotask(() => {
      const root = document.querySelector('#observablehq-main');
      if (!root) return;

      const wrapVisibleForms = () => {
        const forms = [...root.querySelectorAll('form')];
        forms.forEach((form) => {
          const label = form.querySelector('label');
          const labelText = label?.textContent?.trim();
          if (!labelText || !/Include tags|Exclude tags/.test(labelText)) return;
          if (form.closest('.saps-tag-menu')) return;
          wrapMenu(form, labelText);
        });
      };

      wrapVisibleForms();

      // initial count
      updateCount();

      const observer = new MutationObserver(() => {
        wrapVisibleForms();
      });
      observer.observe(root, {childList: true, subtree: true});
    });

    return {allTags, keep: keep ?? [], drop: drop ?? []};
  }});

  define({id: "2d01d479", inputs: ["profile","keep","drop"], outputs: ["ok","nKept","total","curves"], body: (profile,keep,drop) => {
    const ok = profile.problems.map((p) =>
      (keep.length === 0 || p.tags.some((t) => keep.includes(t))) &&
      !p.tags.some((t) => drop.includes(t))
    );

    const nKept = new Map();
    profile.problems.forEach((p, i) => {
      if (ok[i]) nKept.set(p.benchmark, (nKept.get(p.benchmark) ?? 0) + 1);
    });
    const total = nKept.size;

    const curves = total === 0 ? [] : Object.entries(profile.series).flatMap(([framework, points]) => {
      let cum = 0;
      const pts = points
        .filter(([i, ratio]) => ok[i] && ratio <= 100)
        .map(([i, ratio]) => ({
          framework,
          ratio,
          pct: (100 * (cum += 1 / nKept.get(profile.problems[i].benchmark))) / total
        }));
      pts.unshift({framework, ratio: 1, pct: 0});
      pts.push({framework, ratio: profile.xMax, pct: pts.at(-1)?.pct ?? 0});
      return pts;
    });
    return {ok,nKept,total,curves};
  }});

  define({id: "a415e9ad", inputs: ["total","html","Plot","ok","width","profile","curves","display"], body: async (total,html,Plot,ok,width,profile,curves,display) => {
    const plotData = curves.length ? curves : [{framework: "", ratio: 1, pct: 0}, {framework: "", ratio: 1, pct: 0}];
    display(await (
      Plot.plot({
      width,
      x: {type: "log", domain: [1, Math.max(1, profile.xMax)], label: "Target Performance Ratio (runtime / best runtime)"},
      y: {domain: [0, 100], grid: true, label: "% of suite completed"},
      color: {legend: true, domain: Object.keys(profile.series)},
      marks: [
        Plot.line(plotData, {
          x: "ratio",
          y: "pct",
          stroke: "framework",
          curve: "step-after",
          strokeWidth: 3,
          tip: true
        })
      ]
      })
    ))
  }});

</script>

# Workload Tags

Each benchmark/dataset is tagged with workload descriptors, discovered programmatically through tracing. The table below lists each tag and a short description.

| Tag | Description |
| --- | --- |
| `high-dimensional` | 5 or more dimensions in a tensor. |
| `tensor` | 3 or more dimensions in a tensor. |
| `large-query` | 5 or more operands on one line. |
| `elementary-ops` | PEMDAS-only. |
| `transcendental-ops` | Contains sin, cos, pow, exp, or related operations. |
| `shape-ops` | Reshape, concat, transpose, squeeze, or similar operations. |
| `linalg-ops` | Contains `xp.linalg` or solver-like operations; `dot` is okay. |
| `fancy-ops` | min, max, and, or, shift, or similar operations. |
| `index-ops` | Contains indexing. |
| `nonzero-fill` | Uses a fill value other than zero. |
| `iterative` | Loops over a matrix or repeats until convergence. |
| `dense` | Exclusively dense problems. |
| `hypersparse` | Contains hypersparsity, such as `nnz << n` for a dimension. |
| `dynamic-sparsity` | Sparse-sparse interactions may change the sparsity pattern. |