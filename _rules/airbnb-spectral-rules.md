---
api_specs:
- filename: airbnb-homes-api-openapi.yml
  format: yaml
  label: Airbnb Homes API
  slug: homes-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/airbnb/refs/heads/main/openapi/airbnb-homes-api-openapi.yml
- filename: airbnb-activities-api-openapi.yml
  format: yaml
  label: Airbnb Activities API
  slug: activities-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/airbnb/refs/heads/main/openapi/airbnb-activities-api-openapi.yml
- filename: airbnb-webhooks-asyncapi.yml
  format: yaml
  label: Airbnb Webhooks API
  slug: webhooks-api
  spec_type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/airbnb/refs/heads/main/asyncapi/airbnb-webhooks-asyncapi.yml
categories:
- airbnb
description: Spectral linting rules defining API design standards and conventions for airbnb.
layout: rules
name: airbnb API Rules
provider_name: airbnb
provider_slug: airbnb
rule_count: 15
rules:
- description: All operation summaries must use Title Case
  given: $.paths[*][get,post,put,patch,delete]
  name: airbnb-operation-summary-title-case
  severity: warn
- description: Operation IDs must use camelCase
  given: $.paths[*][get,post,put,patch,delete]
  name: airbnb-operation-id-camel-case
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: airbnb-require-operation-tags
  severity: error
- description: GET operations must define a 200 response
  given: $.paths[*].get
  name: airbnb-require-response-200
  severity: error
- description: All component schemas must have a title
  given: $.components.schemas[*]
  name: airbnb-schema-title-required
  severity: warn
- description: All operations must require OAuth2 security
  given: $.paths[*][get,post,put,patch,delete]
  name: airbnb-require-oauth2-security
  severity: error
- description: Listing status must use defined enum values
  given: $.components.schemas.Listing.properties.status
  name: airbnb-listing-status-enum
  severity: warn
- description: List operations should support pagination parameters
  given: $.paths[*].get
  name: airbnb-require-pagination-params
  severity: warn
- description: Reservation schema must include check_in and check_out
  given: $.components.schemas.Reservation.properties
  name: airbnb-reservation-required-dates
  severity: error
- description: API must define at least one server URL
  given: $
  name: airbnb-require-server-url
  severity: error
- description: API info must include contact information
  given: $.info
  name: airbnb-require-contact-info
  severity: warn
- description: Path responses should reference component schemas, not inline
  given: $.paths[*][*].responses[*].content[*].schema
  name: airbnb-no-inline-schemas-in-paths
  severity: warn
- description: Schemas with price fields should include currency
  given: $.components.schemas[*].properties
  name: airbnb-currency-field-present
  severity: warn
- description: All operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: airbnb-require-description-on-paths
  severity: warn
- description: API should include externalDocs pointing to developer portal
  given: $
  name: airbnb-require-external-docs
  severity: warn
rules_file: rules/airbnb-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/airbnb/refs/heads/main/rules/airbnb-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 0
  warn: 10
slug: airbnb-spectral-rules
source_filename: airbnb-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  airbnb-operation-summary-title-case:\n    description: All operation summaries must use Title Case\n    message: Summary \"{{value}}\" is not in Title Case\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: ^[A-Z]\n  airbnb-operation-id-camel-case:\n    description: Operation IDs must use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: ^[a-z][a-zA-Z0-9]*$\n  airbnb-require-operation-tags:\n    description: All operations must have at least one tag\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n  airbnb-require-response-200:\n    description: GET operations must define a 200 response\n    severity: error\n    given: $.paths[*].get\n    then:\n\
  \      field: responses.200\n      function: truthy\n  airbnb-schema-title-required:\n    description: All component schemas must have a title\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: title\n      function: truthy\n  airbnb-require-oauth2-security:\n    description: All operations must require OAuth2 security\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          properties:\n            security:\n              type: array\n              minItems: 1\n  airbnb-listing-status-enum:\n    description: Listing status must use defined enum values\n    severity: warn\n    given: $.components.schemas.Listing.properties.status\n    then:\n      field: enum\n      function: truthy\n  airbnb-require-pagination-params:\n    description: List operations should support pagination parameters\n    severity: warn\n    given: $.paths[*].get\n    then:\n      function:\
  \ schema\n      functionOptions:\n        schema:\n          properties:\n            parameters:\n              type: array\n  airbnb-reservation-required-dates:\n    description: Reservation schema must include check_in and check_out\n    severity: error\n    given: $.components.schemas.Reservation.properties\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          required:\n          - check_in\n          - check_out\n  airbnb-require-server-url:\n    description: API must define at least one server URL\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n  airbnb-require-contact-info:\n    description: API info must include contact information\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  airbnb-no-inline-schemas-in-paths:\n    description: Path responses should reference component schemas, not inline\n    severity: warn\n    given: $.paths[*][*].responses[*].content[*].schema\n\
  \    then:\n      function: schema\n      functionOptions:\n        schema:\n          oneOf:\n          - required:\n            - $ref\n          - required:\n            - properties\n  airbnb-currency-field-present:\n    description: Schemas with price fields should include currency\n    severity: warn\n    given: $.components.schemas[*].properties\n    then:\n      function: schema\n      functionOptions:\n        schema: {}\n  airbnb-require-description-on-paths:\n    description: All operations must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n  airbnb-require-external-docs:\n    description: API should include externalDocs pointing to developer portal\n    severity: warn\n    given: $\n    then:\n      field: externalDocs\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/airbnb/refs/heads/main/rules/airbnb-spectral-rules.yml
tags:
- Spectral
- Linting
- API Governance
---
