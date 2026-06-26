---
layout: post
title: 'The Diverse Vocabulary of API Properties'
date: 2026-06-26
tags:
  - API Commons
  - Properties
  - Vocabulary
  - Standards
  - Governance
  - FinOps
image: /assets/images/blog/api-commons-is-more-than-just-the-definition-specification-or-schema.png
---

API Commons has always been about the things _around_ the API — the properties that make an API usable, governable, and comparable: its documentation, its terms of service, its plans, its rate limits, its SDKs, and now its prompts, rules, and workflows. A property is only useful as a commons if everyone names it the same way. So we went and looked at how the vocabulary is actually being used at scale, and then did the work to make it more consistent.

The corpus is the [API Evangelist network](https://github.com/api-evangelist) — **10,245 API providers**, each kept as its own repository with a machine-readable index at its root. Across those indexes there are **212,780 property references** drawn from a shared vocabulary of common API operations.

## A shared core, and a very long tail

The [reserved vocabulary](https://apisjson.org/format/reservedwords) defines **123 canonical property types** — the common building blocks that tooling, search engines, and AI agents can rely on. But real providers describe themselves with far more than 123 words. Even after normalization, these indexes use **7,134 distinct `type` values**.

That is not noise — it is the commons doing its job. The core vocabulary covers what everyone shares (Documentation, Authentication, Pricing, RateLimits, OpenAPI, FinOps), and the `X-` custom prefix leaves room for everything a particular provider, industry, or moment needs to express: trust centers, investor relations, status feeds, carbon reports, marketplace listings, Kubernetes operators. A healthy commons is consistent at the center and open at the edges.

## What gets published most

Counting how many of the 10,245 providers publish each property tells you what the commons actually values:

| Property | Providers |
| --- | --- |
| Documentation | 8,393 |
| Website | 8,135 |
| LinkedIn | 6,240 |
| GitHubOrganization | 4,205 |
| OpenAPI | 4,203 |
| Blog | 3,282 |
| RateLimits / Pricing / Plans | ~2,700 each |
| FinOps | 2,521 |
| TermsOfService | 2,412 |

The specification matters, but it sits behind the human and operational properties. The interface license, the terms, the pricing, the support channel — the API Commons concerns — are what turn a published endpoint into something an organization can responsibly depend on.

## Normalizing toward the common standard

A commons only works if the same thing has one name. Our survey found the same concepts written a dozen ways — `SDK` and `SDKs`, `Sign Up` and `SignUp` and `Signup`, `JSON Schema` and `JSONSchema`, `GitHub Org` and `GithubOrg`. We ran a careful normalization pass that folded roughly **19,000 references** back onto their canonical reserved type, collapsing only mechanical casing/spelling variants and a curated set of safe synonyms. Genuinely distinct properties were left untouched, and provider-specific custom types were preserved under the `X-` prefix. The [common properties listing](/common/) now documents the full vocabulary, each property with its description, aliases, and a machine-readable example.

## Where to find it

Every property described here is open and machine-readable in two complementary places:

- **As source on GitHub** — each provider is a repository under [github.com/api-evangelist](https://github.com/api-evangelist), with its index and the referenced artifacts (OpenAPI, plans, rate limits, FinOps, rules, workflows) committed alongside it. The commons is literally version-controlled.
- **As search on [APIs.io](https://apis.io)** — the same indexes are crawled into a public search engine, queryable by provider, property, tag, and region, and exposed through an MCP server so AI agents can reason over the commons directly.

A shared vocabulary, applied consistently across ten thousand providers, kept in the open, and queryable by both humans and machines — that is what makes API properties a commons rather than ten thousand private conventions.
