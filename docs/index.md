---
title: Performance profile
---

<style>
.saps-tag-menu-row {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.4rem;
}
.saps-tag-count {
  font-size: 0.68rem;
  color: var(--theme-foreground-muted, #625b79);
}
.saps-tag-menu {
  display: inline-block;
  min-width: 0;
  width: 9.7rem;
  max-width: 9.7rem;
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
  border: 1px solid var(--theme-foreground-faintest, #d9d9e3);
  border-radius: 999px;
  font-size: 0.68rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  font-weight: 700;
  line-height: 1.2;
  box-sizing: border-box;
}
.saps-tag-menu summary::-webkit-details-marker {
  display: none;
}
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
  border: 1px solid var(--theme-foreground-faintest, #d9d9e3);
  border-radius: 0.75rem;
  background: var(--theme-background, #fff);
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
.saps-tag-menu__section {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
}
.saps-tag-menu__section + .saps-tag-menu__section {
  margin-top: 0.25rem;
}
.saps-tag-menu__section-label {
  font-size: 0.52rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--theme-foreground-muted, #625b79);
  font-weight: 700;
  padding: 0.04rem 0;
}
.saps-tag-menu__panel label {
  display: flex;
  align-items: flex-start;
  gap: 0.25rem;
  width: 100%;
  max-width: 100%;
  min-width: 0;
  font-size: 0.58rem;
  font-weight: 500;
  white-space: normal;
  overflow-wrap: anywhere;
  word-break: break-word;
  line-height: 1.2;
}
.saps-tag-menu__panel input[type="checkbox"] {
  margin: 0 0.35rem 0 0;
}
@media (max-width: 42rem) {
  .saps-tag-menu { min-width: 100%; }
  .saps-tag-menu__panel { width: min(18rem, calc(100vw - 4rem)); }
}
</style>

```js
import {buildProfile} from "./components/profile.js";
import {tagMenu} from "./components/tagMenu.js";
const [results, benchmarks, run] = await Promise.all([
  FileAttachment("./data/results.csv").csv(),
  FileAttachment("./data/benchmarks.csv").csv(),
  FileAttachment("./data/run.json").json()
]);
const profile = buildProfile(results, benchmarks, run.frameworks);
```

Results from ${html`<a href=${run.resultsUrl} target="_blank" rel="noopener">${run.run}</a>`}. Each benchmark has equal weight, divided among its selected datasets.

```js
const hiddenTags = new Set(["standard", "test", "trace"]);
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
const groupOf = (tag) => workloadTags.has(tag) ? "workload" : "concepts";

const allTags = [...new Set(profile.problems.flatMap((p) => p.tags))]
  .filter((tag) => !hiddenTags.has(tag))
  .sort();

const keepMenu = tagMenu(allTags, {label: "Include tags", groupOf, groupOrder: ["workload", "concepts"]});
const dropMenu = tagMenu(allTags, {label: "Exclude tags", groupOf, groupOrder: ["workload", "concepts"]});

const countEl = document.createElement("span");
countEl.className = "saps-tag-count";
function updateCount() {
  const keep = keepMenu.value;
  const drop = dropMenu.value;
  const kept = profile.problems.filter((p) =>
    (keep.length === 0 || p.tags.some((t) => keep.includes(t))) &&
    !p.tags.some((t) => drop.includes(t))
  ).length;
  countEl.textContent = `${kept} problems`;
}
keepMenu.addEventListener("input", updateCount);
dropMenu.addEventListener("input", updateCount);
updateCount();

const row = document.createElement("div");
row.className = "saps-tag-menu-row";
row.append(keepMenu, dropMenu, countEl);
display(row);

const keep = Generators.input(keepMenu);
const drop = Generators.input(dropMenu);
```

```js
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
```

```js
total === 0 ? html`<p role="status">No problems match these tags.</p>` : Plot.plot({
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
```

At 1×, a framework matches the fastest runtime for a problem. At 2×, it takes at most twice as long. Failed measurements remain in the suite but do not contribute successes. Include tags match any selection; exclude tags take precedence.

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
