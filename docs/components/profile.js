// Adapt the two CSV tables to the original performance plot's input format.
export function buildProfile(results, benchmarks, frameworkNames = results.map((row) => row.framework)) {
  const key = (row) => JSON.stringify([row.benchmark, row.generator, row.dataset]);
  const timeResults = results.filter((row) => row.metric === "time");
  const problems = benchmarks.map((row) => ({
    benchmark: row.benchmark,
    generator: row.generator,
    dataset: row.dataset,
    tags: Object.keys(row).filter((column) =>
      !["benchmark", "generator", "dataset"].includes(column) &&
      (row[column] === true || row[column] === "true")
    )
  }));
  const indices = new Map(problems.map((problem, i) => [key(problem), i]));
  const values = problems.map(() => new Map());
  const frameworks = [...new Set(frameworkNames)].sort();
  const series = Object.fromEntries(frameworks.map((framework) => [framework, []]));
  for (const row of timeResults) {
    const i = indices.get(key(row));
    if (i === undefined) throw new Error(`Missing benchmark description for ${key(row)}`);
    const value = typeof row.value === "number" || typeof row.value === "string" ? Number(row.value) : NaN;
    if (!Number.isFinite(value) || value <= 0) continue;
    const samples = values[i].get(row.framework) ?? [];
    samples.push(value);
    values[i].set(row.framework, samples);
  }
  let xMax = 2;
  values.forEach((byFramework, i) => {
    const runtimes = [...byFramework].map(([framework, samples]) => [framework, median(samples)]);
    const best = Math.min(...runtimes.map(([, value]) => value));
    for (const [framework, value] of runtimes) {
      const ratio = value / best;
      if (!Number.isFinite(ratio)) throw new Error("Nonfinite runtime ratio");
      series[framework].push([i, ratio]);
      xMax = Math.max(xMax, ratio);
    }
  });
  for (const points of Object.values(series)) points.sort((a, b) => a[1] - b[1]);
  return {problems, series, xMax};
}

function median(values) {
  values.sort((a, b) => a - b);
  const i = Math.floor(values.length / 2);
  return values.length % 2 ? values[i] : values[i - 1] / 2 + values[i] / 2;
}
