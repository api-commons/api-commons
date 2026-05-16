---
name: Status Page
description: A status page provides API consumers with real-time information regarding the up-time and availability of each API being made available. Status pages often provide current as well as historical information regarding stability or outages, helping build trust with consumers over time regarding the health of an API platform.
image: /images/status-page.png
url: '#'
machineReadable: false
source: concept
tags:
  - Status
  - Health
  - Reliability
aliases:
  - Health Page
  - Uptime
  - Incidents
yaml_example: |
  - type: StatusPage
    url: https://status.example.com/

standards:
  - name: RFC 4287 — The Atom Syndication Format
    url: https://www.rfc-editor.org/rfc/rfc4287
    kind: IETF
  - name: RFC 5005 — Feed Paging and Archiving (Atom)
    url: https://www.rfc-editor.org/rfc/rfc5005
    kind: IETF
  - name: RFC 3339 — Date and Time on the Internet — Timestamps
    url: https://www.rfc-editor.org/rfc/rfc3339
    kind: IETF
  - name: RSS 2.0 Specification
    url: https://www.rssboard.org/rss-specification
    kind: Community spec
  - name: JSON Feed v1.1
    url: https://www.jsonfeed.org/version/1.1/
    kind: Community spec
  - name: Atlassian Statuspage API
    url: https://developer.statuspage.io/
    kind: Vendor
  - name: Cachet (open-source status page)
    url: https://github.com/cachethq/cachet
    kind: Open source
  - name: Health Check Response Format for HTTP APIs (draft-inadarei-api-health-check)
    url: https://datatracker.ietf.org/doc/draft-inadarei-api-health-check/
    kind: IETF (expired draft)

headers:
  - name: Cache-Control
    direction: response
    spec: RFC 9111
    description: Status payloads are typically short-cached so dashboards refresh quickly.
  - name: Last-Modified
    direction: response
    spec: RFC 9110 §8.8.2
    description: Indicates the last time the status payload changed.

media_types:
  - type: application/atom+xml
    spec: RFC 4287
    note: Common feed format for incident histories.
  - type: application/rss+xml
    spec: RSS 2.0
    note: Widely used for incident feeds.
  - type: application/feed+json
    spec: JSON Feed v1.1
  - type: application/health+json
    spec: draft-inadarei-api-health-check
    note: Health-check response document for HTTP APIs.

well_known:
  - path: /.well-known/health
    spec: De facto
    description: Common convention for service health endpoints (no IANA registration).

openapi_expression:
  - field: servers
    spec: OpenAPI 3.x
    description: A status API can be documented as its own OpenAPI document alongside the product API.
  - field: paths./health
    spec: De facto
    description: Conventional path for a machine-readable health endpoint.

governance_rules:
  - id: naftiko-status-page
    source: Naftiko Sandbox (status-page/*.yml)
    description: Rules that verify each API references a status page and exposes machine-readable feeds.

risk:
  compliance:
    - SOC 2 A1.2 — environmental and operational monitoring communicated to users
    - ISO/IEC 27001 A.17 — information-security aspects of business continuity
  security_implications: Status pages should not leak internal infrastructure detail (host names, internal component IDs, stack traces) in incident write-ups. They are also a high-trust channel; compromise of the status page can be used for social engineering, so apply the same auth, change-management, and integrity controls as the primary API.

tools:
  - name: Atlassian Statuspage
    url: https://www.atlassian.com/software/statuspage
    category: Hosted
  - name: Cachet
    url: https://github.com/cachethq/cachet
    license: BSD-3-Clause
    category: Self-hosted
  - name: Instatus
    url: https://instatus.com/
    category: Hosted
  - name: Better Stack (Better Uptime)
    url: https://betterstack.com/better-uptime
    category: Hosted
  - name: Upptime
    url: https://upptime.js.org/
    license: MIT
    category: Self-hosted (GitHub Actions)
  - name: Gatus
    url: https://github.com/TwiN/gatus
    license: Apache-2.0
    category: Self-hosted

metrics:
  - name: uptime_percentage
    description: Rolling availability across a defined window (e.g. 30/90/365 days).
  - name: mttr_minutes
    description: Mean time to recover from declared incidents.
  - name: mttd_minutes
    description: Mean time to detect / declare an incident from first impact.
  - name: incident_count
    description: Declared incidents per period, segmented by severity.
  - name: component_availability
    description: Per-component uptime; aligns with Statuspage component model.

examples:
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: githubstatus.com with component-level status and RSS/Atom incident feeds.
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: status.stripe.com with per-product components and historical uptime.
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: status.twilio.com powered by Statuspage with regional component breakdown.
  - provider: Cloudflare
    url: https://providers.apis.io/providers/cloudflare/
    note: www.cloudflarestatus.com with PoP-level component reporting.

related_properties:
  - rate-limits
  - error-codes
  - deprecation-policy
  - lifecycle
  - support
---
