---
api_specs:
- filename: country-state-city-api-openapi.yml
  format: yaml
  label: Country State City API
  slug: country-state-city-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/country-state-city-api/refs/heads/main/openapi/country-state-city-api-openapi.yml
categories:
- csc
description: Spectral linting rules defining API design standards and conventions for Country State City API.
layout: rules
name: Country State City API API Rules
provider_name: Country State City API
provider_slug: country-state-city-api
rule_count: 7
rules:
- description: API title must mention Country State City.
  given: $.info.title
  name: csc-info-title
  severity: error
- description: Servers must reference https://api.countrystatecity.in/v1.
  given: $.servers[*].url
  name: csc-server-base-url
  severity: warn
- description: Spec must define an X-CSCAPI-KEY API key security scheme.
  given: $.components.securitySchemes
  name: csc-api-key-security
  severity: error
- description: API must apply the API key security globally.
  given: $
  name: csc-global-security
  severity: warn
- description: Every operation must define an operationId.
  given: $.paths.*.get
  name: csc-operation-id
  severity: error
- description: Every operation must define at least one tag.
  given: $.paths.*.get
  name: csc-operation-tags
  severity: error
- description: All authenticated operations should document a 401 response.
  given: $.paths.*.get.responses
  name: csc-401-response
  severity: warn
rules_file: rules/country-state-city-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/country-state-city-api/refs/heads/main/rules/country-state-city-api-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 3
slug: country-state-city-api-rules
source_filename: country-state-city-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [\"spectral:oas\"]\ndocumentationUrl: https://docs.countrystatecity.in/api/introduction\nrules:\n  csc-info-title:\n    description: API title must mention Country State City.\n    given: \"$.info.title\"\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"Country State City\"\n  csc-server-base-url:\n    description: Servers must reference https://api.countrystatecity.in/v1.\n    given: \"$.servers[*].url\"\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"api.countrystatecity.in\"\n  csc-api-key-security:\n    description: Spec must define an X-CSCAPI-KEY API key security scheme.\n    given: \"$.components.securitySchemes\"\n    severity: error\n    then:\n      field: ApiKeyAuth\n      function: truthy\n  csc-global-security:\n    description: API must apply the API key security globally.\n    given: \"$\"\n    severity: warn\n    then:\n      field: security\n      function:\
  \ truthy\n  csc-operation-id:\n    description: Every operation must define an operationId.\n    given: \"$.paths.*.get\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n  csc-operation-tags:\n    description: Every operation must define at least one tag.\n    given: \"$.paths.*.get\"\n    severity: error\n    then:\n      field: tags\n      function: truthy\n  csc-401-response:\n    description: All authenticated operations should document a 401 response.\n    given: \"$.paths.*.get.responses\"\n    severity: warn\n    then:\n      field: '401'\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/country-state-city-api/refs/heads/main/rules/country-state-city-api-rules.yml
tags:
- Capitals
- Cities
- Countries
- Currencies
- Geography
- Geolocation
- ISO 3166
- JSON
- Phone Codes
- Provinces
- Reference Data
- Regions
- States
- Time Zones
- Spectral
- Linting
- API Governance
---
