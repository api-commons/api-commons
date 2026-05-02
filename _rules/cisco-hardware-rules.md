---
api_specs:
- filename: openapiSpec
  format: yaml
  label: Cisco Meraki Dashboard API
  slug: meraki-dashboard-api
  spec_type: OpenAPI
  url: https://api.meraki.com/api/v1/openapiSpec
- filename: openapi.yaml
  format: yaml
  label: Cisco Intersight API
  slug: intersight-api
  spec_type: OpenAPI
  url: https://intersight.com/apidocs/downloads/
categories:
- cisco
description: Spectral linting rules defining API design standards and conventions for Cisco Hardware.
layout: rules
name: Cisco Hardware API Rules
provider_name: Cisco Hardware
provider_slug: cisco-hardware
rule_count: 6
rules:
- description: API info object MUST contain a contact for Cisco Hardware APIs.
  given: $.info
  name: cisco-hardware-info-contact
  severity: warn
- description: All Cisco Hardware API servers MUST use HTTPS.
  given: $.servers[*].url
  name: cisco-hardware-https-only
  severity: error
- description: Operations MUST be tagged for hardware domain grouping.
  given: $.paths[*][get,post,put,delete,patch].tags
  name: cisco-hardware-tag-required
  severity: warn
- description: Operations MUST have an operationId.
  given: $.paths[*][get,post,put,delete,patch]
  name: cisco-hardware-operation-id
  severity: error
- description: Operations MUST have a summary.
  given: $.paths[*][get,post,put,delete,patch]
  name: cisco-hardware-summary-required
  severity: warn
- description: API MUST define security schemes for token, basic-auth, or signature auth.
  given: $.components.securitySchemes
  name: cisco-hardware-security-required
  severity: error
rules_file: rules/cisco-hardware-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cisco-hardware/refs/heads/main/rules/cisco-hardware-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 3
slug: cisco-hardware-rules
source_filename: cisco-hardware-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n  - spectral:asyncapi\nrules:\n  cisco-hardware-info-contact:\n    description: API info object MUST contain a contact for Cisco Hardware APIs.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  cisco-hardware-https-only:\n    description: All Cisco Hardware API servers MUST use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  cisco-hardware-tag-required:\n    description: Operations MUST be tagged for hardware domain grouping.\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].tags\n    then:\n      function: truthy\n  cisco-hardware-operation-id:\n    description: Operations MUST have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  cisco-hardware-summary-required:\n    description:\
  \ Operations MUST have a summary.\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: summary\n      function: truthy\n  cisco-hardware-security-required:\n    description: API MUST define security schemes for token, basic-auth, or signature auth.\n    severity: error\n    given: $.components.securitySchemes\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cisco-hardware/refs/heads/main/rules/cisco-hardware-rules.yml
tags:
- Hardware
- Infrastructure
- Networking
- Routers
- Switches
- Spectral
- Linting
- API Governance
---
