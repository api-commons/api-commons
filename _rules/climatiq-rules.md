---
api_specs:
- filename: climatiq-openapi.yml
  format: yaml
  label: Climatiq API
  slug: climatiq-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/climatiq/refs/heads/main/openapi/climatiq-openapi.yml
categories:
- climatiq
description: Spectral linting rules defining API design standards and conventions for Climatiq.
layout: rules
name: Climatiq API Rules
provider_name: Climatiq
provider_slug: climatiq
rule_count: 6
rules:
- description: API info MUST contain a contact email or URL.
  given: $.info
  name: climatiq-info-contact
  severity: warn
- description: All Climatiq API servers MUST use HTTPS.
  given: $.servers[*].url
  name: climatiq-https-only
  severity: error
- description: Operations MUST have an operationId.
  given: $.paths[*][get,post,put,delete,patch]
  name: climatiq-operation-id
  severity: error
- description: Operations MUST be tagged for product-domain grouping (Search, Estimate, Travel, Freight, Energy, Computing, Procurement, Autopilot, Classifications, CBAM).
  given: $.paths[*][get,post,put,delete,patch].tags
  name: climatiq-tag-required
  severity: warn
- description: API MUST define a bearer-token security scheme since Climatiq authenticates with API keys passed as Bearer tokens.
  given: $.components.securitySchemes
  name: climatiq-bearer-auth-required
  severity: error
- description: API MUST declare at least one server URL (api.climatiq.io).
  given: $.servers
  name: climatiq-server-url
  severity: error
rules_file: rules/climatiq-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/climatiq/refs/heads/main/rules/climatiq-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 2
slug: climatiq-rules
source_filename: climatiq-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  climatiq-info-contact:\n    description: API info MUST contain a contact email or URL.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  climatiq-https-only:\n    description: All Climatiq API servers MUST use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  climatiq-operation-id:\n    description: Operations MUST have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  climatiq-tag-required:\n    description: Operations MUST be tagged for product-domain grouping (Search, Estimate, Travel, Freight, Energy, Computing, Procurement, Autopilot, Classifications, CBAM).\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].tags\n    then:\n      function: truthy\n  climatiq-bearer-auth-required:\n\
  \    description: API MUST define a bearer-token security scheme since Climatiq authenticates with API keys passed as Bearer tokens.\n    severity: error\n    given: $.components.securitySchemes\n    then:\n      function: truthy\n  climatiq-server-url:\n    description: API MUST declare at least one server URL (api.climatiq.io).\n    severity: error\n    given: $.servers\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/climatiq/refs/heads/main/rules/climatiq-rules.yml
tags:
- Carbon Accounting
- Carbon Emissions
- Climate
- Energy
- Environment
- GHG Protocol
- Sustainability
- Spectral
- Linting
- API Governance
---
