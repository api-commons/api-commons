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

> **`scripts/generate-spotlight.py` needs a sibling checkout.** It reads the Spotlight
> rule catalog from `../spotlight-validator/rules/all-rules.yaml` — a **private** repo
> that is not vendored here. `_data/spotlight_rules.json`, `assets/rulesets/*` and the
> `/rules/` and `/rulesets/` pages are all **generated** from it, so never hand-edit
> them; the next run overwrites your change. Clone it alongside this repo before
> regenerating:
>
> ```
> git clone https://github.com/api-commons/spotlight-validator.git ../spotlight-validator
> ```

## Building blocks

Each building block is a machine-readable property or artifact that describes one facet
of API operations — designed to be referenced from an `apis.json` / `apis.yml` index so
both humans and agents can consume it. Each lives in its own repo under
[github.com/api-commons](https://github.com/api-commons).

- [**policies**](https://github.com/api-commons/policies) — the business rules behind API governance.
- [**rules**](https://github.com/api-commons/rules) — Spectral rulesets across many artifact types.
- [**guidance**](https://github.com/api-commons/guidance) — the how-to layer that turns governance rules into help.
- [**lifecycle**](https://github.com/api-commons/lifecycle) — the stages every API moves through.
- [**teams**](https://github.com/api-commons/teams) — the people layer of API operations.
- [**experiences**](https://github.com/api-commons/experiences) — the developer experiences an API program offers.
- [**use-cases**](https://github.com/api-commons/use-cases) — the use cases an API serves.
- [**vocabulary**](https://github.com/api-commons/vocabulary) — shared words and definitions for API operations.
- [**plans**](https://github.com/api-commons/plans) — access plans, tiers, and pricing.
- [**rate-limits**](https://github.com/api-commons/rate-limits) — the quotas an API enforces, machine-readably.
- [**versioning**](https://github.com/api-commons/versioning) — how an API is versioned, and which versions are reachable.
- [**features**](https://github.com/api-commons/features) — what an API can do, tied to the operations behind each claim.
- [**benefits**](https://github.com/api-commons/benefits) — the outcomes an API claims, with the measure and the evidence.
- [**integrations**](https://github.com/api-commons/integrations) — the connector catalog, resolvable to the providers on the other end.
- [**change-log**](https://github.com/api-commons/change-log) — publish an API's changelog, machine-readably.
- [**road-map**](https://github.com/api-commons/road-map) — publish an API's roadmap, machine-readably.
- [**interface-license**](https://github.com/api-commons/interface-license) — apply an open license to your API's interface (its surface, not its implementation).

## Specs, templates & examples

- [**api-onboarding**](https://github.com/api-commons/api-onboarding) — the API Onboarding Descriptor (AID), a `/.well-known/api-onboarding` document describing what it takes to onboard with an API.
- [**api-authorization**](https://github.com/api-commons/api-authorization) — a jurisdiction-neutral, two-tier, machine-checkable profile for securing APIs with OAuth 2.1 and FAPI 2.0.
- [**problem-details-for-http-apis**](https://github.com/api-commons/problem-details-for-http-apis) — a base for using RFC 9457 Problem Details in your API, with a [Spectral ruleset](https://github.com/api-commons/spectral-problem-details-ruleset) that checks conformance.
- [**json-api**](https://github.com/api-commons/json-api) — schemas and governance for the JSON:API standard.
- [**train-travel**](https://github.com/api-commons/train-travel) — an OpenAPI + APIs.json template for a Train Travel API, handy for demos and testing.
- [**accounts**](https://github.com/api-commons/accounts) — a base Accounts API: the account lifecycle every service reinvents, described once.
- [**images**](https://github.com/api-commons/images) — a base Images API: upload, metadata, renditions, and deletion.
- [**videos**](https://github.com/api-commons/videos) — a base Videos API: upload, transcoding, playback renditions, and captions.
- [**examples**](https://github.com/api-commons/examples) — shared examples for the building blocks and the APIs.json ecosystem.
- [**snacks-twilio-messages**](https://github.com/api-commons/snacks-twilio-messages) — an API Snack for AI: send a message with Twilio.

## The tools

Browser-first, backend-free tools for working with the APIs you produce and consume —
everything runs locally in your browser, so your tokens and data never leave it. Each
tool lives at its own subdomain of **apicommons.org**:

| Tool | Where | What it does |
| --- | --- | --- |
| **Agent Rule Export** | [agents.apicommons.org](https://agents.apicommons.org) | Export a ruleset into agent-native artifacts — AGENTS.md block, system prompt, remediation prompt pack, and a compact rule digest. |
| **API Discovery** | [discovery.apicommons.org](https://discovery.apicommons.org) | Search APIs.io and Git hosts for API artifacts and roll them into one APIs.json 0.21 index. |
| **API Documentation** | [documentation.apicommons.org](https://documentation.apicommons.org) | Standalone docs for any APIs.json — OpenAPI as a full reference, Arazzo as step timelines. |
| **API Experience** | [experience.apicommons.org](https://experience.apicommons.org) | A DX/AX layer for any APIs.json — trace each REST operation to its MCP tool and Agent Skill, with a free/paid coverage scorecard. |
| **API Governance Graph** | [graph.apicommons.org](https://graph.apicommons.org) | Bind rules, policies, provenance, guidance, experiences, and lifecycle into one navigable graph, with a Gaps view. |
| **API Governance MCP** | [github.com/api-commons/api-governance-mcp](https://github.com/api-commons/api-governance-mcp) | The AI surface of the Validator — the same Spectral governance over MCP for any agent. |
| **API Reusability** | [reusability.apicommons.org](https://reusability.apicommons.org) | Score how reusable your organization's APIs really are, by org, team, or domain. |
| **API Validator** | [validator.apicommons.org](https://validator.apicommons.org) | Browser-first governance linter for OpenAPI (3.x + Swagger 2.0), AsyncAPI, Arazzo, and JSON Schema, powered by Spectral. |
| **Code-First Governance** | [codefirst.apicommons.org](https://codefirst.apicommons.org) | Govern generated specs — fingerprint the OpenAPI generator, separate findings you must fix in code from spec-authoring ones, and map each to the annotation that fixes it. |
| **Context Gate** | [contextgate.apicommons.org](https://contextgate.apicommons.org) | Choose which API operations and fields you expose to agents; emit a governed Tyk API + MCP surface and a Spectral ruleset for it (PII, secrets, compliance). |
| **Governance Baseline** | [baseline.apicommons.org](https://baseline.apicommons.org) | Adopt governance on a legacy estate — snapshot today's violations, then fail only NEW ones while you burn the baseline down. |
| **Governance Certification** | [certification.apicommons.org](https://certification.apicommons.org) | Issue and verify tamper-evident governance certificates — a SHA-256 fingerprint lets consumers re-verify an API passed a ruleset at a profile. |
| **Governance Coverage** | [coverage.apicommons.org](https://coverage.apicommons.org) | Measure how much of your API description your rules actually check — coverage by section, dead rules, and per-rule reach. |
| **Governance Pipeline** | [github.com/api-commons/governance-pipeline](https://github.com/api-commons/governance-pipeline) | A forkable reference API governance pipeline — PR-gated, SHA-pinned, OWASP security job. |
| **Governance Pipeline Auditor** | [auditor.apicommons.org](https://auditor.apicommons.org) | Score a repo's Spectral CI against an 8-point governance maturity rubric. |
| **Governance Scorecard** | [scorecard.apicommons.org](https://scorecard.apicommons.org) | The longitudinal view — ingest Spectral snapshots over time and score governance health per spec (0–100), with trends. |
| **Governance Waivers** | [waivers.apicommons.org](https://waivers.apicommons.org) | Sanctioned, owned, expiring governance exceptions — reconcile a waivers file against Spectral output; expired, stale, and expiring waivers surface. |
| **MCP Install** | [install.apicommons.org](https://install.apicommons.org) | A universal install button for MCP servers — one button, every client. |
| **Model Library** | [library.apicommons.org](https://library.apicommons.org) | A versioned, reusable model/component library — see which specs consume each model and classify a version bump as breaking or not across every consumer. |
| **Ruleset Commons** | [rulesets.apicommons.org](https://rulesets.apicommons.org) | A registry of adoptable, provenanced governance rulesets you can `extends`. |
| **Spec Review** | [review.apicommons.org](https://review.apicommons.org) | A ref-resolving design-diff for OpenAPI/AsyncAPI/Arazzo — resolve `$ref`, flag breaking changes, and get a copyable Markdown summary for the PR. |
| **Spectral OWASP Ruleset** | [github.com/api-commons/spectral-owasp-ruleset](https://github.com/api-commons/spectral-owasp-ruleset) | A grounded Spectral ruleset for the OWASP API Security Top 10. |
| **Spectral Problem Details Ruleset** | [github.com/api-commons/spectral-problem-details-ruleset](https://github.com/api-commons/spectral-problem-details-ruleset) | A grounded Spectral ruleset for RFC 9457 Problem Details — check that your error responses really are problem details. |
| **Spectral Reporter** | [reporter.apicommons.org](https://reporter.apicommons.org) | Turn a Spectral lint run into a self-contained HTML governance report (with SARIF + trends). |
| **Spectral Ruleset Studio** | [studio.apicommons.org](https://studio.apicommons.org) | Turn a prose style guide into an owned, grounded, well-named Spectral ruleset. |
| **Toolsmith** | [toolsmith.apicommons.org](https://toolsmith.apicommons.org) | Forge MCP tools and Agent Skills from your OpenAPI — a workbench for designing the agent layer of an API. |

See the full, current list at [apicommons.org/tools](https://apicommons.org/tools/).

## Find your way around

New here? Start with the hub, then dig into the tools or the building blocks.

**Tools** — browser-first, backend-free apps
- [apicommons.org/tools](https://apicommons.org/tools/) — the full, current index
- [validator.apicommons.org](https://validator.apicommons.org) · [studio.apicommons.org](https://studio.apicommons.org) · [graph.apicommons.org](https://graph.apicommons.org) · [reporter.apicommons.org](https://reporter.apicommons.org) — a few to start with

**Building blocks** — machine-readable properties of API operations
- [policies](https://github.com/api-commons/policies) · [rules](https://github.com/api-commons/rules) · [guidance](https://github.com/api-commons/guidance) · [lifecycle](https://github.com/api-commons/lifecycle) · [plans](https://github.com/api-commons/plans) — and more, above

**Specs** — schemas, profiles, and templates
- [api-onboarding](https://github.com/api-commons/api-onboarding) (AID) · [api-authorization](https://github.com/api-commons/api-authorization) · [problem-details-for-http-apis](https://github.com/api-commons/problem-details-for-http-apis) · [json-api](https://github.com/api-commons/json-api)

**The network**
- [github.com/api-commons](https://github.com/api-commons) — every repo, each released independently
- [apis.io](https://apis.io) — the API discovery network API Commons is part of
- [apisjson.org](https://apisjson.org) — the APIs.json discovery format
- Questions or contributions — [open an issue](https://github.com/api-commons/api-commons/issues)

---

A project of [API Evangelist](https://apievangelist.com), maintained openly under
API Commons. The building blocks and tools are open and free to use; API Evangelist
offers expert API governance and strategy services around them.
