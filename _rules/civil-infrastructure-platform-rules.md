---
categories:
- cip
description: Spectral linting rules defining API design standards and conventions for Civil Infrastructure Platform.
layout: rules
name: Civil Infrastructure Platform API Rules
provider_name: Civil Infrastructure Platform
provider_slug: civil-infrastructure-platform
rule_count: 5
rules:
- description: API info MUST contain a contact for the maintaining working group.
  given: $.info
  name: cip-info-contact
  severity: warn
- description: CIP-derived API descriptions SHOULD declare an open source license.
  given: $.info
  name: cip-info-license
  severity: warn
- description: API servers MUST use HTTPS.
  given: $.servers[*].url
  name: cip-https-only
  severity: error
- description: Operations MUST have an operationId.
  given: $.paths[*][get,post,put,delete,patch]
  name: cip-operation-id
  severity: error
- description: Operations MUST be tagged for working group grouping.
  given: $.paths[*][get,post,put,delete,patch].tags
  name: cip-tag-required
  severity: warn
rules_file: rules/civil-infrastructure-platform-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/civil-infrastructure-platform/refs/heads/main/rules/civil-infrastructure-platform-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 0
  warn: 3
slug: civil-infrastructure-platform-rules
source_filename: civil-infrastructure-platform-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  cip-info-contact:\n    description: API info MUST contain a contact for the maintaining working group.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  cip-info-license:\n    description: CIP-derived API descriptions SHOULD declare an open source license.\n    severity: warn\n    given: $.info\n    then:\n      field: license\n      function: truthy\n  cip-https-only:\n    description: API servers MUST use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  cip-operation-id:\n    description: Operations MUST have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  cip-tag-required:\n    description: Operations MUST be tagged for working group grouping.\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].tags\n\
  \    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/civil-infrastructure-platform/refs/heads/main/rules/civil-infrastructure-platform-rules.yml
tags:
- Embedded
- Industrial
- Infrastructure
- Linux
- Linux Foundation
- Long-Term Support
- Open Source
- Spectral
- Linting
- API Governance
---
