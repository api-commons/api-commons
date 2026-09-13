---
name: Open Data
description: >-
  Nobody ratified CKAN's Action API as the open-data standard. It became one because
  government after government installed the same software, and a client written against one
  national portal now works against hundreds of city, state and research catalogues by
  changing a hostname. This is the only profile in the programme authored rather than
  derived — CKAN publishes no machine-readable specification of its own API.
cohort: version-drift — the same software at releases spanning years, not independent reimplementations
status: Published — 134 actions graded from 36 live portal probes across 30 CKAN releases
repository: https://github.com/api-commons/open-data
image: /images/api-commons-icon.png

profiles:

  - name: The CKAN Action API
    standard_id: ckan-action-v3
    originator: CKAN
    description: >-
      63 core actions, measured by calling 36 live government portals.
      The interesting number is not the count but the gradient across releases.
    source:
      name: ckan/ckan — ckan/logic/action/*.py
      url: https://github.com/ckan/ckan
      license: AGPL-3.0 (the software)
      pinned: 0731a7a4ab76dd11889eb89a892b3feae4fd69a8
      note: >-
        134 actions, 65 of them reads.
        CKAN publishes no machine-readable specification, so the action list is enumerated
        from its own source. The AGPL governs the code, not a description of the HTTP surface
        it serves.
    measurement: >-
      Never from our own catalog. Counting how often each action appears across our harvested
      artifacts gives status_show 81% and package_search 14% — a number that measures our
      harvester, which fingerprints portals by calling status_show. Instead 48 portals were
      probed read-only and 36 produced usable results. Every portal gets two
      controls: an action that cannot exist, and status_show, which every CKAN release has.
      The second is necessary because catalog.data.gov answers 404 to everything and would
      otherwise read as a portal implementing nothing.
    tiers:
      - name: Core
        count: 63
        description: >-
          Served by a majority of probed portals. status_show and organization_list_for_user
          reach 100%; package_search and package_list sit at 72.2% and 61.1%, because the
          oldest installs predate parts of the surface.
      - name: Extended
        count: 2
        description: >-
          Only two actions land between 5% and 50% — organization_followee_count and
          user_show. On this cohort divergence is a version gradient rather than a spread of
          choices, so the middle band is nearly empty by nature.
      - name: Vendor
        count: 69
        description: >-
          Under 5%, or not probed. Every write action is here: the probe runs anonymously
          against public-sector servers and never calls create, update, delete or patch.
    adopters:
      count: 48
      as_of: '2026-09-13'
      url: https://github.com/api-commons/open-data/blob/main/adopters/ckan-action-v3.yml
      matrix_url: https://github.com/api-commons/open-data/blob/main/adopters/ckan-action-v3-matrix.md
      evidence:
        - grade: tested
          count: 36
          description: >-
            The actions were called against a live portal. 6 serve the whole core
            tier; the rest serve part of it, which on this cohort usually means an older CKAN.
        - grade: prose
          count: 12
          description: >-
            Could not be probed — unreachable, refused at the edge, or unable to distinguish a
            present action from an absent one. No tier is recorded for any of them.
    apis:
      - name: OpenAPI
        description: One path per action, x-tier on each, and the shared response envelope.
        properties:
          - type: OpenAPI
            url: https://raw.githubusercontent.com/api-commons/open-data/main/standard/ckan-action-v3/openapi.yml
      - name: Profile
        description: All 134 actions with tier, probe evidence and the status breakdown behind each.
        properties:
          - type: Profile
            url: https://raw.githubusercontent.com/api-commons/open-data/main/standard/ckan-action-v3/profile.yml
      - name: Spectral Ruleset
        description: Generated from the profile — 63 core-action rules plus two hygiene rules.
        properties:
          - type: SpectralRules
            url: https://raw.githubusercontent.com/api-commons/open-data/main/standard/ckan-action-v3/spectral/ckan-profile.yaml
      - name: Arazzo
        description: status_show, then package_search, then package_show on the first result.
        properties:
          - type: Arazzo
            url: https://raw.githubusercontent.com/api-commons/open-data/main/standard/ckan-action-v3/arazzo/core-conformance.yml
      - name: MCP Tools
        description: MCP tool definitions for the core tier.
        properties:
          - type: MCP
            url: https://raw.githubusercontent.com/api-commons/open-data/main/standard/ckan-action-v3/mcp/tools.json

licensing: >-
  The profile is authored from CKAN's own source and from live observation; it copies no
  document. CKAN the software is AGPL-3.0, which governs the code rather than a description
  of the HTTP surface it serves. API Commons artifacts are CC BY-NC-SA 4.0 and code is
  Apache-2.0. Nothing here implies endorsement by CKAN, by the Open Knowledge Foundation, or
  by any portal named in the registry.

tags:
  - Open Data
  - Government
  - Data

further_reading:
  - name: Support by CKAN release
    url: https://github.com/api-commons/open-data/blob/main/adopters/ckan-action-v3-matrix.md
    description: >-
      The version gradient, which is what this cohort exists to show — 2.2b serves 42 of the
      63 core actions and 2.9.11 serves all 63.
  - name: The adopters building block
    url: https://github.com/api-commons/adopters
    description: The schema behind the registry, and the software_version field this cohort needs.
---
