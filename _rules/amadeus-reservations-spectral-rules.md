---
api_specs:
- filename: amadeus-reservations-hotel-booking-openapi.yaml
  format: yaml
  label: Hotel Booking API
  slug: hotel-booking-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amadeus-reservations/refs/heads/main/openapi/amadeus-reservations-hotel-booking-openapi.yaml
- filename: amadeus-reservations-flight-create-orders-openapi.yaml
  format: yaml
  label: Flight Create Orders API
  slug: flight-create-orders-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amadeus-reservations/refs/heads/main/openapi/amadeus-reservations-flight-create-orders-openapi.yaml
- filename: amadeus-reservations-flight-order-management-openapi.yaml
  format: yaml
  label: Flight Order Management API
  slug: flight-order-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amadeus-reservations/refs/heads/main/openapi/amadeus-reservations-flight-order-management-openapi.yaml
- filename: amadeus-reservations-transfer-booking-openapi.yaml
  format: yaml
  label: Transfer Booking API
  slug: transfer-booking-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amadeus-reservations/refs/heads/main/openapi/amadeus-reservations-transfer-booking-openapi.yaml
- filename: amadeus-reservations-transfer-management-openapi.yaml
  format: yaml
  label: Transfer Management API
  slug: transfer-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amadeus-reservations/refs/heads/main/openapi/amadeus-reservations-transfer-management-openapi.yaml
categories:
- delete
- get
- info
- operation
- parameter
- post
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amadeus Reservations.
layout: rules
name: Amadeus Reservations API Rules
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
rule_count: 20
rules:
- description: API title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: API title must reference Amadeus.
  given: $.info.title
  name: info-title-amadeus-prefix
  severity: warn
- description: API must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be present.
  given: $.info
  name: info-version-required
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-required
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
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
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
- description: Every operation must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Booking operations should define a 401 response.
  given: $.paths[*][post].responses
  name: response-401-booking
  severity: warn
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: info
- description: Security schemes should be defined in components.
  given: $.components
  name: security-schemes-recommended
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return 204 No Content.
  given: $.paths[*].delete.responses
  name: delete-returns-204
  severity: info
- description: POST operations for booking creation should have a request body.
  given: $.paths[*].post
  name: post-has-request-body
  severity: warn
rules_file: rules/amadeus-reservations-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amadeus-reservations/refs/heads/main/rules/amadeus-reservations-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 2
  warn: 7
slug: amadeus-reservations-spectral-rules
source_filename: amadeus-reservations-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: API title must be present.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-title-amadeus-prefix:\n    description: API title must reference Amadeus.\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"Amadeus|amadeus\"\n\n  info-description-required:\n    description: API must have a description.\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API version must be present.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # SERVERS\n  servers-required:\n    description: At least one server must be defined.\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description:\
  \ Server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-amadeus-prefix:\n    description: Operation summaries must start with \"Amadeus\".\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amadeus \"\n\n  operation-description-required:\n    description: Every operation must have a description.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId.\n    severity:\
  \ error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: warn\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must define at least one 2xx response.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-401-booking:\n    description: Booking operations should define a 401 response.\n    severity:\
  \ warn\n    given: $.paths[*][post].responses\n    then:\n      field: '401'\n      function: truthy\n\n  response-description-required:\n    description: Every response must have a description.\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-recommended:\n    description: Top-level schemas should have descriptions.\n    severity: info\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-recommended:\n    description: Security schemes should be defined in components.\n    severity: warn\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n\
  \  delete-returns-204:\n    description: DELETE operations should return 204 No Content.\n    severity: info\n    given: $.paths[*].delete.responses\n    then:\n      field: '204'\n      function: truthy\n\n  post-has-request-body:\n    description: POST operations for booking creation should have a request body.\n    severity: warn\n    given: $.paths[*].post\n    then:\n      field: requestBody\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amadeus-reservations/refs/heads/main/rules/amadeus-reservations-spectral-rules.yml
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
- Spectral
- Linting
- API Governance
---
