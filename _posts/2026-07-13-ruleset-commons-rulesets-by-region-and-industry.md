---
layout: post
title: "Ruleset Commons: Provenanced Rulesets by Region and Industry"
date: 2026-07-13
tags:
  - API Commons
  - Spectral
  - API Governance
  - Rulesets
  - Registry
image: /assets/images/blog/ruleset-commons-rulesets-by-region-and-industry.png
---

Most API linting runs on nothing you own. In a study of 1,005 real-world Spectral pipelines, 63% ran the linter's implicit defaults and only 8 extended a shared, remote ruleset. The demand for governance is there; the supply of adoptable, owned rulesets is not. So we built **Ruleset Commons** — a curated registry of rulesets you can adopt by reference, by region and by industry, instead of silently running Spectral's, Redocly's, or vacuum's defaults.

[**Try it → rulesets.apicommons.org**](https://rulesets.apicommons.org)

## Adoptable and Provenanced

Every entry answers two questions the defaults never do. **Who owns this** — a real, named owner and a URL where that ownership is documented, because a ruleset without an owner is a config, not a standard. And **how do I adopt it** — a copy-paste `adoptVia` snippet: a remote `extends` URL, an npm package, or config to paste. You adopt by reference so you inherit updates instead of forking a frozen copy.

Each entry also carries a **`governed`** flag, so the registry stays honest about what is a real standard and what is just a tool default.

| Flag | Meaning |
| --- | --- |
| **Governed** | An owned, provenanced standard with naming, ownership, and domain rules — Italy's `api-oas-checker`, the NL API Design Rules, the OWASP security rulesets. |
| **Default** | A tool's built-in config, honestly labeled — `spectral:oas`, Redocly `recommended`, vacuum's defaults — so teams can *see what they are actually running* and swap it for something owned. |

## One Open Data File

In the spirit of the [MCP Install](https://install.apicommons.org) client registry, the whole commons is a single open, machine-readable file — **`rulesets.json`** — served as open data at [`/rulesets.json`](https://rulesets.apicommons.org/rulesets.json) and validated by a published JSON Schema. Each entry records its `id`, `publisher`, `category` (`national`, `industry`, `security`, `vendor-default`, `community`, `company`), `provenance`, `sourceUrl`, `adoptVia`, `artifactTypes`, and `governed` flag. The website is simply a browsable directory over that file, with category, artifact-type, and governed-versus-default filters plus search and a copy-paste "how to adopt" snippet.

The seed set is mined from real ecosystem usage — including every remote ruleset observed in our Spectral pipelines research corpus, from the Italian and Dutch government rulesets to the single most-referenced remote ruleset in the whole corpus, alongside the OWASP security rulesets and the honestly-labeled vendor defaults. The commons grows by pull request against `rulesets.json`: fork, add an object with a genuine owner and a resolvable `adoptVia` value, and open a PR.

Ruleset Commons is one of the [API Commons tools](https://apicommons.org/tools/), and like the rest of them it is open, portable, and Spectral underneath — because the rulesets that decide whether an API is any good should not be locked inside a vendor. It is part of a series introducing the tools one at a time.
