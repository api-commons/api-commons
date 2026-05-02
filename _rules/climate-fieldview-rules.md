---
api_specs:
- filename: climate-fieldview-platform-openapi.yml
  format: yaml
  label: Climate FieldView Platform API
  slug: fieldview-platform-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/climate-fieldview/refs/heads/main/openapi/climate-fieldview-platform-openapi.yml
categories:
- climate
description: Spectral linting rules defining API design standards and conventions for Climate FieldView.
layout: rules
name: Climate FieldView API Rules
provider_name: Climate FieldView
provider_slug: climate-fieldview
rule_count: 6
rules:
- description: API info MUST contain a contact email or URL.
  given: $.info
  name: climate-fieldview-info-contact
  severity: warn
- description: All Climate FieldView API servers MUST use HTTPS.
  given: $.servers[*].url
  name: climate-fieldview-https-only
  severity: error
- description: Operations MUST have an operationId.
  given: $.paths[*][get,post,put,delete,patch]
  name: climate-fieldview-operation-id
  severity: error
- description: Operations MUST be tagged for agronomic-domain grouping (Fields, Planting, Harvest, Application, Soil Sampling).
  given: $.paths[*][get,post,put,delete,patch].tags
  name: climate-fieldview-tag-required
  severity: warn
- description: API MUST define an OAuth2 security scheme since FieldView authenticates with OAuth 2.0 authorization-code grant.
  given: $.components.securitySchemes
  name: climate-fieldview-oauth2-required
  severity: error
- description: API MUST declare at least one server URL pointing at api.climate.com.
  given: $.servers
  name: climate-fieldview-server-url
  severity: error
rules_file: rules/climate-fieldview-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/climate-fieldview/refs/heads/main/rules/climate-fieldview-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 2
slug: climate-fieldview-rules
source_filename: climate-fieldview-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  climate-fieldview-info-contact:\n    description: API info MUST contain a contact email or URL.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  climate-fieldview-https-only:\n    description: All Climate FieldView API servers MUST use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  climate-fieldview-operation-id:\n    description: Operations MUST have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  climate-fieldview-tag-required:\n    description: Operations MUST be tagged for agronomic-domain grouping (Fields, Planting, Harvest, Application, Soil Sampling).\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].tags\n    then:\n      function: truthy\n  climate-fieldview-oauth2-required:\n\
  \    description: API MUST define an OAuth2 security scheme since FieldView authenticates with OAuth 2.0 authorization-code grant.\n    severity: error\n    given: $.components.securitySchemes\n    then:\n      function: truthy\n  climate-fieldview-server-url:\n    description: API MUST declare at least one server URL pointing at api.climate.com.\n    severity: error\n    given: $.servers\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/climate-fieldview/refs/heads/main/rules/climate-fieldview-rules.yml
tags:
- Agriculture
- Bayer
- Crop Data
- Field Boundaries
- Harvest
- OAuth2
- Planting
- Precision Ag
- Spectral
- Linting
- API Governance
---
