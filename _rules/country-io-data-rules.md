---
api_specs:
- filename: country-io-data-openapi.yml
  format: yaml
  label: Country.io Data API
  slug: country-io-data-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/country-io/refs/heads/main/openapi/country-io-data-openapi.yml
categories:
- country
description: Spectral linting rules defining API design standards and conventions for Country.io.
layout: rules
name: Country.io API Rules
provider_name: Country.io
provider_slug: country-io
rule_count: 7
rules:
- description: API title must mention Country.io.
  given: $.info.title
  name: country-io-info-title
  severity: error
- description: Servers must reference https://country.io.
  given: $.servers[*].url
  name: country-io-server
  severity: warn
- description: All Country.io data paths must end in .json.
  given: $.paths
  name: country-io-paths-json
  severity: error
- description: Country.io data endpoints must only support GET.
  given: $.paths.*
  name: country-io-get-only
  severity: error
- description: Operations must define an operationId.
  given: $.paths.*.get
  name: country-io-operation-id
  severity: error
- description: Operations must define at least one tag.
  given: $.paths.*.get
  name: country-io-tags
  severity: error
- description: Each endpoint must define a 200 application/json response.
  given: $.paths.*.get.responses.200.content
  name: country-io-200-json-response
  severity: error
rules_file: rules/country-io-data-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/country-io/refs/heads/main/rules/country-io-data-rules.yml
severity_counts:
  error: 6
  hint: 0
  info: 0
  warn: 1
slug: country-io-data-rules
source_filename: country-io-data-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [\"spectral:oas\"]\ndocumentationUrl: https://country.io/data/\nrules:\n  country-io-info-title:\n    description: API title must mention Country.io.\n    given: \"$.info.title\"\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"Country.io\"\n  country-io-server:\n    description: Servers must reference https://country.io.\n    given: \"$.servers[*].url\"\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"country.io\"\n  country-io-paths-json:\n    description: All Country.io data paths must end in .json.\n    given: \"$.paths\"\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          patternProperties:\n            \"^/[a-z0-9_-]+\\\\.json$\": {}\n          additionalProperties: false\n  country-io-get-only:\n    description: Country.io data endpoints must only support GET.\n    given: \"$.paths.*\"\
  \n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            get:\n              type: object\n          additionalProperties: false\n  country-io-operation-id:\n    description: Operations must define an operationId.\n    given: \"$.paths.*.get\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n  country-io-tags:\n    description: Operations must define at least one tag.\n    given: \"$.paths.*.get\"\n    severity: error\n    then:\n      field: tags\n      function: truthy\n  country-io-200-json-response:\n    description: Each endpoint must define a 200 application/json response.\n    given: \"$.paths.*.get.responses.200.content\"\n    severity: error\n    then:\n      field: application/json\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/country-io/refs/heads/main/rules/country-io-data-rules.yml
tags:
- Capitals
- Continents
- Countries
- Currencies
- Currency Codes
- Dialing Codes
- Geography
- ISO 3166
- JSON
- Open Data
- Phone Codes
- Reference Data
- Spectral
- Linting
- API Governance
---
