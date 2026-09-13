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
status: Profile in progress — adopters identified, none graded
repository: https://github.com/api-commons/models
image: /images/api-commons-icon.png

source:
  name: openai/openai-openapi
  url: https://github.com/openai/openai-openapi
  license: MIT
  note: >-
    OpenAPI 3.1.0, info.version 2.3.0 — 162 paths, 242 operations, 959 schemas. The
    upstream document moves weekly, so each profile release pins a commit SHA.

tiers:
  - name: Core
    description: >-
      Implement this or the compatibility claim is false — /chat/completions,
      /completions, /embeddings and /models.
  - name: Extended
    description: >-
      Commonly emulated and materially varied — streaming SSE, tool calling, structured
      outputs, vision inputs, /files. This is where implementations diverge.
  - name: Vendor
    description: >-
      OpenAI alone operates these, and they are out of scope by design — Assistants,
      ChatKit, Realtime, evals, and organization administration.

adopters:
  count: 211
  as_of: '2026-09-13'
  url: https://github.com/api-commons/models/blob/main/adopters/adopters.yml
  evidence:
    - grade: declared
      count: 0
      description: Publishes a machine-readable spec that lints against the profile.
    - grade: vendor-matrix
      count: 0
      description: Publishes their own compatibility table.
    - grade: prose
      count: 211
      description: >-
        States compatibility in their own words. Identified from the API Evangelist
        catalog and not yet graded further.
    - grade: tested
      count: 0
      description: The profile's read-only flows were run against a live endpoint.

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
