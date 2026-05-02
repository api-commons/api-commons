---
api_specs:
- filename: cisco-systems-cisco-api-openapi.yml
  format: yaml
  label: Cisco DevNet API Catalog
  slug: devnet-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-systems/refs/heads/main/openapi/cisco-systems-cisco-api-openapi.yml
- filename: openapiSpec
  format: yaml
  label: Cisco Meraki Dashboard
  slug: meraki
  spec_type: OpenAPI
  url: https://api.meraki.com/api/v1/openapiSpec
categories:
- cisco
description: Spectral linting rules defining API design standards and conventions for Cisco Systems.
layout: rules
name: Cisco Systems API Rules
provider_name: Cisco Systems
provider_slug: cisco-systems
rule_count: 6
rules:
- description: API info MUST contain a contact email or URL.
  given: $.info
  name: cisco-info-contact
  severity: warn
- description: All Cisco Systems API servers MUST use HTTPS.
  given: $.servers[*].url
  name: cisco-https-only
  severity: error
- description: Operations MUST have an operationId.
  given: $.paths[*][get,post,put,delete,patch]
  name: cisco-operation-id
  severity: error
- description: Operations MUST be tagged for product domain grouping.
  given: $.paths[*][get,post,put,delete,patch].tags
  name: cisco-tag-required
  severity: warn
- description: API MUST define security schemes.
  given: $.components.securitySchemes
  name: cisco-security-required
  severity: error
- description: API MUST declare at least one server URL.
  given: $.servers
  name: cisco-server-url
  severity: error
rules_file: rules/cisco-systems-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cisco-systems/refs/heads/main/rules/cisco-systems-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 2
slug: cisco-systems-rules
source_filename: cisco-systems-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  cisco-info-contact:\n    description: API info MUST contain a contact email or URL.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  cisco-https-only:\n    description: All Cisco Systems API servers MUST use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  cisco-operation-id:\n    description: Operations MUST have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  cisco-tag-required:\n    description: Operations MUST be tagged for product domain grouping.\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].tags\n    then:\n      function: truthy\n  cisco-security-required:\n    description: API MUST define security schemes.\n    severity: error\n    given: $.components.securitySchemes\n\
  \    then:\n      function: truthy\n  cisco-server-url:\n    description: API MUST declare at least one server URL.\n    severity: error\n    given: $.servers\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cisco-systems/refs/heads/main/rules/cisco-systems-rules.yml
tags:
- Collaboration
- Infrastructure
- Networking
- Security
- Spectral
- Linting
- API Governance
---
