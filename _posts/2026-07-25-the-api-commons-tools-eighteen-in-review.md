---
layout: post
title: "The API Commons Tools: Eighteen in Review"
date: 2026-07-25
tags:
  - API Commons
  - API Governance
  - Spectral
  - Discovery
  - Tools
  - Agents
image: /assets/images/blog/the-api-commons-tools-eighteen-in-review.png
---

Over the last eighteen days we introduced one [API Commons tool](https://apicommons.org/tools/) per day. This post gathers the whole run in one place. None of these tools is a platform you adopt — each is a small, open, single-purpose thing you can pick up on its own — but read together they form a complete governance and discovery stack that is [Spectral](https://github.com/stoplightio/spectral) underneath and portable all the way through.

## The Full Run

- **[API Validator](https://apicommons.org/2026/07/07/api-validator-governance-in-the-browser/)** — lint OpenAPI, AsyncAPI, Arazzo, and JSON Schema in the browser.
- **[API Discovery](https://apicommons.org/2026/07/08/api-discovery-a-registry-in-your-browser/)** — a browser-first registry for API artifacts.
- **[API Documentation](https://apicommons.org/2026/07/09/api-documentation-from-apis-json/)** — standalone docs from APIs.json, with OpenAPI and Arazzo.
- **[API Reusability](https://apicommons.org/2026/07/10/api-reusability-discover-inventory-and-score/)** — discover, inventory, and score API reusability.
- **[Spectral Reporter](https://apicommons.org/2026/07/11/spectral-reporter-lint-runs-as-html/)** — Spectral runs as self-contained HTML reports.
- **[Spectral Ruleset Studio](https://apicommons.org/2026/07/12/spectral-ruleset-studio-style-guides-into-rulesets/)** — turn prose style guides into grounded rulesets.
- **[Ruleset Commons](https://apicommons.org/2026/07/13/ruleset-commons-rulesets-by-region-and-industry/)** — a registry of provenanced rulesets by region and industry.
- **[Spectral OWASP Ruleset](https://apicommons.org/2026/07/14/spectral-owasp-ruleset-api-security-top-10-as-rules/)** — the OWASP API Security Top 10 as grounded rules.
- **[Governance Pipeline](https://apicommons.org/2026/07/15/governance-pipeline-a-pr-gating-blueprint/)** — a reference PR-gating pipeline blueprint.
- **[Governance Pipeline Auditor](https://apicommons.org/2026/07/16/governance-pipeline-auditor-score-your-ci-setup/)** — score your Spectral CI setup against a maturity rubric.
- **[Governance Coverage](https://apicommons.org/2026/07/17/governance-coverage-measure-what-your-rules-examine/)** — measure how much of an API your rules actually examine.
- **[Governance Waivers](https://apicommons.org/2026/07/18/governance-waivers-exceptions-with-owners-and-expiry/)** — sanctioned, owned, expiring exceptions.
- **[API Governance Graph](https://apicommons.org/2026/07/19/api-governance-graph-rules-policies-and-provenance/)** — bind the building blocks into one navigable graph.
- **[API Certification](https://apicommons.org/2026/07/20/api-certification-verifiable-trust-stamps/)** — issue and verify tamper-evident governance certificates.
- **[API Governance MCP](https://apicommons.org/2026/07/06/an-mcp-server-for-api-governance/)** — the same ruleset as an MCP server an agent can call.
- **[Agent Rule Export](https://apicommons.org/2026/07/22/agent-rule-export-rulesets-as-agent-native-guidance/)** — turn a ruleset into agent-native guidance.
- **[MCP Install](https://apicommons.org/2026/07/02/a-universal-install-button-for-mcp-servers/)** — a universal install interface for MCP servers.
- **[Context Gate](https://apicommons.org/2026/07/24/context-gate-consumer-centric-governance/)** — govern what agents are allowed to consume.

## One Idea, Many Surfaces

The arc runs from the everyday acts of checking and finding an API, through the machinery of writing, running, and measuring governance, and out to the newest frontier: governing what agents produce and what they are allowed to consume. What holds it together is that a `spectral-` ruleset is the portable artifact every tool shares — the rules are the product, and each tool is just another surface for the same rules.

Everything is open and Apache-2.0, most of it runs entirely in your browser, and all of it lives on the [API Commons tools](https://apicommons.org/tools/) page alongside whatever we ship next. Thanks for reading along, one day at a time.
