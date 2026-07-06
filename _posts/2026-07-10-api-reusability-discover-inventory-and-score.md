---
layout: post
title: "API Reusability: Discover, Inventory, and Score"
date: 2026-07-10
tags:
  - API Commons
  - Reuse
  - Discovery
  - APIs.json
  - API Governance
image: /assets/images/blog/api-reusability-discover-inventory-and-score.png
---

Every organization we talk to has more APIs than anyone can see at once, spread across teams, gateways, and repositories — which is exactly how the same capability gets built three times. The honest question, *how reusable is what we already have?*, goes unanswered because answering it usually means a project. So we built [**API Reusability**](https://reusability.apicommons.org) to make it answerable in a browser tab: discover the evidence, inventory it as a portable index, and score it. Nothing leaves the page, and your keys stay in `localStorage`.

[**Try it → reusability.apicommons.org**](https://reusability.apicommons.org)

## Discover, Then Inventory

API Reusability pulls evidence of APIs from wherever they live: [**APIs.io**](https://apis.io) catalog search with no key, code search across **GitHub / GitLab / Bitbucket** with your own token, and a **HAR upload** that synthesizes an evidence-based OpenAPI from real captured traffic — paths, parameters, headers, response schema. For gateways and wikis a browser can't safely reach — AWS API Gateway, Kong, Tyk, Confluence — a tiny local helper CLI pulls the specs into a bundle you import. Everything is then indexed as OpenAPI into a single **[APIs.json 0.21](https://apis.io)** file: the durable, re-importable reusability index for your org.

## Two Axes, Plus Duplication

Reusability is scored on two axes and a cross-API duplication check, rolled up by **org / team / domain**.

| Axis | Question | Weighted highest |
| --- | --- | --- |
| **A — OpenAPI design** | How reusable is the interface? | schema reuse via `components` + `$ref` |
| **B — APIs.json metadata** | How discoverable & adoptable is it? | linked OpenAPI, docs, license, companion artifacts |
| **Duplication** | Is it already built elsewhere? | repeated paths & near-identical schemas → consolidation |

The composite is `wA·design + wB·metadata + wD·(1 − duplication)`, graded **A–F**. The weights are tunable in **Config → Scoring weights**, and your org's definition of reuse gets published on the **Rubric** tab rather than left undefined — this is *your* score, not ours.

## Before, and After

Two things close the loop. An **intent search** — "what are you trying to build?" — surfaces reuse candidates before a team goes down the rabbit hole and builds from scratch. And a **reuse ledger** records when a team actually adopts an existing API, because the one number every API program struggles to produce is reuse actually happening.

API Reusability is one of the [API Commons tools](https://apicommons.org/tools/), and like the rest it is browser-first, portable, and open — an APIs.json index underneath, so what you build here travels. This is part of a series introducing the tools one at a time.
