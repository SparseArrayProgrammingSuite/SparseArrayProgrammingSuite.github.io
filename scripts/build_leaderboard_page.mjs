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

const scriptMatch = html.match(/<script type="module">([\s\S]*?)<\/script>/);
if (!scriptMatch) throw new Error(`No <script type="module"> found in ${buildHtmlPath}`);
// Observable's build emits paths (imports, registerFile) relative to
// assets/leaderboard/index.html; the Jekyll page lives at /leaderboard/
// instead, so root-absolute the paths under the real build output location.
const script = scriptMatch[1]
  .replace(/(["'])\.\/(_observablehq|_import|_npm|_file)/g, "$1/assets/leaderboard/$2")
  .trim();

const mainMatch = html.match(/<main id="observablehq-main" class="observablehq">([\s\S]*?)<\/main>/);
if (!mainMatch) throw new Error(`No #observablehq-main content found in ${buildHtmlPath}`);
const body = mainMatch[1].trim();

const template = readFileSync(templatePath, "utf8");
const output = template
  .replace("{{OBSERVABLE_BODY}}", () => body)
  .replace("{{OBSERVABLE_SCRIPT}}", () => script);

writeFileSync(outputPath, output);
console.log(`Generated ${path.relative(process.cwd(), outputPath)} from ${path.relative(process.cwd(), buildHtmlPath)}`);
