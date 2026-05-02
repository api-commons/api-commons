---
api_specs:
- filename: cities-database-api-openapi.yml
  format: yaml
  label: AirLabs Cities API
  slug: airlabs-cities-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cities-database-api/refs/heads/main/openapi/cities-database-api-openapi.yml
categories:
- cities
description: Spectral linting rules defining API design standards and conventions for Cities Database API.
layout: rules
name: Cities Database API API Rules
provider_name: Cities Database API
provider_slug: cities-database-api
rule_count: 5
rules:
- description: Cities Database API server URL MUST use HTTPS.
  given: $.servers[*].url
  name: cities-server-https
  severity: error
- description: Cities Database API server SHOULD be airlabs.co/api/v9.
  given: $.servers[*].url
  name: cities-base-url
  severity: warn
- description: Operations MUST have an operationId.
  given: $.paths[*][get,post,put,delete,patch]
  name: cities-operation-id
  severity: error
- description: Operations MUST be tagged.
  given: $.paths[*][get,post,put,delete,patch].tags
  name: cities-tag-required
  severity: warn
- description: Cities Database API operations MUST require an api_key parameter.
  given: $.paths[*][get,post,put,delete,patch].parameters[?(@.name=='api_key')]
  name: cities-api-key-required
  severity: error
rules_file: rules/cities-database-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cities-database-api/refs/heads/main/rules/cities-database-api-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 2
slug: cities-database-api-rules
source_filename: cities-database-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  cities-server-https:\n    description: Cities Database API server URL MUST use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  cities-base-url:\n    description: Cities Database API server SHOULD be airlabs.co/api/v9.\n    severity: warn\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://airlabs\\.co/api/v9'\n  cities-operation-id:\n    description: Operations MUST have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  cities-tag-required:\n    description: Operations MUST be tagged.\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].tags\n    then:\n      function: truthy\n  cities-api-key-required:\n    description: Cities Database API operations MUST require\
  \ an api_key parameter.\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch].parameters[?(@.name=='api_key')]\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cities-database-api/refs/heads/main/rules/cities-database-api-rules.yml
tags:
- Cities
- Data
- Geography
- Locations
- Reference Data
- Travel
- Spectral
- Linting
- API Governance
---
