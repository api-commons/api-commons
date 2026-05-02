---
api_specs:
- filename: amadeus-solutions-flight-offers-search-openapi.yaml
  format: yaml
  label: Flight Offers Search API
  slug: flight-offers-search-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amadeus-solutions/refs/heads/main/openapi/amadeus-solutions-flight-offers-search-openapi.yaml
- filename: amadeus-solutions-flight-offers-price-openapi.yaml
  format: yaml
  label: Flight Offers Price API
  slug: flight-offers-price-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amadeus-solutions/refs/heads/main/openapi/amadeus-solutions-flight-offers-price-openapi.yaml
- filename: amadeus-solutions-branded-fares-upsell-openapi.yaml
  format: yaml
  label: Branded Fares Upsell API
  slug: branded-fares-upsell-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amadeus-solutions/refs/heads/main/openapi/amadeus-solutions-branded-fares-upsell-openapi.yaml
- filename: amadeus-solutions-seat-map-display-openapi.yaml
  format: yaml
  label: Seat Map Display API
  slug: seat-map-display-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amadeus-solutions/refs/heads/main/openapi/amadeus-solutions-seat-map-display-openapi.yaml
categories:
- get
- info
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amadeus Solutions.
layout: rules
name: Amadeus Solutions API Rules
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
rule_count: 15
rules:
- description: API title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: API must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be present.
  given: $.info
  name: info-version-required
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Amadeus".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-amadeus-prefix
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Every parameter must have a description.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Operations should define a 401 response.
  given: $.paths[*][get,post].responses
  name: response-401-required
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description
  severity: info
- description: Security schemes should be defined.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
rules_file: rules/amadeus-solutions-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amadeus-solutions/refs/heads/main/rules/amadeus-solutions-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 1
  warn: 4
slug: amadeus-solutions-spectral-rules
source_filename: amadeus-solutions-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: API title must be present.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  info-description-required:\n    description: API must have a description.\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: API version must be present.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  servers-https:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n  operation-summary-amadeus-prefix:\n    description:\
  \ Operation summaries must start with \"Amadeus\".\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amadeus \"\n  operation-id-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: warn\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: description\n      function: truthy\n  response-description-required:\n    description: Every response must have a description.\n    severity: error\n    given: $.paths[*][*].responses[*]\n\
  \    then:\n      field: description\n      function: truthy\n  response-401-required:\n    description: Operations should define a 401 response.\n    severity: warn\n    given: $.paths[*][get,post].responses\n    then:\n      field: '401'\n      function: truthy\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n  schema-description:\n    description: Top-level schemas should have descriptions.\n    severity: info\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n  security-schemes-defined:\n    description: Security schemes should be defined.\n    severity: warn\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes.\n    severity: error\n    given: $.paths\n    then:\n      function:\
  \ pattern\n      functionOptions:\n        notMatch: \"/$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amadeus-solutions/refs/heads/main/rules/amadeus-solutions-spectral-rules.yml
tags:
- Airlines
- Booking
- Flights
- GDS
- Hotels
- Travel
- Travel Technology
- Spectral
- Linting
- API Governance
---
