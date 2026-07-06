---
layout: post
title: "API Validator: Governance Checks in the Browser"
date: 2026-07-07
tags:
  - API Commons
  - API Governance
  - Spectral
  - OpenAPI
  - AsyncAPI
  - Arazzo
  - JSON Schema
image: /assets/images/blog/api-validator-governance-in-the-browser.png
---

Most API governance tooling assumes a pipeline, an account, and a server that your document gets uploaded to. That is the wrong default for the most common moment of all: someone has a spec open and wants a fast, honest read on it. So we built [**API Validator**](https://validator.apicommons.org) — a browser-first governance tool that lints your document where it already is, with nothing leaving the page.

[**Try it → validator.apicommons.org**](https://validator.apicommons.org)

## Four Artifact Types, On Purpose

API Validator lints [**OpenAPI** (3.x *and* Swagger 2.0), **AsyncAPI**, **Arazzo**, and **JSON Schema**](https://validator.apicommons.org) — and nothing else. The narrowness is deliberate: this is the tool you open to check one document, not a platform to adopt. [Spectral](https://github.com/stoplightio/spectral) runs entirely client-side, so your tokens and your specs never touch a backend.

A detail we care about: **Swagger 2.0 is governed at full parity with OpenAPI 3.x**. The curated OpenAPI catalog lints `swagger: "2.0"` documents exactly as it lints 3.x — rules are either broadened to match both structures or shipped as format-gated `oas2`/`oas3` twins, so a rule only fires on the versions it applies to and never false-positives across formats. Most of the world's OpenAPI is still 2.0; a validator that ignores that is ignoring the corpus.

## Educate First, Enforce by Choice

Every rule ships at **`info`**. The default posture is to teach, not to block; you raise individual rules to `warn` or `error` for the conventions you decide to enforce, and those overrides persist in your browser. The rule editor is a focused form — severity, message, and description — with no raw-YAML foot-guns.

The catalog itself is **best-of-breed**, compiled from the first-party [API Evangelist](https://github.com/api-evangelist/rules) OpenAPI ruleset plus public, redistribution-compatible Spectral rulesets from SPS Commerce, Adidas, Trimble, Paystack, DigitalOcean, Microcks, and more — all Apache-2.0 or MIT, with attribution and vendored licenses recorded in the repo.

## More Than a Linter

Search GitHub, GitLab, or Bitbucket with your own token and load any artifact straight into the Monaco editor with a YAML ⇄ JSON toggle. Render readable docs from the current artifact, run per-artifact utilities — bundle `$ref`s, componentize, split by tag or channel or workflow, migrate JSON Schema drafts — and assemble everything you have saved into a single [**APIs.json 0.21**](https://apis.io) index you can download.

API Validator is one of the [API Commons tools](https://apicommons.org/tools/), and like the rest of them it is open, portable, and Spectral underneath — because the rules that decide whether an API is any good should not be locked inside a vendor. This is the first in a series introducing the tools one at a time.
