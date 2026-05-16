---
name: Release Notes
description: A time-ordered, human-facing record of what shipped in each release — new features, deprecations, fixes, and migration guidance. Release notes are the consumer-facing companion to a change log; where a change log catalogs every commit-level change, release notes summarize the things consumers need to act on or celebrate. They are essential for any API with paying customers and for any team that wants to set explicit expectations about pace and stability.
image: /images/release-notes.png
url: '#'
machineReadable: false
source: commons
tags:
  - Lifecycle
  - Versioning
  - Communication
aliases:
  - Release Log
  - Releases
  - What's New
  - Updates
  - Product Updates
yaml_example: |
  - type: ReleaseNotes
    url: https://developers.example.com/releases

standards:
  - name: Semantic Versioning 2.0
    url: https://semver.org/spec/v2.0.0.html
    kind: Community
  - name: Keep a Changelog 1.1
    url: https://keepachangelog.com/en/1.1.0/
    kind: Community
  - name: Atom Syndication Format (RFC 4287)
    url: https://www.rfc-editor.org/rfc/rfc4287
    kind: IETF
  - name: schema.org Article
    url: https://schema.org/Article
    kind: Schema.org

link_relations:
  - rel: alternate
    spec: HTML Living Standard
    description: Used to point from release notes pages to their feed equivalents.
  - rel: prev / next
    spec: IANA Link Relations
    description: Paging between successive release entries.

openapi_expression:
  - field: info.version
    spec: OpenAPI 3.x
    description: Anchors each release-notes entry to a specific version of the spec.

risk:
  security_implications: Release notes for security fixes need coordinated-disclosure discipline — describing a vulnerability before patches are deployed can hand attackers a roadmap. Maintain a separate security-advisory channel for CVE-class fixes and link to it rather than describing exploitable details inline.
  compliance:
    - Customer notification requirements may apply to deprecations and breaking changes — keep dated, archived release notes for audit.

tools:
  - name: GitHub Releases
    url: https://docs.github.com/en/repositories/releasing-projects-on-github
    category: Releases tied to git tags
  - name: release-please
    url: https://github.com/googleapis/release-please
    license: Apache-2.0
    category: Automated release-notes generator
  - name: Conventional Changelog
    url: https://github.com/conventional-changelog/conventional-changelog
    license: ISC
    category: Generates notes from conventional-commits history
  - name: Bump.sh
    url: https://bump.sh/
    category: Spec-diff release notes for API providers

metrics:
  - name: release_cadence
    description: Median time between published release-notes entries.
  - name: breaking_change_count
    description: Number of breaking-change entries per quarter — a stability indicator.
  - name: notes_to_deprecation_lead_time
    description: Days between a deprecation being announced in release notes and the affected feature being removed.

examples:
  - provider: Stripe
    url: https://stripe.com/docs/upgrades
    note: Versioned API changes published per release with migration guidance.
  - provider: GitHub
    url: https://github.blog/changelog/
    note: Public changelog for the GitHub platform, including REST and GraphQL APIs.
  - provider: Twilio
    url: https://www.twilio.com/docs/release-notes
    note: Per-product release notes across the Twilio suite.

related_properties:
  - change-log
  - versioning
  - deprecation-policy
  - road-map
---
