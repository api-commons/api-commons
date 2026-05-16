---
name: Change Log
description: Communicating change is important for any API provider, and having a simple and up-to-date log of what has changed is a great way to make change self-service. Your change log doesn't have to be verbose, but should be accurate and provide as much useful detail for consumers as possible.
image: /images/change-log.png
url: '#'
machineReadable: true
source: commons
tags:
  - Change Log
  - Versioning
  - Communication
aliases:
  - Changelog
  - Release Notes
  - What's New
  - Updates
yaml_example: |
  - type: ChangeLog
    url: https://developers.example.com/changelog

standards:
  - name: Keep a Changelog 1.1.0
    url: https://keepachangelog.com/en/1.1.0/
    kind: De facto
  - name: Conventional Commits 1.0.0
    url: https://www.conventionalcommits.org/en/v1.0.0/
    kind: De facto
  - name: Semantic Versioning 2.0.0
    url: https://semver.org/spec/v2.0.0.html
    kind: SemVer
  - name: Schema.org releaseNotes
    url: https://schema.org/releaseNotes
    kind: Schema.org
  - name: RSS 2.0
    url: https://www.rssboard.org/rss-specification
    kind: RSS Advisory Board
  - name: RFC 4287 — Atom Syndication Format
    url: https://www.rfc-editor.org/rfc/rfc4287
    kind: IETF
  - name: OpenAPI Specification 3.1
    url: https://spec.openapis.org/oas/v3.1.0
    kind: OpenAPI Initiative

headers:
  - name: Deprecation
    direction: response
    spec: RFC 9745
    description: Signals that a resource is deprecated, with a timestamp.
  - name: Sunset
    direction: response
    spec: RFC 8594
    description: Signals the date a resource will become unresponsive.
  - name: Link
    direction: response
    spec: RFC 8288
    description: With `rel=sunset` or `rel=deprecation`, points to the changelog entry.

media_types:
  - type: text/markdown
    spec: RFC 7763
    note: CHANGELOG.md is the canonical form.
  - type: application/rss+xml
    note: Changelog feed for subscribers.
  - type: application/atom+xml
    spec: RFC 4287

openapi_expression:
  - field: info.version
    spec: OpenAPI 3.x
    description: SemVer string of the API description; the anchor entries are tied to.
  - field: deprecated
    spec: OpenAPI 3.x
    description: Operation- or parameter-level deprecation flag referenced from changelog entries.
  - field: info.x-api-lifecycle
    spec: Common vendor extension
    description: Lifecycle stage (alpha/beta/stable/deprecated) — frequently surfaced in the changelog.

link_relations:
  - rel: alternate
    spec: HTML / RFC 8288
    description: Used to advertise an RSS/Atom feed of changelog entries.
  - rel: sunset
    spec: RFC 8594
    description: Points to documentation (often the changelog entry) explaining a sunset.
  - rel: deprecation
    spec: RFC 9745
    description: Points to documentation for a deprecated resource.

governance_rules:
  - id: info-version
    source: Spectral built-in
    description: "`info.version` must be set so changelog entries can be anchored to a release."
  - id: oas-version-bump-on-breaking
    source: House rule
    description: Breaking changes must bump the major version (SemVer) and produce a changelog entry.
  - id: deprecated-operations-changelog
    source: House rule
    description: "Operations flagged `deprecated: true` must have a corresponding changelog entry and Sunset/Deprecation headers."

risk:
  security_implications: Changelogs that disclose CVE-adjacent fixes before coordinated release can expose unpatched consumers; pair security-relevant entries with advisory channels. Conversely, silent breaking changes undermine trust and can trigger outage post-mortems against the provider.
  compliance:
    - Contract / SLA — material API changes often require advance notice
    - Privacy regulations (GDPR Art. 13/14) — material changes to data handling require user notification

tools:
  - name: semantic-release
    url: https://semantic-release.gitbook.io/
    license: MIT
    category: Release automation
  - name: Conventional Changelog
    url: https://github.com/conventional-changelog/conventional-changelog
    license: ISC
    category: Changelog generator
  - name: release-please
    url: https://github.com/googleapis/release-please
    license: Apache-2.0
    category: Release automation
  - name: Bump.sh
    url: https://bump.sh/
    category: API diff and changelog
  - name: oasdiff
    url: https://www.oasdiff.com/
    license: Apache-2.0
    category: OpenAPI diff
  - name: Optic
    url: https://www.useoptic.com/
    category: API diff and governance

metrics:
  - name: releases_per_quarter
    description: Number of versioned releases captured in the changelog.
  - name: breaking_changes_per_release
    description: Count of entries flagged as breaking in each release.
  - name: deprecation_lead_time_days
    description: Days between a deprecation entry and the corresponding sunset.
  - name: changelog_freshness_days
    description: Days between the latest API change and its changelog entry.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Dated API versions paired with prose upgrade guides per change.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: Platform-wide changelog with RSS feed and category filters.
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: Per-product changelog feeds aligned with SDK release notes.
  - provider: Shopify
    url: https://providers.apis.io/providers/shopify/
    note: Quarterly API versions with detailed release notes per version.

related_properties:
  - road-map
  - deprecation
  - blog
  - openapi
  - versioning
---
