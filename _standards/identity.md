---
name: Identity
description: >-
  SCIM is the odd one out in this programme, and that is why it is here. The other five
  standards became standards by being copied, so a profile is the only specification they
  have. SCIM was ratified in 2015 — describing it again would add nothing. What was missing
  is the measurement beside it: what RFC 7644 says about each operation, quoted, against what
  the industry actually built.
cohort: reimplementation — independent servers built against a published specification
status: Published — 24 operations graded on two axes, 320 adopters recorded
repository: https://github.com/api-commons/identity
image: /images/api-commons-icon.png

profiles:

  - name: SCIM 2.0
    standard_id: scim-2.0
    originator: IETF
    description: >-
      The measured core is five operations, all of them on /Users. Group management does not
      reach it, and PATCH misses by a single point.
    source:
      name: RFC 7643 (Core Schema) and RFC 7644 (Protocol)
      url: https://www.rfc-editor.org/rfc/rfc7644
      license: IETF Trust — quoted with section, not reproduced
      pinned: September 2015
      note: >-
        Operations transcribed from RFC 7644 Section 3.2 Table 2. Every normative claim on this
        page is quoted from the RFC text with its section rather than paraphrased from memory.
    measurement: >-
      Two gradings per operation. One is what the RFC says; the other is what the industry
      declares, measured the same way as every other profile here. 368 providers
      mention SCIM — the largest claim cohort in the programme — and 77 publish an
      OpenAPI containing a SCIM path, which is the denominator. No tested grade is possible:
      every SCIM operation is authenticated, so there is no anonymous discriminator, the same
      structural limit S3 has.
    tiers:
      - name: Core
        count: 5
        description: >-
          GET and POST /Users at 68.8% and 67.5%, then GET, PUT and DELETE on /Users/&#123;id&#125;.
          Five operations, all on /Users. GET /Groups reaches only 45.5% — barely two-thirds
          the rate of GET /Users — so a client that provisions users can rely on this surface
          and one that also manages group membership cannot.
      - name: Extended
        count: 12
        description: >-
          PATCH /Users/&#123;id&#125; at 49.4%, missing the core by one point, which is notable
          because PATCH is what an identity provider uses on every attribute update. Then the
          Groups surface and the three discovery endpoints at roughly a third each.
      - name: Vendor
        count: 7
        description: >-
          /Me, /Bulk and /.search — defined by the RFC and declared by one or two providers
          apiece. The specification anticipated uses the field did not take up.
    adopters:
      count: 320
      as_of: '2026-09-14'
      url: https://github.com/api-commons/identity/blob/main/adopters/scim-2.0.yml
      matrix_url: https://github.com/api-commons/identity/blob/main/adopters/scim-2.0-matrix.md
      evidence:
        - grade: declared
          count: 51
          description: >-
            Publishes an OpenAPI declaring an operation from RFC 7644 Table 2. Note that 77
            publish a SCIM path but only these map to the standard surface — the rest publish
            something SCIM-shaped that does not.
        - grade: prose
          count: 269
          description: Mentions SCIM and publishes nothing a reader can check against.
        - grade: tested
          count: 0
          description: >-
            Structurally unavailable. Every SCIM operation is authenticated, so an anonymous
            caller learns nothing about which operations exist.
    apis:
      - name: OpenAPI
        description: >-
          The artifact of record. SCIM is the only standard in this programme that OpenAPI
          describes cleanly — ordinary REST with real paths, and it lints clean under spectral:oas.
        properties:
          - type: OpenAPI
            url: https://raw.githubusercontent.com/api-commons/identity/main/standard/scim-2.0/openapi.yml
      - name: Profile
        description: All 24 operations with their RFC citation, normative force and measured tier.
        properties:
          - type: Profile
            url: https://raw.githubusercontent.com/api-commons/identity/main/standard/scim-2.0/profile.yml
      - name: Spectral Ruleset
        description: >-
          Measured core as errors, discovery as a warning — because the RFC compels one and not
          the other. Plus the two mistakes that break generated clients.
        properties:
          - type: SpectralRules
            url: https://raw.githubusercontent.com/api-commons/identity/main/standard/scim-2.0/spectral/scim-profile.yaml
      - name: Arazzo
        description: Discover, create, read, delete — and it keeps going when discovery fails.
        properties:
          - type: Arazzo
            url: https://raw.githubusercontent.com/api-commons/identity/main/standard/scim-2.0/arazzo/core-conformance.yml
      - name: MCP Tools
        description: MCP tool definitions for the measured core.
        properties:
          - type: MCP
            url: https://raw.githubusercontent.com/api-commons/identity/main/standard/scim-2.0/mcp/tools.json

licensing: >-
  RFC 7643 and RFC 7644 are IETF Standards Track documents. This profile quotes their normative
  language with section references and does not reproduce them. API Commons artifacts are CC
  BY-NC-SA 4.0 and code is Apache-2.0. Nothing here implies endorsement by the IETF or by any
  provider named in the registry.

tags:
  - Identity
  - SCIM
  - Provisioning

further_reading:
  - name: Why discovery is optional
    url: https://www.rfc-editor.org/rfc/rfc7644#section-4
    description: >-
      RFC 7644 Section 4 introduces the three discovery endpoints with "MAY be retrieved using
      HTTP GET" and uses SHALL only for the shape of a response. There is no obligation to
      implement them, which makes the third of the field that declares them a specification
      outcome rather than a compliance failure.
  - name: The adopters building block
    url: https://github.com/api-commons/adopters
    description: The schema behind the registry, and the evidence grades it enforces.
---
