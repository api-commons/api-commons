---
layout: post
title: "Governance Pipeline: A PR-Gating Blueprint"
date: 2026-07-15
tags:
  - API Commons
  - Spectral
  - API Governance
  - CI/CD
  - Pipeline
image: /assets/images/blog/governance-pipeline-a-pr-gating-blueprint.png
---

Most teams that put API governance into CI/CD assemble it from whatever fragment they find first — and the fragment they find first is usually the wrong one. We know this because [API Evangelist read 1,005 real public GitHub pipelines](https://apievangelist.com) running [Spectral](https://github.com/stoplightio/spectral) and scored each against an eight-point maturity rubric. The ceiling was six; two repositories reached it. Nobody had the whole blueprint — even though every piece of it already ships somewhere in the corpus. So we bolted the pieces together into one artifact you fork.

[**Try it → pipeline.apicommons.org**](https://pipeline.apicommons.org)

## Eight Decisions, Each Fixing a Finding

Governance Pipeline is a **teaching artifact you fork**: a starter GitHub Actions workflow, a one-step composite action, and an owned starter ruleset. Every decision in it maps to something the research found broken and a real team that proved the fix.

| Decision | Finding it fixes |
| --- | --- |
| Gate on **`pull_request`** (+ push baseline) | A third of pipelines lint *after* the merge they meant to prevent |
| **`paths:`** filter to spec + ruleset | Only 22% run only when the spec actually changed |
| Spectral **pinned by commit SHA** | Of 215 Action users, just 14 pin by commit |
| An **owned, grounded ruleset** | 63% run the tool's defaults — governing with nothing |
| A **separate OWASP security job** | Security rules appear in only 14% of pipelines |
| A **human-readable report** | Readable reports ~7%, SARIF ~3% |

Nobody in 1,005 pipelines had all of these at once. This repo does.

## The Ruleset Is the Point

The headline finding was that **63% run Spectral with no ruleset of their own** — the most common way to use a governance tool is to not govern with it. So the starter ruleset is the counter-example: roughly a dozen rules, each written on purpose, each with a prose `description` and a `documentationUrl`, severity-tuned, and **exactly three set to block** (an owner, a machine-addressable operationId, a defined auth scheme). The blocking set's credibility comes from being short.

You are told not to adopt it unread. Copy the `ruleset/` directory, rewrite the rules against your own operations, point the docs links at your handbook. The identical YAML is a governance artifact in one repo and an empty gesture in another; the difference is whether human work exists behind it. It lints OpenAPI 3.x and Swagger 2.0, and the pipeline runs [**Spectral Reporter**](https://reporter.apicommons.org) after the lint to emit a self-contained HTML governance report — a scoreboard with a trajectory instead of a wall of red.

Governance Pipeline is one of the [API Commons tools](https://apicommons.org/tools/), open and Apache-2.0 and Spectral underneath, and it continues the series introducing the tools one at a time.
