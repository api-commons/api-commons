---
layout: post
title: "Spectral OWASP Ruleset: The API Security Top 10 as Rules"
date: 2026-07-14
tags:
  - API Commons
  - Spectral
  - API Security
  - OWASP
  - API Governance
image: /assets/images/blog/spectral-owasp-ruleset-api-security-top-10-as-rules.png
---

Most teams lint their OpenAPI for style but never for security. A study of 1,005 public API pipelines found only **14%** run any security rules at all, and just **3.4%** emit SARIF for the security tooling they do run. So we built [**Spectral OWASP Ruleset**](https://github.com/api-commons/spectral-owasp-ruleset) — a curated, owned, grounded [Spectral](https://github.com/stoplightio/spectral) ruleset that maps to the [OWASP API Security Top 10 (2023)](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) and adds a real security governance layer to your linting in one line.

**`npm i -D @api-common/spectral-owasp-ruleset`**

```yaml
# .spectral.yaml
extends:
  - "spectral:oas"
  - "@api-common/spectral-owasp-ruleset"
```

```bash
npx @stoplight/spectral-cli lint openapi.yaml
```

Prefer no install? Point `extends` at the raw ruleset file on a pinned tag or commit and skip the package entirely.

## Grounded, owned, and honest about coverage

It maps **22 OWASP checks to all ten OWASP API Security categories**, using only Spectral's built-in functions — no custom JavaScript to install, audit, or trust beyond Spectral itself. Every rule carries its provenance: a stable OWASP-mapped id, a description of the risk, a finding message, a severity, and a `documentationUrl` that deep-links the specific OWASP item it defends.

We do not fake coverage. Parts of the Top 10 are runtime authorization and abuse decisions a static document cannot express, so where an item is directly lintable we ship a real check, and where it is not we ship the strongest static **proxy** we honestly can and mark the residual **advisory**.

| OWASP item | Static coverage |
| --- | --- |
| API1 BOLA | Proxy — require auth *declared* per operation |
| API2 Broken Authentication | Lintable — schemes, key location, no Basic, HTTPS OAuth |
| API3 BOPLA | Proxy — request/response schemas so properties are reviewable |
| API4 Resource Consumption | Lintable — `maxItems`/`maxLength`/`maximum` bounds |
| API5 BFLA | Proxy — default-deny `security` baseline |
| API6 Sensitive Business Flows | Advisory — nudge a `429` on state-changing ops |
| API7 SSRF | Advisory — flag URL-bearing inputs for review |
| API8 Security Misconfiguration | Lintable — HTTPS servers, no TRACE, servers declared |
| API9 Improper Inventory | Lintable — version, contact, per-op description/operationId |
| API10 Unsafe Consumption | Advisory — HTTPS on the URLs the doc points others to |

## Parity across Swagger 2.0 and OpenAPI 3.x

Spectral auto-detects a document's format and each check runs on the shape it applies to. Format-agnostic checks carry no `formats` tag and fire on both; where the specs differ structurally — security schemes, transport, request and response bodies — the 3.x rule is tagged `formats: [oas3]` and a `-oas2` twin carries the same OWASP grounding for Swagger 2.0. Nothing false-positives or no-ops across formats. The repo ships intentionally-broken and well-governed fixtures for both, plus a test that proves the ruleset actually fires on each. We like running it as its own CI job so a security regression is unambiguous, and optionally emitting SARIF into the repo's code-scanning tab.

Spectral OWASP Ruleset is one of the [API Commons tools](https://apicommons.org/tools/), open and Apache-2.0 like the rest of them — because the rules that decide whether an API is safe should not be locked inside a vendor. This is another in a series introducing the tools one at a time.
