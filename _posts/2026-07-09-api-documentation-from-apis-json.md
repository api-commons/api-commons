---
layout: post
title: "API Documentation: OpenAPI and Arazzo From APIs.json"
date: 2026-07-09
tags:
  - API Commons
  - Documentation
  - APIs.json
  - OpenAPI
  - Arazzo
image: /assets/images/blog/api-documentation-from-apis-json.png
---

An APIs.json describes a collection of APIs — and since version 0.19 it can carry the artifacts themselves inline: full OpenAPI definitions, Arazzo workflows, prompts, and rules living right inside the index. So we built [**API Documentation**](https://documentation.apicommons.org), a standalone tool that turns any APIs.json into rich, readable HTML. Nothing leaves the browser, and there is no backend.

[**Try it → documentation.apicommons.org**](https://documentation.apicommons.org)

## What It Renders

Point it at an APIs.json and you get the whole picture. Every API in the index shows up with its link properties — documentation, signup, pricing, authentication — as cards. Any **inline OpenAPI** is rendered as a full API reference: servers, authentication, tag-grouped operations, parameters, request bodies, and response schemas. Any **inline Arazzo** becomes a step-by-step workflow timeline with inputs, payloads, success criteria, and outputs. On top of that it surfaces the common properties, workflows, prompts, rules, includes, overlays, network, and maintainers — and it reads every specification version, **0.11 through 0.21**, with advisory notes when a document reaches for fields newer than the version it declares.

## Three Ways to Use It

The tool is built to be portable, because documentation you cannot move is documentation you do not really own.

| Mode | How | Result |
| --- | --- | --- |
| **Hosted** | Drop a file, or add `?url=` to point at any APIs.json on the web | Instant docs in the browser |
| **Zip** | Rename the built viewer `index.html`, sit it next to your `apis.json` | Self-contained folder; the viewer finds its sibling |
| **Single file** | `npm run bundle -- apis.json my-apis.html` | One HTML file that works from disk, a gist, or email |

Two examples ship with the site: a [local food business bundle](https://documentation.apicommons.org/examples/running-a-local-food-business-on-apis/) — an APIs.json 0.21 bundle with 8 APIs carrying inline OpenAPI and per-API and cross-provider Arazzo workflows — and a [classic 0.14 index](https://documentation.apicommons.org/examples/api-evangelist-classic/) with URL-only properties, the way APIs.json looked when apis.io launched.

## Your Index, Your Source of Truth

There is no import step and no platform to adopt. The APIs.json is the source of truth; this tool just reads it and makes it legible to a human. That is the whole design.

API Documentation is one of the [API Commons tools](https://apicommons.org/tools/), open and Apache-2.0 like the rest of them, and this is another entry in our series introducing the tools one at a time.
