#!/usr/bin/env node
// Regenerates _pages/leaderboard.md from the Observable Framework build
// output (assets/leaderboard/index.html, built from docs/index.md by
// `observable build`). This keeps the Jekyll-hosted leaderboard page in
// sync with the Observable source automatically, instead of requiring a
// hand-maintained copy of the generated script/markup.
import {readFileSync, writeFileSync} from "node:fs";
import {fileURLToPath} from "node:url";
import path from "node:path";

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const buildHtmlPath = path.join(root, "assets", "leaderboard", "index.html");
const templatePath = path.join(root, "scripts", "leaderboard.template.md");
const outputPath = path.join(root, "_pages", "leaderboard.md");

const html = readFileSync(buildHtmlPath, "utf8");

function extract(re, what) {
  const match = html.match(re);
  if (!match) throw new Error(`No ${what} found in ${buildHtmlPath}`);
  return match[1];
}

// Observable's build emits paths (imports, registerFile) relative to
// assets/leaderboard/index.html; the Jekyll page lives at /leaderboard/
// instead, so root-absolute the paths under the real build output location.
const script = extract(/<script type="module">([\s\S]*?)<\/script>/, "<script type=\"module\">")
  .replace(/(["'])\.\/(_observablehq|_import|_npm|_file)/g, "$1/assets/leaderboard/$2")
  .trim();

const body = extract(/<main id="observablehq-main" class="observablehq">([\s\S]*?)<\/main>/, "#observablehq-main content")
  .trim();

const template = readFileSync(templatePath, "utf8");
const output = template
  .replace("{{OBSERVABLE_BODY}}", () => body)
  .replace("{{OBSERVABLE_SCRIPT}}", () => script);

writeFileSync(outputPath, output);
console.log(`Generated ${path.relative(process.cwd(), outputPath)} from ${path.relative(process.cwd(), buildHtmlPath)}`);
