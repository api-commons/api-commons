---
layout: post
title: "The Train Travel API Moves to OpenAPI 3.2"
date: 2026-10-23
tags:
  - API Commons
  - OpenAPI
  - OpenAPI 3.2
  - Examples
image: /assets/images/blog/train-travel-moves-to-openapi-3-2.png
---

The [Train Travel API](https://github.com/api-commons/train-travel) is the example OpenAPI we keep in the commons because it is small enough to read in one sitting and real enough to exercise tooling. Today it moved to OpenAPI 3.2. Thanks to [Polo](https://github.com/Polo2) from Bump.sh, who opened [PR #3](https://github.com/api-commons/train-travel/pull/3) to bring our copy back in sync with the upstream [bump-sh-examples/train-travel-api](https://github.com/bump-sh-examples/train-travel-api) — and to strip out Bump.sh-specific vendor extensions like `x-topic` along the way, so what lives here is plain specification.

## What 3.2 Looks Like in a Real Document

The diff is about 800 lines, and most of it is the new specification earning its keep:

- **Navigation tags.** Tags now carry `kind: nav` and `parent:`, so "Search" and "Booking & Payment" become real sections with children — structure the document owns instead of the docs renderer.
- **Named servers.** Servers get a `name`, so "Production" is a fact in the contract, not a guess from a URL.
- **`QUERY /stations`.** Station search gets the HTTP [QUERY](https://www.ietf.org/archive/id/draft-ietf-httpbis-safe-method-w-body-08.html) method — a safe, idempotent request with a body — badged Beta. The old `GET /stations` is marked `deprecated` and badged "Removed next release." That is a deprecation path written down where agents and tools can read it.
- **`SUBSCRIBE /trips/{id}`.** A custom verb, declared through `additionalOperations`, for following a trip as it happens.
- **Examples that say what they mean.** The Example Object now uses `dataValue` in place of the overloaded `value`, and `serializedValue` shows exactly what goes over the wire for the subscription stream.
- **Security.** The existing OAuth 2 scheme gains `oauth2MetadataUrl`, and a new `deviceAuthorization` scheme covers the device flow.

## Why an Example Matters

A year after 3.2 shipped, most tooling still does not state support for it. Specifications get adopted when there are honest, working documents to test against — not when the release notes go out. A shared example that uses query, additional operations, nav tags, and the new example fields in one place is exactly what tool builders need to find out where they break.

Keeping it in sync with Bump.sh's upstream also matters. One example, maintained in the open by more than one party, is worth more than two that drift apart. That is the whole point of a commons.

Grab the [openapi.yml](https://github.com/api-commons/train-travel/blob/main/openapi.yml), point your validator, docs, mock server, or SDK generator at it, and see what happens. If something breaks, that is a finding — open an issue, here or with the tool.
