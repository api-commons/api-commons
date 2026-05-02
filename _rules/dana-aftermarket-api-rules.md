---
api_specs:
- filename: dana-aftermarket-api-openapi.yml
  format: yaml
  label: Dana Aftermarket API
  slug: aftermarket-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dana/refs/heads/main/openapi/dana-aftermarket-api-openapi.yml
categories:
- dana
description: Spectral linting rules defining API design standards and conventions for Dana.
layout: rules
name: Dana API Rules
provider_name: Dana
provider_slug: dana
rule_count: 5
rules:
- description: API info should include a contact for Dana's developer relations team.
  given: $.info
  name: dana-info-contact
  severity: warn
- description: Servers should reference the api.danaaftermarket.com base URL.
  given: $.servers[*].url
  name: dana-base-url
  severity: warn
- description: API should declare an X-API-Key apiKey security scheme.
  given: $.components.securitySchemes
  name: dana-api-key-security
  severity: error
- description: Operations should be tagged Parts, Availability, Pricing, Orders, or Shipping.
  given: $.paths[*][*]
  name: dana-operation-tags
  severity: warn
- description: Endpoints touching a single part must accept partNumber as a path or query parameter.
  given: $.paths
  name: dana-part-number-required
  severity: warn
rules_file: rules/dana-aftermarket-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/dana/refs/heads/main/rules/dana-aftermarket-api-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 4
slug: dana-aftermarket-api-rules
source_filename: dana-aftermarket-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  dana-info-contact:\n    description: API info should include a contact for Dana's developer relations team.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  dana-base-url:\n    description: Servers should reference the api.danaaftermarket.com base URL.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"danaaftermarket\\\\.com\"\n  dana-api-key-security:\n    description: API should declare an X-API-Key apiKey security scheme.\n    given: $.components.securitySchemes\n    severity: error\n    then:\n      field: apiKey\n      function: truthy\n  dana-operation-tags:\n    description: Operations should be tagged Parts, Availability, Pricing, Orders, or Shipping.\n    given: $.paths[*][*]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n  dana-part-number-required:\n    description: Endpoints\
  \ touching a single part must accept partNumber as a path or query parameter.\n    given: $.paths\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"partNumber\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/dana/refs/heads/main/rules/dana-aftermarket-api-rules.yml
tags:
- Aftermarket
- Auto Parts
- Drivetrain
- eCommerce
- Supply Chain
- Spectral
- Linting
- API Governance
---
