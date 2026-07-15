---
layout: post
title: "The API Commons Tools Are Now an API"
date: 2026-07-26
tags:
  - API Commons
  - API Governance
  - Spectral
  - Discovery
  - Agents
  - MCP
image: /assets/images/blog/the-api-commons-tools-are-now-an-api.png
---

Every [API Commons tool](https://apicommons.org/tools/) is browser-first on purpose. No backend, no accounts, no upload — your spec and your tokens never leave the page. That is the right shape for a person with a document and a question. It is the wrong shape for a pipeline: CI cannot click a button, and an agent cannot open a tab. So the same engines now also run as a hosted API.

[**Docs → developer.apievangelist.com/governance/index**](https://developer.apievangelist.com/governance/index)

## The Same Engine, Not a Reimplementation

Twenty-three endpoints sit at `api.apievangelist.com/v1/governance/*` and `/v1/discovery/*`, and none of them is a second implementation. The logic is lifted from each tool's own source: the [Spectral](https://github.com/stoplightio/spectral) engine and the curated rule catalog out of the [API Validator](https://validator.apicommons.org) — 574 rules across OpenAPI, AsyncAPI, Arazzo, and JSON Schema — plus the reach analysis out of [Governance Coverage](https://coverage.apicommons.org), the reconciler out of [Governance Waivers](https://waivers.apicommons.org), the fingerprinting out of [API Certification](https://certification.apicommons.org), the duplication scoring out of [API Reusability](https://reusability.apicommons.org), and the emitters out of [Toolsmith](https://toolsmith.apicommons.org) and [Context Gate](https://contextgate.apicommons.org).

The browser tools stay the source of truth. The API vendors their modules at build time and bundles them — Spectral, the rule catalog, and all of it — into one function. Fix a rule in the tool and the endpoint runs the fixed rule. There is no second copy to drift. `GET /governance/rules` will hand you the whole catalog if you want to read it.

## Checking Is Free. Keyless.

Twelve endpoints need no key at all — `validate`, `coverage`, `waivers`, `report`, `verify`, `classify`, `diff`, `scorecard`, `deprecation`, `rules`, `rulesets`, and `onboarding`:

```bash
curl -X POST https://api.apievangelist.com/v1/governance/validate \
  -H "content-type: application/json" \
  -d '{"document":"openapi: 3.0.0\ninfo:\n  title: Widget API\n  version: 1.0.0\npaths: {}"}'
```

That runs the full curated ruleset and hands back the findings. Nothing to sign up for.

## Generating Is Paid

Eleven are Pro — `certify`, `agent-export`, `pipeline-audit`, `toolsmith`, `context-gate`, `overlay`, `mock`, `snippets`, `reusability`, `experience`, and `agent-descriptor`. The line is capability, not volume: **if it checks an API you already have, it is free; if it produces an artifact you keep, certifies something, audits a repository, or rolls up across an estate, it is Pro.** A keyless caller hitting a Pro endpoint gets a clean `402` and an upgrade link, never a silent truncation.

## Some of This Had No Tool

Standing the API up made the gaps obvious — things we have argued for repeatedly and never shipped anything for. Those became endpoints too:

| Endpoint | What it does |
| --- | --- |
| **`diff`** | Breaking-change detection between two OpenAPI versions. |
| **`classify`** | Inventories the PII and secret fields a spec exposes. |
| **`scorecard`** | A composite maturity score across design, coverage, docs, and agent-readiness. |
| **`deprecation`** | Which deprecated operations actually announce a sunset — and which go quiet. |
| **`overlay`** | Applies an [OpenAPI Overlay](https://spec.openapis.org/overlay/v1.0.0.html) and reports what each action matched. |
| **`mock`** / **`snippets`** | Example payloads, and runnable curl / JavaScript / Python per operation. |
| **`agent-descriptor`** | Generates an API's `llms.txt` and an `AGENTS.md` consumption contract. |

The first one it ran in anger caught a real drift in one of our own published onboarding descriptors. That is the point.

## Why Bother

Governance that only runs in a browser only runs when someone remembers to open it. The pipeline is where it has to gate, and the conversation is where agents now ask. Same rules, same engine, three surfaces: the tool, the [MCP server](https://apicommons.org/2026/07/06/an-mcp-server-for-api-governance/), and now the API.

Browser-first is not going anywhere. It just stopped being the only way in.
