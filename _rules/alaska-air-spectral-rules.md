---
api_specs:
- filename: alaska-air-flight-status-openapi.yaml
  format: yaml
  label: Alaska Airlines Flight Status API
  slug: flight-status-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/alaska-air/refs/heads/main/openapi/alaska-air-flight-status-openapi.yaml
- filename: alaska-air-flight-schedules-openapi.yaml
  format: yaml
  label: Alaska Airlines Flight Schedules API
  slug: flight-schedules-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/alaska-air/refs/heads/main/openapi/alaska-air-flight-schedules-openapi.yaml
- filename: alaska-air-cargo-openapi.yaml
  format: yaml
  label: Alaska Air Cargo API
  slug: cargo-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/alaska-air/refs/heads/main/openapi/alaska-air-cargo-openapi.yaml
- filename: alaska-air-mileage-plan-openapi.yaml
  format: yaml
  label: Alaska Airlines Mileage Plan API
  slug: mileage-plan-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/alaska-air/refs/heads/main/openapi/alaska-air-mileage-plan-openapi.yaml
categories:
- examples
- get
- info
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Alaska Airlines.
layout: rules
name: Alaska Airlines API Rules
provider_name: Alaska Airlines
provider_slug: alaska-air
rule_count: 32
rules:
- description: Info title must be defined
  given: $.info
  name: info-title-required
  severity: error
- description: API title should start with 'Alaska'
  given: $.info.title
  name: info-title-alaska-prefix
  severity: warn
- description: Info description must be defined
  given: $.info
  name: info-description-required
  severity: warn
- description: Info version must be defined
  given: $.info
  name: info-version-required
  severity: error
- description: Info should include contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Must use OpenAPI 3.0.x
  given: $
  name: openapi-version-3
  severity: error
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https-required
  severity: error
- description: Server URLs should use alaskaair.com or alaskacargo.com domains
  given: $.servers[*]
  name: servers-alaskaair-domain
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: API paths should include a version prefix
  given: $.paths[*]~
  name: paths-versioned
  severity: warn
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with 'Alaska Airlines' or 'Alaska Air'
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-alaska-prefix
  severity: warn
- description: Operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: OperationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Tags should be defined at the global level
  given: $
  name: tags-defined
  severity: warn
- description: Global tags should have descriptions
  given: $.tags[*]
  name: tags-description-required
  severity: warn
- description: Parameters must have a description
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: Parameters must have a schema
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: IATA airport code parameters should use enum or note valid format
  given: $.paths[*][*].parameters[?(@.name == 'origin' || @.name == 'destination' || @.name == 'originAirport' || @.name == 'destinationAirport')]
  name: parameter-iata-uppercase
  severity: info
- description: Operations must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: APIs should define 401 Unauthorized response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-401-required
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schemas should define a type
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Security schemes must be defined
  given: $
  name: security-schemes-defined
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should have examples
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/alaska-air-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/alaska-air/refs/heads/main/rules/alaska-air-spectral-rules.yml
severity_counts:
  error: 16
  hint: 0
  info: 2
  warn: 14
slug: alaska-air-spectral-rules
source_filename: alaska-air-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: Info title must be defined\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-title-alaska-prefix:\n    description: API title should start with 'Alaska'\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Alaska \"\n\n  info-description-required:\n    description: Info description must be defined\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info version must be defined\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Info should include contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n\
  \  openapi-version-3:\n    description: Must use OpenAPI 3.0.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-required:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-alaskaair-domain:\n    description: Server URLs should use alaskaair.com or alaskacargo.com domains\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"alaska(air|cargo)\\\\.com\"\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should\
  \ use kebab-case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9-{}]+)+$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have a trailing slash\n    severity: error\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  paths-versioned:\n    description: API paths should include a version prefix\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/v[0-9]\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-alaska-prefix:\n    description: Operation summaries should start with 'Alaska Airlines' or 'Alaska Air'\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\
  \n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Alaska (Airlines|Air) \"\n\n  operation-description-required:\n    description: Operations should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n    description: Operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-camel-case:\n    description: OperationId should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: Operations must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n  \
  \  then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tags-defined:\n    description: Tags should be defined at the global level\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  tags-description-required:\n    description: Global tags should have descriptions\n    severity: warn\n    given: \"$.tags[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Parameters must have a description\n    severity: error\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Parameters must have a schema\n    severity: error\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  parameter-iata-uppercase:\n    description: IATA airport code parameters should use enum or note valid format\n    severity: info\n  \
  \  given: \"$.paths[*][*].parameters[?(@.name == 'origin' || @.name == 'destination' || @.name == 'originAirport' || @.name == 'destinationAirport')]\"\n    then:\n      field: schema.example\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z]{3}$\"\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must have at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses\n      function: truthy\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-401-required:\n    description: APIs should define 401 Unauthorized response\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses.401\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n\
  \    description: Top-level schemas should have descriptions\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-type-required:\n    description: Schemas should define a type\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: components.securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n\
  \      functionOptions:\n        match: \".+\"\n\n  examples-encouraged:\n    description: Schema properties should have examples\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: example\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/alaska-air/refs/heads/main/rules/alaska-air-spectral-rules.yml
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
- Spectral
- Linting
- API Governance
---
