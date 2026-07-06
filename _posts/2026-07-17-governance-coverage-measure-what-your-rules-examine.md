---
layout: post
title: "Governance Coverage: Measure What Your Rules Examine"
date: 2026-07-17
tags:
  - API Commons
  - Spectral
  - API Governance
  - Coverage
image: /assets/images/blog/governance-coverage-measure-what-your-rules-examine.png
---

A clean governance run tells you your rules found nothing to complain about. It does not tell you whether your rules ever looked. Those are very different claims, and the difference is where blind spots live. So we built [**Governance Coverage**](https://coverage.apicommons.org) — a browser-first tool that measures how much of your API description your governance actually examines.

[**Try it → coverage.apicommons.org**](https://coverage.apicommons.org)

## Test Coverage, One Altitude Up

Test coverage asks how much of your code your tests execute. Governance coverage asks the same question of your API description. Point the tool at an OpenAPI, AsyncAPI, or Arazzo document and a ruleset, and it resolves every rule's JSONPath against the document. Of all the addressable locations — every operation, parameter, response, schema, and property — how many does *any* rule actually inspect? A section at 0% is a blind spot. A rule that matches nothing is dead weight for *this* API. [Spectral](https://github.com/stoplightio/spectral) givens are resolved client-side with [`jsonpath-plus`](https://github.com/JSONPath-Plus/JSONPath), format-gated so an `oas2` rule is never counted against a 3.x document.

## What It Reports

| Signal | What it tells you |
| --- | --- |
| **Coverage** | Share of governable nodes reached by at least one rule, plus **depth** — average rules per covered node |
| **By section** | Coverage % and depth per structural kind; a fully-covered section leaning on one rule is flagged **thin** |
| **Dead rules for this API** | Active rules whose `given` matches nothing — often the more actionable list |
| **Per-rule reach** | How many nodes each rule touches, so you can spot over-broad rules |

Coverage measures **reach, not quality**: a node touched by one broad rule is "covered" but barely governed, which is why depth rides alongside every number. Click into any section to see its individual nodes and which ones are blind.

## Bring Your Own Ruleset

The bundled **API Commons catalog** — the 769-rule set from [API Validator](https://github.com/api-commons/api-validator) — is auto-selected by the document's format and makes a fine starting read, though against a catalog that broad most node types get touched, so the sharper signals become depth and dead rules. The moment this tool earns its place is when you paste in *your own* Spectral ruleset and measure *your* governance against *your* API. That is when the real blind spots appear. Everything runs in your browser; the description and ruleset you paste never leave the page.

Governance Coverage is one of the [API Commons tools](https://apicommons.org/tools/), open and portable and Spectral underneath, and part of a series introducing the tools one at a time — because knowing whether your rules are any good starts with knowing whether they are even looking.
