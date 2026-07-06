---
layout: post
title: "Governance Pipeline Auditor: Score Your CI Setup"
date: 2026-07-16
tags:
  - API Commons
  - Spectral
  - API Governance
  - CI/CD
  - Pipeline
image: /assets/images/blog/governance-pipeline-auditor-score-your-ci-setup.png
---

Plenty of tooling will tell you whether your API description is any good. Almost nothing tells you whether the pipeline that is supposed to be checking it is any good. So we built the [**Governance Pipeline Auditor**](https://auditor.apicommons.org) — it scans a repository's [Spectral](https://github.com/stoplightio/spectral) CI setup, scores it against an eight-point maturity rubric, and hands back a prioritized punch-list of concrete fixes, each with a one-line *why* and a docs link. Lint your linting.

[**Try it → auditor.apicommons.org**](https://auditor.apicommons.org)

## The Rubric Comes From Real Pipelines

The eight signals are lifted straight from the API Evangelist paper *"The State of Spectral in API Pipelines,"* a census of **1,005 real public pipelines** where the maturity ceiling was 6/8 and nobody reached 7 or 8. It measures only the **mechanical** surface a workflow file exposes — the automatable quarter of governance. It says nothing about whether a human wrote the rules on purpose, which is the three-quarters no file census can see. But the mechanical quarter is where almost everyone is leaking, and it is the cheapest to fix.

| Signal | Question it answers |
| --- | --- |
| Gates the PR | Does governance fire before the merge, not after? |
| Custom ruleset | Are the rules the organization's, not the tool's defaults? |
| Owned ruleset home | Do the rules live in a dedicated dir, not a remote source? |
| Pinned tooling | Is the enforcing tool pinned to a chosen version? |
| Security layer | Are OWASP/security rules present, not just style? |
| Real gate | Does it fail the build on error, not just annotate? |
| Path-filtered | Does it run only when the spec/ruleset changes? |
| Machine-readable report | Does it emit SARIF / a readable report / PR comment? |

Bands run from `0–1` Nominal through `2–3` Thin, `4–5` Developing, `6–7` Strong, up to `8` Blueprint. The auditor also flags the paper's named anti-patterns: the default ruleset, `@latest` and floating pins, linting after the merge, toothless `continue-on-error`, and rules with no `documentationUrl`.

## One Scorer, Three Surfaces

The scoring logic is a single pure, dependency-free function, imported verbatim by the browser demo, the CLI, and the GitHub Action — so the score you see when you paste a workflow into the site is byte-for-byte what CI produces. Run it now with no install: `npx @api-common/governance-pipeline-auditor .` prints the score, per-signal PASS/FAIL with evidence, and the punch-list. Add `--min-score 5` to gate a pipeline on its own maturity, `--html` to write a self-contained report, or drop the composite `api-commons/governance-pipeline-auditor@v1` action into a job to get the score in the step summary and a hard gate. It is the sequel to [Spectral Reporter](https://reporter.apicommons.org): that one reports on your API, this one reports on your pipeline.

The Governance Pipeline Auditor is one of the [API Commons tools](https://apicommons.org/tools/) — free and open under Apache-2.0, and part of a series introducing the tools one at a time. Point it at your own repository; every failing signal it finds is a specific, boring, one-afternoon fix.
