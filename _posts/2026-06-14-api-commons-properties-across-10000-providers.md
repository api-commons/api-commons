---
layout: post
title: 'API Commons Properties Across 10,000 API Providers'
date: 2026-06-14
tags:
  - API Commons
  - Properties
  - Standards
  - Vocabulary
  - Governance
image: /assets/images/blog/api-commons-properties-across-10000-providers.png
---
The API Evangelist catalog has crossed 10,000 provider repositories, and running a count of which API Commons property types appear across those repos produces something worth looking at closely. Not because the numbers are impressive — though some of them are — but because of what they reveal about how API providers actually describe what they offer and where the machine-readable gaps still are.

## What the Numbers Show

The most widely documented properties are the ones you'd expect. Website appears in 7,836 repos. Documentation in 6,723. LinkedIn in 5,830. These are baseline identifiers — the minimum an API provider publishes about themselves. After that the numbers start to tell a more interesting story.

GitHubOrganization shows up in 3,958 repos, which reflects how central open-source tooling has become to API operations. Blog at 3,315 and JSONSchema at 3,033 sit close together — two forms of publishing, one narrative and one structural. Pricing at 2,482 and Integrations at 2,441 follow, and then a cluster of operational properties that all land in the 2,000–2,400 range: SDK, TermsOfService, RateLimits, Portal, PrivacyPolicy, Support, Plans, and FinOps.

That cluster is where the governance story is. RateLimits documented across 2,295 providers. FinOps — the property that surfaces cost-related metadata — across 2,016. Plans at 2,116. These are not properties that most providers thought to publish in a machine-readable way five years ago. They published them as HTML pages for human readers, which meant every tool or agent trying to understand the operational envelope of an API had to scrape and guess. The API Commons property vocabulary gives those signals a consistent home.

Further down: StatusPage at 1,736, Vocabulary at 1,535. The vocabulary and semantic properties sit at the lower end, which makes sense — semantic interoperability is a harder problem than documenting a rate limit. But 1,535 providers with a Vocabulary property reference is a foundation to build on.

## The Spec Layer

Across the full catalog there are 10,754 OpenAPI specs and 14,123 unique tags. The tags represent the informal vocabulary that providers have developed organically — the way they've chosen to describe their own surface area. The gap between 10,000 providers and 10,754 OpenAPI specs means some providers have multiple specs, and also that not every provider has one at all. The JSONSchema property at 3,033 connects directly to data models extracted from those specs, making the schema layer independently discoverable.

## Governance Without Machine-Readable Specs

The Plans, RateLimits, and FinOps properties are doing governance work that doesn't depend on having a machine-readable API spec in place. A provider can document their rate limits, pricing tiers, and cost structure through API Commons property references in an APIs.json file without publishing a complete OpenAPI document. That matters because it means the governance baseline can extend to APIs that are still documented informally, not just the ones that have invested in full spec coverage.

For teams building tooling on top of this catalog — whether that's API discovery, compliance checking, cost modeling, or AI-assisted integration — these properties are the entry points. A provider with RateLimits, Plans, and FinOps documented is a provider whose operational behavior can be reasoned about without a human reading the docs first.

## Semantic Properties and What's Next

The Vocabulary and JSONLDContext properties are at the lower end of adoption right now, but they represent the direction API Commons is heading. As more APIs need to interoperate — passing data between systems, combining outputs from multiple providers, feeding structured information to agents — shared semantic definitions become critical. The vocabulary layer is where API Commons can make that interoperability more systematic rather than leaving it to each integration to negotiate on its own terms.

The catalog at 10,000 providers is a snapshot of where API documentation practice actually stands, not where best practices say it should be. The property counts show what providers choose to publish when they have a standard vocabulary to publish against. The more useful API Commons makes that vocabulary, the more it will be used.
