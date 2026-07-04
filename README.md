# API Commons

The source for **[apicommons.org](https://apicommons.org)** — the home of the open,
machine-readable **building blocks of API operations** and a family of **browser-first
API tools**. Part of the [APIs.io](https://apis.io) network.

API Commons began as a machine-readable artifact for declaring the licensing of your
API, and has grown into a shared library of operational properties — getting started,
authentication, plans, SDKs, road maps, change logs, support, governance rules, and
more. It works in concert with **[APIs.json](https://apisjson.org)** to turn the
human-readable properties of your API operations into machine-readable building blocks
you can use to standardize and automate your API ecosystem at scale. The premise: if we
are going to take things to the next level with APIs and AI, there are aspects of API
operations we need to stop competing on and start sharing.

## This repository

This is the Jekyll site published to **apicommons.org**. It carries both the building
blocks and the index of tools:

- `_common/` — **Common Schema**: shared operational properties every API can adopt.
- `_community/` — **Community Schema**: community-contributed properties.
- `_blueprints/` — reusable API blueprints.
- `_overlays/` — OpenAPI Overlays for applying properties to existing descriptions.
- `_rulesets/` / `rules/` / `rulesets/` — governance rules and rulesets.
- `onboarding/` — agentic API onboarding building blocks.
- `_posts/` — the API Commons blog.
- `_data/`, `_includes/`, `_layouts/`, `assets/`, `images/` — site data and theme.
- `tools/` — the index of the API Commons tool family (below).
- `scripts/` — helpers that generate site data (e.g. rulesets from the API Commons
  rule catalog).

## Building blocks

Each building block is a machine-readable property or artifact that describes one facet
of API operations — licensing, authentication, plans, SDKs, road map, change log,
support, and governance — designed to be referenced from an `apis.json` / `apis.yml`
index so both humans and agents can consume it.

## The tools

Browser-first, backend-free tools for working with the APIs you produce and consume —
everything runs locally in your browser, so your tokens and data never leave it. Each
tool lives at its own subdomain of **apicommons.org**:

| Tool | Where | What it does |
| --- | --- | --- |
| **API Discovery** | [discovery.apicommons.org](https://discovery.apicommons.org) | Search APIs.io and Git hosts for API artifacts and roll them into one APIs.json 0.21 index. |
| **API Documentation** | [documentation.apicommons.org](https://documentation.apicommons.org) | Standalone docs for any APIs.json — OpenAPI as a full reference, Arazzo as step timelines. |
| **API Validator** | [validator.apicommons.org](https://validator.apicommons.org) | Browser-first governance linter for OpenAPI (3.x + Swagger 2.0), AsyncAPI, Arazzo, and JSON Schema, powered by Spectral. |
| **API Governance Graph** | [graph.apicommons.org](https://graph.apicommons.org) | Bind rules, policies, provenance, guidance, experiences, and lifecycle into one navigable graph — walk the Guidance Stack and see where it breaks. |
| **Governance Coverage** | [coverage.apicommons.org](https://coverage.apicommons.org) | Measure how much of your API description your rules actually check — coverage by section, dead rules, and per-rule reach. |
| **Governance Waivers** | [waivers.apicommons.org](https://waivers.apicommons.org) | Sanctioned, owned, expiring governance exceptions — reconcile a waivers file against Spectral output; expired, stale, and expiring waivers surface. |
| **API Certification** | [certification.apicommons.org](https://certification.apicommons.org) | Issue and verify tamper-evident API governance certificates — a SHA-256 fingerprint lets consumers re-verify an API passed a ruleset at a profile. |
| **Agent Rule Export** | [agents.apicommons.org](https://agents.apicommons.org) | Export a ruleset into agent-native artifacts — AGENTS.md block, system prompt, remediation prompt pack, and a compact rule digest. |
| **API Reusability** | [reusability.apicommons.org](https://reusability.apicommons.org) | Score how reusable your organization's APIs really are, by org, team, or domain. |
| **MCP Install** | [install.apicommons.org](https://install.apicommons.org) | A universal install button for MCP servers — one button, every client. |
| **API Governance MCP** | [`@api-common/api-governance-mcp`](https://github.com/api-commons/api-governance-mcp) | The AI surface of the Validator — the same Spectral governance over MCP for any agent. |
| **Spectral Reporter** | [reporter.apicommons.org](https://reporter.apicommons.org) | Turn a Spectral lint run into a self-contained HTML governance report (with SARIF + trends). |
| **Governance Pipeline Auditor** | [auditor.apicommons.org](https://auditor.apicommons.org) | Score a repo's Spectral CI against an 8-point governance maturity rubric. |
| **Governance Pipeline** | [pipeline.apicommons.org](https://pipeline.apicommons.org) | A forkable reference API governance pipeline — PR-gated, SHA-pinned, OWASP security job. |
| **Ruleset Commons** | [rulesets.apicommons.org](https://rulesets.apicommons.org) | A registry of adoptable, provenanced governance rulesets you can `extends`. |
| **Spectral Ruleset Studio** | [studio.apicommons.org](https://studio.apicommons.org) | Turn a prose style guide into an owned, grounded, well-named Spectral ruleset. |
| **Spectral OWASP Ruleset** | [`@api-common/spectral-owasp-ruleset`](https://www.npmjs.com/package/@api-common/spectral-owasp-ruleset) | A grounded Spectral ruleset for the OWASP API Security Top 10. |

See the full, current list at [apicommons.org/tools](https://apicommons.org/tools/).

## Links

- [apicommons.org](https://apicommons.org) — this site
- [apis.io](https://apis.io) — the API discovery network API Commons is part of
- [apisjson.org](https://apisjson.org) — the APIs.json discovery format
- Questions or contributions — [open an issue](https://github.com/api-commons/api-commons/issues)

---

A project of [API Evangelist](https://apievangelist.com), maintained openly under
API Commons. The building blocks and tools are open and free to use; API Evangelist
offers expert API governance and strategy services around them.
