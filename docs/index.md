---
title: Performance profile
---

```js
import {buildProfile} from "./components/profile.js";
const results = FileAttachment("./data/results.csv").csv();
const benchmarks = FileAttachment("./data/benchmarks.csv").csv();
const run = FileAttachment("./data/run.json").json();
const profile = buildProfile(results, benchmarks, run.frameworks);
```

Results from ${html`<a href=${run.resultsUrl} target="_blank" rel="noopener">${run.run}</a>`}. Each benchmark has equal weight, divided among its selected datasets.

```js
const allTags = [...new Set(profile.problems.flatMap((p) => p.tags))].sort();
const keep = view(Inputs.checkbox(allTags, {label: "Include tags"}));
const drop = view(Inputs.checkbox(allTags, {label: "Exclude tags"}));
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
```

At 1×, a framework matches the fastest runtime for a problem. At 2×, it takes at most twice as long. Failed measurements remain in the suite but do not contribute successes. Include tags match any selection; exclude tags take precedence.
