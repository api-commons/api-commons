---
name: Models
description: >-
  Two API standards that nobody standardized. OpenAI published an API and the industry
  turned it into a wire format; Anthropic's Messages API became the second dialect a
  growing share of model hosts speak. Both are profiled here as adopters actually
  implement them, graded into tiers by measured adoption, with a registry of who
  implements what and how strongly each claim is evidenced.
cohort: reimplementation — independent servers written against someone else's published surface
status: Published — 582 operations graded across two profiles, 195 adopters recorded
repository: https://github.com/api-commons/models
image: /images/api-commons-icon.png

profiles:

  - name: The OpenAI Interface
    standard_id: openai-v1
    originator: OpenAI
    description: >-
      "OpenAI-compatible" appears in the documentation of 211 providers. Measured against
      what they publish, it means two operations.
    source:
      name: openai/openai-openapi
      url: https://github.com/openai/openai-openapi
      license: MIT
      pinned: 38170fdddbb6a1813eae6c6587ee17cf2987185b
      note: OpenAPI 3.1.0, info.version 2.3.0 — 215 paths, 338 operations.
    measurement: >-
      120 of the 211 claimants publish an OpenAPI harvested byte-identical from their own
      site, and those are the denominator. Grading is per method and path, not per path: a
      path-level count credits GET and POST equally, which put GET /chat/completions at the
      adoption rate of POST and DELETE /models/{id} at four times its real share.
    tiers:
      - name: Core
        count: 2
        description: >-
          POST /chat/completions at 87.5% and GET /models at 71.7%. Nothing else clears a
          third, so the boundary sits in a gap rather than at a threshold somebody picked.
      - name: Extended
        count: 19
        description: >-
          5% to 50% — embeddings (32.5%), the legacy completions endpoint (30.0%), image
          generation (23.3%), the Responses API (21.7%), audio, files and batches.
      - name: Vendor
        count: 317
        description: >-
          Under 5% — Assistants, ChatKit, Realtime, evals and the whole organization
          administration surface. Effectively OpenAI-only in practice.
    adopters:
      count: 175
      as_of: '2026-09-13'
      url: https://github.com/api-commons/models/blob/main/adopters/openai-v1.yml
      matrix_url: https://github.com/api-commons/models/blob/main/adopters/openai-v1-matrix.md
      evidence:
        - grade: declared
          count: 101
          description: >-
            Publishes their own OpenAPI, harvested byte-identical, declaring operations in
            this profile. 15 reach core and 52 reach extended; 34 declare part of the
            profile but not the whole core tier.
        - grade: prose
          count: 74
          description: States compatibility in their own words and publishes no readable spec.
        - grade: tested
          count: 0
          description: >-
            Not attempted. Unlike open data and blockchain, running the conformance flow
            here needs credentials and costs money.
    apis:
      - name: OpenAPI
        description: Core and extended surface, self-contained, x-tier on every operation.
        properties:
          - type: OpenAPI
            url: https://raw.githubusercontent.com/api-commons/models/main/standard/openai-v1/openapi.yml
      - name: Profile
        description: All 338 operations with their tier and the evidence for that grading.
        properties:
          - type: Profile
            url: https://raw.githubusercontent.com/api-commons/models/main/standard/openai-v1/profile.yml
      - name: Spectral Ruleset
        description: Lint any provider's OpenAPI and see which tier it reaches.
        properties:
          - type: SpectralRules
            url: https://raw.githubusercontent.com/api-commons/models/main/standard/openai-v1/spectral/openai-profile.yaml
      - name: Arazzo
        description: List models, then use one — the flow that proves a core claim.
        properties:
          - type: Arazzo
            url: https://raw.githubusercontent.com/api-commons/models/main/standard/openai-v1/arazzo/core-conformance.yml
      - name: MCP Tools
        description: MCP tool definitions for the core tier.
        properties:
          - type: MCP
            url: https://raw.githubusercontent.com/api-commons/models/main/standard/openai-v1/mcp/tools.json

  - name: The Anthropic Messages Dialect
    standard_id: anthropic-messages-v1
    originator: Anthropic
    description: >-
      The second language a growing share of model hosts speak. Measuring it required
      solving a problem the first profile did not have.
    source:
      name: anthropics/anthropic-sdk-python — scripts/mock-spec.json.gz
      url: https://github.com/anthropics/anthropic-sdk-python
      license: MIT
      pinned: eb21a4352015686c30f5759e8c2f02d70f5371e2
      note: >-
        OpenAPI 3.1.0 — 165 paths, 244 operations, no declared info.version. Anthropic
        bundled this spec into their own repository on 2026-09-03, in the same commit that
        removed the Stainless CDN URL from .stats.yml. The in-repo file is first-party and
        pinnable by commit, which the CDN copy was not.
    measurement: >-
      29 of Anthropic's operations share a path shape with the OpenAI interface — /models,
      /files, /skills, /vaults, /agents. Graded against everyone who publishes a spec, GET
      /models came out at 86.3% here, and that number was measuring OpenAI. The cohort is
      therefore the 29 providers declaring at least one operation UNIQUE to Anthropic, and
      every shared operation is flagged rather than silently counted.
    tiers:
      - name: Core
        count: 2
        description: >-
          POST /v1/messages at 69.0% — the only operation that identifies the dialect — and
          GET /v1/models at 72.4%, which shares its shape with the OpenAI interface and so
          is evidence of a model listing rather than of this dialect.
      - name: Extended
        count: 11
        description: >-
          count_tokens (13.8%), a single model read, files, skills and the legacy /v1/complete.
      - name: Vendor
        count: 231
        description: >-
          Under 5% — agents, deployments, sessions, batches and the admin surface, plus the
          preview operations the upstream document expresses as a query string on the path key.
    adopters:
      count: 20
      as_of: '2026-09-13'
      url: https://github.com/api-commons/models/blob/main/adopters/anthropic-messages-v1.yml
      matrix_url: https://github.com/api-commons/models/blob/main/adopters/anthropic-messages-v1-matrix.md
      evidence:
        - grade: declared
          count: 20
          description: >-
            Every entry here publishes a spec — by construction, since a prose claim cannot
            be cross-checked when the paths are shared with another dialect. 6 reach core,
            3 reach extended, 11 declare part of the profile but not the whole core tier.
        - grade: prose
          count: 0
          description: Excluded by design for this profile. See the measurement note above.
        - grade: tested
          count: 0
          description: Not attempted — needs credentials.
    apis:
      - name: OpenAPI
        description: Core and extended surface, self-contained, x-tier on every operation.
        properties:
          - type: OpenAPI
            url: https://raw.githubusercontent.com/api-commons/models/main/standard/anthropic-messages-v1/openapi.yml
      - name: Profile
        description: All 244 operations with their tier, evidence, and shared-shape flags.
        properties:
          - type: Profile
            url: https://raw.githubusercontent.com/api-commons/models/main/standard/anthropic-messages-v1/profile.yml
      - name: Spectral Ruleset
        description: >-
          Checks the two things that break a shim written against the wrong dialect —
          max_tokens required, and content blocks rather than choices.
        properties:
          - type: SpectralRules
            url: https://raw.githubusercontent.com/api-commons/models/main/standard/anthropic-messages-v1/spectral/anthropic-profile.yaml
      - name: Arazzo
        description: List models, then send the smallest message with the first one.
        properties:
          - type: Arazzo
            url: https://raw.githubusercontent.com/api-commons/models/main/standard/anthropic-messages-v1/arazzo/core-conformance.yml
      - name: MCP Tools
        description: MCP tool definitions for the core tier.
        properties:
          - type: MCP
            url: https://raw.githubusercontent.com/api-commons/models/main/standard/anthropic-messages-v1/mcp/tools.json

licensing: >-
  Both profiles are independently authored from openly licensed machine-readable sources;
  neither republishes a vendor's document. Both upstreams are MIT and carry their
  attribution. API Commons artifacts are CC BY-NC-SA 4.0 and code is Apache-2.0. "OpenAI"
  and "Anthropic" appear as factual references to the interfaces described, and nothing
  here implies endorsement.

tags:
  - Models
  - LLM
  - Inference
  - Artificial Intelligence

further_reading:
  - name: The adopters building block
    url: https://github.com/api-commons/adopters
    description: The schema behind both registries, and the evidence grades it enforces.
  - name: The adopter matrix — OpenAI
    url: https://github.com/api-commons/models/blob/main/adopters/openai-v1-matrix.md
    description: Operation by adopter, across everyone who publishes a spec.
---
