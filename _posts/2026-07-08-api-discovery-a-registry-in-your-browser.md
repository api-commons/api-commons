---
layout: post
title: "API Discovery: A Registry That Lives in Your Browser"
date: 2026-07-08
tags:
  - API Commons
  - Discovery
  - APIs.json
  - OpenAPI
  - Registry
  - API Governance
image: /assets/images/blog/api-discovery-a-registry-in-your-browser.png
---

Most registries assume a central server that every team writes to and nobody trusts is current. But real API catalogs are relative to domains, teams, categories, and purposes — they are ephemeral and ever-changing, not one static list somebody blesses once. So we built [**API Discovery**](https://discovery.apicommons.org): a browser-first registry that composes purpose-scoped catalogs from a shared pool of discovered artifacts, with nothing leaving the page.

[**Try it → discovery.apicommons.org**](https://discovery.apicommons.org)

## Discover Into One Pool, Compose Many Catalogs

You discover into a single pool — search or **Scan** APIs.io, GitHub, GitLab, Bitbucket, SwaggerHub, and Postman as you add keys, across 11 artifact types including OpenAPI, AsyncAPI, Arazzo, MCP, and agent skills. Upload **HAR** traffic captures and they are synthesized into evidence-based OpenAPI, or **Import** a bundle from the enterprise helper CLI (Backstage, Apigee, Azure APIM, MuleSoft, AWS, Kong, Tyk, Kubernetes, Kafka). Then you compose named **views** over that pool: type an intent like *"everything payments"* and **🧠 Compose** semantic-matches the pool with a small embedding model that runs in your browser. The same artifact can live in many catalogs, and deleting a catalog deletes nothing.

## A Catalog Is a Build Artifact, Not a Database

Every composed catalog carries its **recipe** as `x-recipe` in the export and can be rebuilt against live sources anytime — freshness badges are first-class, because a catalog is something you regenerate, not something you hand-tend forever. Inside any catalog, cluster members into named business capabilities with **🧠 Suggest**, pick canonicals, and ship the capability map as `x-capabilities`.

| Step | What you get |
| --- | --- |
| Discover | One shared pool across 11 artifact types |
| Compose | Purpose-scoped catalogs by intent |
| Regenerate | Rebuild from the `x-recipe` anytime |
| Publish | APIs.json (YAML) you commit, PR, or federate |

## Publish and Federate, Don't Centralize

Download any catalog as [**APIs.json**](https://apis.io) in YAML, commit or PR it straight to a repo, and export a **catalog of catalogs** — an APIs.json `includes` index linking every purpose-built catalog. You federate instead of centralizing. Discovery stops at cataloging on purpose: governance and deep linting live in [API Validator](https://validator.apicommons.org), and reusability scoring lives in [API Reusability](https://reusability.apicommons.org).

API Discovery is one of the [API Commons tools](https://apicommons.org/tools/), open and browser-first like the rest. This is the second in a series introducing the tools one at a time.
