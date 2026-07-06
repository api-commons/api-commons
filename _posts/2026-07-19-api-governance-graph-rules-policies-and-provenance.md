---
layout: post
title: "API Governance Graph: Rules, Policies, and Provenance"
date: 2026-07-19
tags:
  - API Commons
  - API Governance
  - Graph
  - Building Blocks
image: /assets/images/blog/api-governance-graph-rules-policies-and-provenance.png
---

Governance is not a list of rules — it is a stack. A machine rule enforces a written policy, which is explained by a piece of guidance, protects a consumer experience, carries a provenance, and applies at a point in the API lifecycle. When those links exist, governance is legible; when they break, it is just noise. So we built [**API Governance Graph**](https://graph.apicommons.org) to bind all six building blocks into one navigable graph — and make the breaks impossible to miss.

[**Try it → graph.apicommons.org**](https://graph.apicommons.org)

## Three Views of One Stack

The tool renders the same governance stack three ways, all client-side with no backend and no account:

| View | What it shows |
| --- | --- |
| **Stack** | Every node in six columns — Guidance, Policy, Rule, Provenance, Experience, Lifecycle. Click any node to light up everything bound to it and open a detail rail you can keep walking from. |
| **Gaps** | The loose ends, scored per layer: rules no policy enforces, rules tied to no experience, policies with no stated *why*, policies enforcing rules absent from the executable catalog, and guidance nothing points at. |
| **By experience** | The whole stack rolled up by the `experience:` axis — the one that answers *what does turning a rule on actually buy the consumer.* |

Stack makes governance legible. Gaps is the view that turns "we have governance" into "here is where it is thin."

## An Explicit Join Spine, Not Fuzzy Matching

The graph is assembled at build time from two sources we already maintain and shipped as a single static snapshot (`graph-bundle.json`), so the app has no runtime dependencies and makes no network calls. It draws on the [**API Commons rule catalog**](https://github.com/api-commons/api-validator) — the full 769-rule, twelve-format ruleset with each rule's tags, `source` provenance, and `given`/`then` — and the [**apievangelist.com** building blocks](https://apievangelist.com): the policies, guidance, experiences, lifecycle, properties, and strategies collections, joined by their published cross-link arrays.

The join is declared, not guessed. A policy names the rule slugs it enforces, points at the guidance that explains it, and lists the experiences it improves; a rule carries its own `experience:` tags and its `source` lineage. The graph simply renders what is already true in the data — which is why the Gaps view can be trusted to name real holes rather than artifacts of a matcher.

API Governance Graph is one of the [API Commons tools](https://apicommons.org/tools/), and like the rest it is open, portable, and static under the hood — free to fork, with expert governance services available when you want the stack mapped for a real organization. This is part of a series introducing the tools one at a time.
