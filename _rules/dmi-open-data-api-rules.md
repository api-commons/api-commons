---
api_specs:
- filename: dmi-open-data-api-openapi.yml
  format: yaml
  label: DMI Open Data API
  slug: dmi-open-data-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/danish-meteorological-institutes/refs/heads/main/openapi/dmi-open-data-api-openapi.yml
categories:
- dmi
description: Spectral linting rules defining API design standards and conventions for Danish Meteorological Institutes.
layout: rules
name: Danish Meteorological Institutes API Rules
provider_name: Danish Meteorological Institutes
provider_slug: danish-meteorological-institutes
rule_count: 5
rules:
- description: API info should publish a license, since DMI publishes under CC-BY 4.0.
  given: $.info
  name: dmi-info-license
  severity: warn
- description: Server URLs must include the /v2 version prefix.
  given: $.servers[*].url
  name: dmi-server-versioned
  severity: error
- description: Endpoints should reference the api-key security scheme.
  given: $.paths[*][*]
  name: dmi-apikey-security
  severity: warn
- description: GET item endpoints should return a FeatureCollection schema.
  given: $.paths[*].get.responses['200'].content['application/geo+json'].schema
  name: dmi-feature-collection-response
  severity: warn
- description: timeResolution parameters should be limited to hour/day/month/year.
  given: $.paths[*].get.parameters[?(@.name == 'timeResolution')].schema
  name: dmi-time-resolution-enum
  severity: warn
rules_file: rules/dmi-open-data-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/danish-meteorological-institutes/refs/heads/main/rules/dmi-open-data-api-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 4
slug: dmi-open-data-api-rules
source_filename: dmi-open-data-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  dmi-info-license:\n    description: API info should publish a license, since DMI publishes under CC-BY 4.0.\n    given: $.info\n    severity: warn\n    then:\n      field: license\n      function: truthy\n  dmi-server-versioned:\n    description: Server URLs must include the /v2 version prefix.\n    given: $.servers[*].url\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/v[0-9]+(/|$)\"\n  dmi-apikey-security:\n    description: Endpoints should reference the api-key security scheme.\n    given: $.paths[*][*]\n    severity: warn\n    then:\n      field: security\n      function: truthy\n  dmi-feature-collection-response:\n    description: GET item endpoints should return a FeatureCollection schema.\n    given: $.paths[*].get.responses['200'].content['application/geo+json'].schema\n    severity: warn\n    then:\n      field: $ref\n      function: truthy\n  dmi-time-resolution-enum:\n    description:\
  \ timeResolution parameters should be limited to hour/day/month/year.\n    given: $.paths[*].get.parameters[?(@.name == 'timeResolution')].schema\n    severity: warn\n    then:\n      field: enum\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/danish-meteorological-institutes/refs/heads/main/rules/dmi-open-data-api-rules.yml
tags:
- Climate
- Environment
- Lightning
- Meteorological
- Ocean
- Open Data
- Weather
- Spectral
- Linting
- API Governance
---
