---
name: Road Map
description: Providing visibility as far into the future as possible is a common trait of successful APIs. Maintaining, publishing, and consistently communicating around a road map helps bring alignment between API producer and consumers, providing an essential building block for managing change across any platform.
image: /images/road-map.png
url: '#'
machineReadable: true
source: commons
tags:
  - SDKs
aliases:
  - Roadmap
  - Product Roadmap
  - Upcoming
yaml_example: |
  - type: RoadMap
    url: https://developers.example.com/roadmap

standards:
  - name: schema.org CreativeWork
    url: https://schema.org/CreativeWork
    kind: schema.org
    note: No dedicated Roadmap type — providers typically model items as Article or ItemList of planned work.
  - name: RFC 8594 — Sunset HTTP Header
    url: https://www.rfc-editor.org/rfc/rfc8594
    kind: IETF
    note: Companion to a public roadmap when retiring endpoints.
  - name: IANA Link Relation — deprecation
    url: https://www.iana.org/assignments/link-relations/link-relations.xhtml
    kind: IANA
  - name: OpenAPI Specification — deprecated flag
    url: https://spec.openapis.org/oas/latest.html
    kind: OAI

headers:
  - name: Sunset
    direction: response
    spec: RFC 8594
    description: HTTP-date when the resource will become unresponsive — a roadmap signal at the protocol level.
  - name: Deprecation
    direction: response
    spec: draft-ietf-httpapi-deprecation-header
    description: Indicates a resource is deprecated, often paired with a roadmap link.

link_relations:
  - rel: deprecation
    spec: IANA (registered alongside the Deprecation header work)
  - rel: sunset
    spec: RFC 8594

openapi_expression:
  - field: paths.*.deprecated
    spec: OpenAPI 3.x
    description: Operation-level deprecation flag — roadmap items often correspond to operations being deprecated.
  - field: info.x-roadmap
    spec: Vendor extension (no formal spec)
    description: Some providers expose a roadmap URL via an x- extension.

governance_rules:
  - id: oas-operation-deprecated
    source: Spectral (custom)
    description: Deprecated operations should link to roadmap or migration guidance.

risk:
  security_implications: Public roadmaps can leak competitive intent or signal future attack surface (e.g., upcoming beta endpoints). Most providers publish themes and quarters rather than dated commitments.

tools:
  - name: ProductBoard
    url: https://www.productboard.com/
    category: Roadmap management
  - name: Aha!
    url: https://www.aha.io/
    category: Roadmap management
  - name: GitHub Projects
    url: https://docs.github.com/en/issues/planning-and-tracking-with-projects
    category: Public roadmap board
  - name: Linear
    url: https://linear.app/
    category: Issue / roadmap tool
  - name: Canny
    url: https://canny.io/
    category: Public roadmap + feedback

metrics:
  - name: roadmap_items_shipped_per_quarter
    description: Count of public roadmap items moved to released state per quarter.
  - name: roadmap_slip_rate
    description: Share of items that miss their stated quarter or window.
  - name: feedback_to_roadmap_ratio
    description: Share of inbound feature requests that result in a public roadmap entry.

examples:
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: Public roadmap maintained as a GitHub Projects board.
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Versioned API changelog plus targeted previews instead of a long-horizon roadmap.
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: Product changelogs and deprecation notices feed roadmap visibility.

related_properties:
  - change-log
  - deprecation
  - versioning
  - releases
  - status
---
