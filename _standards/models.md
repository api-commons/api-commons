---
name: The OpenAI Interface
standard_id: openai-v1
description: >-
  The inference contract every model host, router and local runtime speaks. OpenAI
  published an API; the industry turned it into a wire format, and a chat completion
  request written for one provider now runs against hundreds. This profiles that
  interface as it is actually implemented, grades it into tiers, and records who
  implements what.
originator: OpenAI
cohort: reimplementation
status: Published — 338 operations graded, 175 adopters recorded
repository: https://github.com/api-commons/models
image: /images/api-commons-icon.png

source:
  name: openai/openai-openapi
  url: https://github.com/openai/openai-openapi
  license: MIT
  note: >-
    OpenAPI 3.1.0, info.version 2.3.0 — 215 paths, 338 operations. The upstream document
    moves weekly, so each profile release pins a commit SHA rather than tracking a branch.
  pinned: 38170fdddbb6a1813eae6c6587ee17cf2987185b

tiers:
  - name: Core
    count: 2
    description: >-
      Measured, not chosen. POST /chat/completions is declared by 87.5% of the cohort and
      GET /models by 71.7%. Nothing else clears a third, so the tier boundary sits in a
      gap rather than at a threshold somebody picked.
  - name: Extended
    count: 19
    description: >-
      Declared by 5% to 50% of the cohort — embeddings (32.5%), the legacy completions
      endpoint (30.0%), image generation (23.3%), the Responses API (21.7%), audio, files
      and batches. This is where implementations diverge.
  - name: Vendor
    count: 317
    description: >-
      Under 5% of the cohort declares any of these — Assistants, ChatKit, Realtime, evals,
      and the whole organization administration surface. Effectively OpenAI-only in
      practice, and excluded from the profile OpenAPI by design.

adopters:
  count: 175
  as_of: '2026-09-13'
  url: https://github.com/api-commons/models/blob/main/adopters/adopters.yml
  evidence:
    - grade: declared
      count: 101
      description: >-
        Publishes their own OpenAPI, harvested byte-identical from their site, which
        declares operations in this profile. 15 reach the core tier and 52 reach extended;
        34 declare part of the profile but not the whole core tier.
    - grade: vendor-matrix
      count: 0
      description: Publishes their own compatibility table. None harvested yet.
    - grade: prose
      count: 74
      description: >-
        States compatibility in their own words and publishes no spec we can read.
        Recorded, never promoted to a verdict.
    - grade: tested
      count: 0
      description: >-
        The conformance flow was run against a live endpoint. Not yet attempted — unlike
        open data and blockchain, this needs credentials and costs money.

apis:
  - name: OpenAPI
    description: The core and extended surface, self-contained, with x-tier on every operation.
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-commons/models/main/standard/openai-v1/openapi.yml
  - name: Profile
    description: All 338 operations, each with its tier and the evidence for that grading.
    properties:
      - type: Profile
        url: https://raw.githubusercontent.com/api-commons/models/main/standard/openai-v1/profile.yml
  - name: Overlay
    description: Stamps the tier grading onto the upstream OpenAI spec without copying it.
    properties:
      - type: Overlay
        url: https://raw.githubusercontent.com/api-commons/models/main/standard/openai-v1/overlay.yml
  - name: Arazzo
    description: The flow that proves a core claim — list models, then use one.
    properties:
      - type: Arazzo
        url: https://raw.githubusercontent.com/api-commons/models/main/standard/openai-v1/arazzo/core-conformance.yml
  - name: MCP Tools
    description: MCP tool definitions for the core tier.
    properties:
      - type: MCP
        url: https://raw.githubusercontent.com/api-commons/models/main/standard/openai-v1/mcp/tools.json
  - name: Spectral Ruleset
    description: Lint any provider's OpenAPI and see which tier it reaches.
    properties:
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-commons/models/main/standard/openai-v1/spectral/openai-profile.yaml
  - name: Adopter Matrix
    description: Generated — operation by adopter, across everyone who publishes a spec.
    properties:
      - type: Adopters
        url: https://github.com/api-commons/models/blob/main/adopters/matrix.md

licensing: >-
  The profile is independently authored from openly licensed machine-readable sources and
  public documentation; it does not republish a vendor's document. The upstream OpenAPI is
  MIT and carries its attribution. API Commons artifacts are CC BY-NC-SA 4.0 and code is
  Apache-2.0. "OpenAI" appears as a factual reference to the interface described, and
  nothing here implies endorsement.

tags:
  - Models
  - LLM
  - Inference
  - Artificial Intelligence

further_reading:
  - name: The adopters building block
    url: https://github.com/api-commons/adopters
    description: The schema behind the registry, and the evidence grades it enforces.
---
