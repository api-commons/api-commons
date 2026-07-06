---
layout: post
title: "Context Gate: Consumer-Centric API Governance"
date: 2026-07-24
tags:
  - API Commons
  - API Governance
  - Consumer API Governance
  - Agents
  - MCP
image: /assets/images/blog/context-gate-consumer-centric-governance.png
---

Almost every API tool and ruleset governs what a *producer* ships: is your API well-formed, documented, and secure? That leaves the most important question of the agent era unanswered — of everything your APIs can do, what should an agent actually be allowed to consume? So we built [**Context Gate**](https://contextgate.apicommons.org), a browser-first tool that lets you compose and govern exactly the context you expose to agents. No backend, no accounts; it runs in your browser.

[**Try it → contextgate.apicommons.org**](https://contextgate.apicommons.org)

## Compose the Surface on Purpose

You start by sourcing your APIs — search [APIs.io](https://apis.io), fetch from GitHub with your own token, or upload and paste an OpenAPI. Then you make two deliberate choices. First, pick the operations you'll expose; that selection becomes both the **API paths** and the **MCP tools** you offer to agents. Second, control the fields — for each operation, include or exclude individual parameters and request/response schema fields, and flag fields as **PII**. Excluded fields are pruned from the exposed surface, and excluding a parent object cascades to its children. The context you give an agent is something you compose deliberately, not everything your backend happens to expose.

## Three Governed Artifacts

From that selection, Context Gate emits three artifacts that fit together:

| Artifact | What it is |
| --- | --- |
| **Tyk OpenAPI** | A self-contained OAS of only the selected operations and kept fields, with the `x-tyk-api-gateway` extension — upstream, listen path, auth, and per-operation `allow` / `validateRequest` / optional `rateLimit`. |
| **MCP tool manifest** | One tool per exposed operation, its input schema built from the kept parameters and body. Tyk can serve MCP from the generated OpenAPI. |
| **Spectral ruleset** | Governance for the *exposed surface* in tiers — base Tyk OAS validity, extension posture, schema minimization, and the agent-critical checks: PII review, secret-field blocking, no-secrets-in-parameters. |

## Consumer-Centric, and It Doesn't Stand Alone

The rest of the toolchain is producer-centric. Context Gate is **consumer-centric** — it governs the least-privilege slice of your APIs that reaches an agent, and generates the ruleset to keep that slice honest as it changes. It pairs with the [Validator](https://validator.apicommons.org) (lint the generated Tyk OAS against the generated ruleset) and [Agent Rule Export](https://agents.apicommons.org) (hand the rules to the agent). Everything runs client-side; your API descriptions and GitHub token never leave the page.

Context Gate is one of the [API Commons tools](https://apicommons.org/tools/), open and Spectral underneath like the rest — and it is the capstone of this series, the tool that turns governance around to face the consumer. It's where the whole run was always headed.
