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
    margin: 0 0 0.75rem;
  }
  .saps-observable .observablehq--block form {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    align-items: flex-start;
    margin: 0;
  }
  .saps-tag-menu {
    display: inline-block;
    min-width: 0;
    width: 13rem;
    max-width: 13rem;
    position: relative;
    vertical-align: top;
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
    width: 13rem;
    max-width: 13rem;
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
      margin-left: 0.5rem;
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
</style>
<link rel="stylesheet" type="text/css" href="{{ '/assets/leaderboard/_observablehq/stdlib/inputs.f7bf0e12.css' | relative_url }}">

<div id="observablehq-center" class="saps-observable">
  <main id="observablehq-main" class="observablehq">
    <div class="observablehq observablehq--block"><!--:03c27090:--></div>
    <p>Results from <observablehq-loading></observablehq-loading><!--:7688b8fd:-->. Each benchmark has equal weight, divided among its selected datasets.</p>
    <div class="observablehq observablehq--block"><!--:7ebc449c:--></div>
    <div class="observablehq observablehq--block"><!--:2d01d479:--></div>
    <div class="observablehq observablehq--block"><observablehq-loading></observablehq-loading><!--:a415e9ad:--></div>
    <p>At 1×, a framework matches the fastest runtime for a problem. At 2×, it takes at most twice as long. Failed measurements remain in the suite but do not contribute successes. Include tags match any selection; exclude tags take precedence.</p>
  </main>
</div>

<script type="module">
  import {define} from "{{ '/assets/leaderboard/_observablehq/client.189d7a0d.js' | relative_url }}";
  import {registerFile} from "{{ '/assets/leaderboard/_observablehq/stdlib.81cd90e3.js' | relative_url }}";

  registerFile("./data/benchmarks.csv", {"name":"./data/benchmarks.csv","mimeType":"text/csv","path":"{{ '/assets/leaderboard/_file/data/benchmarks.c1e63a4d.csv' | relative_url }}","lastModified":1789162235465,"size":1127968});
  registerFile("./data/results.csv", {"name":"./data/results.csv","mimeType":"text/csv","path":"{{ '/assets/leaderboard/_file/data/results.2ce9b38c.csv' | relative_url }}","lastModified":1789162235438,"size":245230});
  registerFile("./data/run.json", {"name":"./data/run.json","mimeType":"application/json","path":"{{ '/assets/leaderboard/_file/data/run.d161b0e4.json' | relative_url }}","lastModified":1789162235465,"size":339});

  define({id: "03c27090", inputs: ["FileAttachment"], outputs: ["buildProfile","results","benchmarks","run","profile"], body: async (FileAttachment) => {
    const {buildProfile} = await import("{{ '/assets/leaderboard/_import/components/profile.1c1f73f4.js' | relative_url }}");
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

    const keep = view(Inputs.checkbox(allTags, {label: "Include tags", value: allTags}));
    const drop = view(Inputs.checkbox(allTags, {label: "Exclude tags", value: []}));

    const wrapMenu = (form, labelText) => {
      if (!form || form.closest('.saps-tag-menu')) return;

      const wrapper = document.createElement('details');
      wrapper.className = 'saps-tag-menu';
      wrapper.open = false;

      const summary = document.createElement('summary');
      summary.textContent = labelText;

      const panel = document.createElement('div');
      panel.className = 'saps-tag-menu__panel';

      const actions = document.createElement('div');
      actions.className = 'saps-tag-menu__actions';

      const selectAll = document.createElement('button');
      selectAll.type = 'button';
      selectAll.className = 'saps-tag-menu__action';
      selectAll.textContent = 'Select all';

      const deselectAll = document.createElement('button');
      deselectAll.type = 'button';
      deselectAll.className = 'saps-tag-menu__action';
      deselectAll.textContent = 'Deselect all';

      const applySelection = (checked) => {
        const boxes = [...form.querySelectorAll('input[type="checkbox"]')];
        boxes.forEach((box) => {
          if (box.checked !== checked) {
            box.checked = checked;
            box.dispatchEvent(new Event('input', {bubbles: true}));
            box.dispatchEvent(new Event('change', {bubbles: true}));
          }
        });
      };

      selectAll.addEventListener('click', (event) => {
        event.preventDefault();
        applySelection(true);
      });

      deselectAll.addEventListener('click', (event) => {
        event.preventDefault();
        applySelection(false);
      });

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
      actions.append(selectAll, deselectAll);
      panel.append(actions, form);
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
        .filter(([i]) => ok[i])
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
    display(await (
      total === 0 ? html`<p role="status">No problems match these tags.</p>` : Plot.plot({
        title: `${ok.filter(Boolean).length} problems`,
        width,
        x: {type: "log", domain: [1, profile.xMax], label: "Ratio (runtime / best runtime)"},
        y: {domain: [0, 100], grid: true, label: "% of suite completed"},
        color: {legend: true, domain: Object.keys(profile.series)},
        marks: [
          Plot.line(curves, {
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
