import assert from "node:assert/strict";
import {readFileSync} from "node:fs";
import {test} from "node:test";
import {buildProfile} from "../docs/components/profile.js";

const description = (dataset, extra = {}) => ({benchmark: "A", generator: "g", dataset, dense: "true", ...extra});
const result = (dataset, framework, value, extra = {}) => ({
  ...description(dataset), framework, metric: "time", value, ...extra
});

test("ratios are sorted, failures stay in the denominator, and duplicates use their median", () => {
  const profile = buildProfile([
    result("one", "a", "4"), result("one", "a", "8"), result("one", "b", "2"),
    result("two", "a", "1"), result("two", "b", "3")
  ], [description("one"), description("two"), description("failed")]);
  assert.equal(profile.problems.length, 3);
  assert.deepEqual(profile.series, {a: [[1, 1], [0, 3]], b: [[0, 1], [1, 3]]});
  assert.deepEqual(profile.problems[0].tags, ["dense"]);
});

test("invalid values and other metrics cannot produce runtime successes", () => {
  const rows = [null, "", "NaN", "Infinity", "0", "-1", true].map((value) => result("one", "a", value));
  rows.push(result("one", "a", "1", {metric: "memory"}));
  const profile = buildProfile(rows, [description("one")], ["a", "b"]);
  assert.deepEqual(profile.series, {a: [], b: []});
  assert.equal(profile.problems.length, 1);
  assert.equal(profile.xMax, 2);
});

test("an all-failed run retains its frameworks and problems", () => {
  const profile = buildProfile([], [description("one"), description("two")], ["a", "b"]);
  assert.equal(profile.problems.length, 2);
  assert.deepEqual(profile.series, {a: [], b: []});
  assert.equal(profile.xMax, 2);
});

test("dataset identities include generator and preserve numeric-looking names", () => {
  const descriptions = [description("01"), description("1"), description("1", {generator: "other"})];
  const rows = descriptions.map((row) => result(row.dataset, "a", "1", {generator: row.generator}));
  assert.equal(buildProfile(rows, descriptions).series.a.length, 3);
  assert.throws(() => buildProfile(rows, []), /Missing benchmark description/);
});

// Execute the actual weighting cell so the original plot's math stays covered.
const page = readFileSync(new URL("../docs/index.md", import.meta.url), "utf8");
const cell = [...page.matchAll(/```js\n([\s\S]*?)\n```/g)].map((match) => match[1]).find((code) => code.includes("const ok ="));
const curvesFor = new Function("profile", "keep", "drop", `${cell}\nreturn {curves, total};`);

test("the page awaits both CSVs and the run metadata before building the profile", async () => {
  const loadCell = [...page.matchAll(/```js\n([\s\S]*?)\n```/g)][0][1].replace(/^import .*;\n/m, "");
  const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
  const load = new AsyncFunction("FileAttachment", "buildProfile", `${loadCell}\nreturn profile;`);
  const files = {
    "./data/results.csv": [result("one", "a", "1")],
    "./data/benchmarks.csv": [description("one")],
    "./data/run.json": {frameworks: ["a", "failed"]}
  };
  const profile = await load((path) => ({csv: async () => files[path], json: async () => files[path]}), buildProfile);
  assert.deepEqual(profile.series, {a: [[0, 1]], failed: []});
});

test("the plot weights benchmarks equally and recomputes weights after tag filtering", () => {
  const profile = {xMax: 2, problems: [
    {benchmark: "A", tags: ["dense"]}, {benchmark: "A", tags: ["sparse"]},
    {benchmark: "B", tags: ["dense"]}
  ], series: {a: [[0, 1], [2, 2]], failed: []}};
  assert.equal(curvesFor(profile, [], []).curves.filter((point) => point.framework === "a").at(-1).pct, 75);
  assert.equal(curvesFor(profile, ["dense"], []).curves.filter((point) => point.framework === "a").at(-1).pct, 100);
  assert.deepEqual(curvesFor(profile, ["dense"], ["dense"]), {curves: [], total: 0});
  assert.deepEqual(curvesFor(profile, [], []).curves.filter((point) => point.framework === "failed").map((point) => point.pct), [0, 0]);
});
