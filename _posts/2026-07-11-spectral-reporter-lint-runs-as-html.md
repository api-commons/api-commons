---
layout: post
title: "Spectral Reporter: Lint Runs as Self-Contained HTML"
date: 2026-07-11
tags:
  - API Commons
  - Spectral
  - API Governance
  - Reporting
image: /assets/images/blog/spectral-reporter-lint-runs-as-html.png
---

Spectral produces excellent governance findings and terrible reading material. Its native output is a JSON array or a scroll of terminal lines that disappear the moment the CI job finishes — which means the people who most need the result never see it. So we built [**Spectral Reporter**](https://reporter.apicommons.org): a post-processor that turns a Spectral lint run into one self-contained HTML file, inline CSS and JS, no external or CDN requests, ready to open offline or attach to a build.

[**Try it → reporter.apicommons.org**](https://reporter.apicommons.org)

## What's in the Report

You feed it Spectral's `--format json` output and it renders a governance artifact a non-author can read. A pass/fail banner fails if there are any errors. Severity stat tiles count errors, warnings, info, and hints with reserved, always-labelled status colors — never color alone. Per-issue rows carry a severity chip, the rule code, the message, the file basename, and the exact `line:character`; expand a row for the JSON `path` and source. A group-by toggle regroups by rule, file, or severity, search and severity chips filter the whole report client-side, and top-offending rule and file rankings tell you where to start. It is responsive, respects `prefers-reduced-motion`, and does light and dark. The design lineage is [newman-reporter-htmlextra](https://github.com/DannyDainton/newman-reporter-htmlextra), which did the same for Postman/Newman runs.

## Run It With No Install

```bash
# From a Spectral JSON results file
npx @api-common/spectral-reporter spectral-results.json -o governance-report.html

# Or pipe straight from Spectral
spectral lint -f json openapi.yaml | npx @api-common/spectral-reporter -o report.html
```

Drop the output into an `actions/upload-artifact` step and every build leaves behind a report a human can open. Beyond the HTML, a few flags extend it:

| Flag | What it does |
| --- | --- |
| `--sarif <file>` | Also write **SARIF 2.1.0** for GitHub code scanning |
| `--history <dir>` | Render a **trend report** across dated runs — improved vs. regressed rules |
| `--totals <file>` | Add a **compliance scoreboard** — "82% comply," not just violations |

The SARIF path matters: our pipelines research found only **3.4%** of API teams surface governance findings in GitHub code scanning, and this closes that gap in one flag. The totals sidecar and trend modes both degrade gracefully — omit them and you get the deficit-only report exactly as before.

Spectral Reporter is one of the [API Commons tools](https://apicommons.org/tools/), Apache-2.0 and published to npm as `@api-common/spectral-reporter`, with the report renderer shared byte-for-byte between the CLI and the web demo. It is another entry in our series introducing the tools one at a time.
