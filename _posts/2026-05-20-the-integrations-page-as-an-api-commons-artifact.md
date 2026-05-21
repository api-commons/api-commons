---
layout: post
title: "The Integrations Page as an API Commons Artifact"
date: 2026-05-20
tags:
  - API Commons
  - integrations
  - Naftiko
  - API operations
  - capabilities
  - spec-driven integration
---

Most "integrations" pages in the API economy are screenshots. A grid of partner logos. Sometimes a sentence or two. Almost never anything an agent — or another developer — can actually *run*. The page exists to convince a human reader that the integration ecosystem is real. It is marketing. It is not a contract.

The [Stripe Integrations page on APIs.io](https://providers.apis.io/providers/stripe/integrations/) is a small experiment in what happens when you take that page seriously as an API Commons artifact. Each entry is a [Naftiko](https://naftiko.io) capability — a declarative YAML manifest that describes a real integration workflow involving Stripe and at least one other system. They are versioned. They are testable. They are runnable end-to-end with one Docker command. And because they are specifications, not bespoke code, they are commons artifacts in exactly the same sense that an OpenAPI document is.

Kin has been pushing on this concept publicly. [His LinkedIn essay this week](https://www.linkedin.com/pulse/pushing-forward-concept-integration-page-naftiko-sng5e/) lays out the broader argument for why integration pages need to stop being static screenshots and start being a real machine-readable surface — for partners, for AI agents, and for the providers themselves who currently shoulder the cost of every bespoke integration that walks in the door.

## What Changes When the Page Becomes a Contract

An integration manifest is a different kind of object than an integration screenshot.

A screenshot describes a relationship — "Stripe works with Shopify." A manifest describes the *operation* — which Stripe endpoints, which Shopify endpoints, in what sequence, under what authentication, returning what shape of data. The first is a marketing claim. The second is a checkable assertion.

When the integrations page consists of checkable assertions, every constituency benefits:

- **API producers** stop being on the hook for one-off integration code. New partners can author a YAML file and the integration *runs*. The provider's surface is the API plus the capability format — not "the API plus a growing inventory of bespoke connector projects we have to maintain forever."
- **API consumers** can clone an existing capability that already does ~80% of what they want, fork it for the last 20%, and ship. The capability is a starting point that is also the artifact — not a screenshot inviting them to start from scratch.
- **AI agents** can discover, read, and invoke these capabilities directly. There is no documentation-to-code translation step. The spec *is* the integration.

This is the same argument [we made for Spec-Driven Integration](/2026/04/21/spec-driven-integration-capability-specs-as-shared-integration-artifacts/) — applied to the publishing surface where most providers tell the integration story.

## Why This Belongs in the Commons

API Commons has always argued that machine-readable artifacts about how an API operates are more valuable when they are shared, forkable, and composable. The conversation has historically centered on the contract (OpenAPI), the catalog (APIs.json), and the operational properties (the [API Commons vocabulary](https://apicommons.org/properties/)). Integrations have lived outside that frame — too provider-specific, too implementation-flavored, too bound up in private connector code.

A capability spec is what changes that. It is operational. It is portable. It is declarative enough to live alongside the OpenAPI in a provider's repo, and concrete enough to actually do work. Most importantly, it composes — a Stripe capability that fires a Slack notification on a successful charge is built from a Stripe consumes block and a Slack consumes block, both of which can live in shared YAML and be reused by hundreds of other capabilities. That is the commons philosophy applied to integrations: shared definitions, open licenses, composable artifacts, executable on any runtime that implements the spec.

## The Stripe Page as a Sketch

The Stripe integrations page is a starting sketch, not a finished destination. The first 50 capabilities focus on the integrations that come up most frequently in Stripe's own partner ecosystem — payments to CRM, payments to analytics, payments to operations tooling. Each is a YAML file you can read in a few minutes, fork into your own repo, and run under Naftiko in a Docker container.

There are obvious next steps. Some are mechanical: cover the other 200+ providers in APIs.io with the same treatment. Some are harder: develop the conventions for how a provider *officially* publishes a capability versus how the community contributes one, how versioning works as a capability gets adopted across hundreds of consumers, how to handle the privacy and security surfaces that bespoke connectors handle today.

But the directional bet is straightforward: the integrations page of the next decade is a directory of executable capability specs, published under open licenses, composable from shared building blocks. The screenshot wall has run its course.

[Browse the Stripe integrations →](https://providers.apis.io/providers/stripe/integrations/) | [Read Kin's framing on LinkedIn →](https://www.linkedin.com/pulse/pushing-forward-concept-integration-page-naftiko-sng5e/) | [Naftiko Framework on GitHub →](https://github.com/naftiko/framework)
