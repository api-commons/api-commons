---
api_specs:
- filename: debian-sources-api-openapi.yml
  format: yaml
  label: Debian Sources API
  slug: debian-sources-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/debian/refs/heads/main/openapi/debian-sources-api-openapi.yml
- filename: debian-bts-api-openapi.yml
  format: yaml
  label: Debian Bug Tracking System
  slug: debian-bts-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/debian/refs/heads/main/openapi/debian-bts-api-openapi.yml
- filename: debian-udd-api-openapi.yml
  format: yaml
  label: Debian Ultimate Database (UDD)
  slug: debian-udd
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/debian/refs/heads/main/openapi/debian-udd-api-openapi.yml
categories:
- debian
description: Spectral linting rules defining API design standards and conventions for Debian.
layout: rules
name: Debian API Rules
provider_name: Debian
provider_slug: debian
rule_count: 5
rules:
- description: API info should declare the license used for served content.
  given: $.info
  name: debian-info-license
  severity: warn
- description: Servers should reference sources.debian.org.
  given: $.servers[*].url
  name: debian-sources-base-url
  severity: warn
- description: API should expose /list as a primary path for package discovery.
  given: $.paths
  name: debian-list-resource
  severity: warn
- description: API should expose /ping/ for health checks.
  given: $.paths
  name: debian-ping-resource
  severity: warn
- description: Operations should be tagged Sources, Copyright, or Patches.
  given: $.paths[*][*]
  name: debian-operation-tags
  severity: warn
rules_file: rules/debian-sources-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/debian/refs/heads/main/rules/debian-sources-api-rules.yml
severity_counts:
  error: 0
  hint: 0
  info: 0
  warn: 5
slug: debian-sources-api-rules
source_filename: debian-sources-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  debian-info-license:\n    description: API info should declare the license used for served content.\n    given: $.info\n    severity: warn\n    then:\n      field: license\n      function: truthy\n  debian-sources-base-url:\n    description: Servers should reference sources.debian.org.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"sources\\\\.debian\\\\.org\"\n  debian-list-resource:\n    description: API should expose /list as a primary path for package discovery.\n    given: $.paths\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/list\"\n  debian-ping-resource:\n    description: API should expose /ping/ for health checks.\n    given: $.paths\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/ping\"\n  debian-operation-tags:\n    description: Operations should\
  \ be tagged Sources, Copyright, or Patches.\n    given: $.paths[*][*]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/debian/refs/heads/main/rules/debian-sources-api-rules.yml
tags:
- Bug Tracker
- Debian
- Linux
- Open Source
- Operating System
- Package Management
- Source Code
- Spectral
- Linting
- API Governance
---
