---
api_specs:
- filename: blablacar-bus-api-openapi.yaml
  format: yaml
  label: BlaBlaCar Bus API
  slug: blablacar-bus-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/blablacar-bus-api/refs/heads/main/openapi/blablacar-bus-api-openapi.yaml
categories:
- delete
- external
- get
- info
- 'no'
- openapi
- operation
- parameter
- paths
- post
- request
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for BlaBlaCar Bus API.
layout: rules
name: BlaBlaCar Bus API API Rules
provider_name: BlaBlaCar Bus API
provider_slug: blablacar-bus-api
rule_count: 36
rules:
- description: API title must start with "BlaBlaCar Bus"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Info object should have contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Server entries should have descriptions
  given: $.servers[*]
  name: servers-description
  severity: info
- description: Path segments must use kebab-case or use path parameters
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "BlaBlaCar Bus"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-id-required
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must define a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Parameter names should use snake_case
  given: $.paths[*][get,post,put,patch,delete].parameters[*].name
  name: parameter-snake-case
  severity: info
- description: Request bodies must support application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json
  severity: warn
- description: Request bodies should have a description
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: info
- description: Every operation must define at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Operations should define a 401 Unauthorized response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-defined
  severity: warn
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations with path parameters should define a 404 response
  given: $.paths[*~.*\{.*\}.*][get,delete].responses
  name: response-404-on-path-params
  severity: warn
- description: Schema property names must use snake_case
  given: $.components.schemas[*].properties[*]~
  name: schema-property-snake-case
  severity: warn
- description: Top-level schemas must have a description
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema objects must define a type
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: At least one security scheme must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: warn
- description: POST operations should have a request body
  given: $.paths[*].post
  name: post-has-request-body
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return a success response
  given: $.paths[*].delete.responses
  name: delete-returns-success
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Global tags array should be defined
  given: $
  name: tags-global-defined
  severity: info
- description: External documentation should be provided
  given: $
  name: external-docs-encouraged
  severity: info
rules_file: rules/blablacar-bus-api-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/blablacar-bus-api/refs/heads/main/rules/blablacar-bus-api-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 5
  warn: 18
slug: blablacar-bus-api-spectral-rules
source_filename: blablacar-bus-api-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# BlaBlaCar Bus API Spectral Ruleset\n# Enforces conventions observed in the BlaBlaCar Bus API OpenAPI specification.\n\nrules:\n\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"BlaBlaCar Bus\"\n    severity: warn\n    given: '$.info.title'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^BlaBlaCar Bus'\n\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: '$.info'\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must have a version\n    severity: error\n    given: '$.info'\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Info object should have contact information\n    severity: warn\n    given: '$.info'\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description:\
  \ Must use OpenAPI 3.x\n    severity: error\n    given: '$'\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: '^3\\.'\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined\n    severity: error\n    given: '$'\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: '$.servers[*].url'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n\n  servers-description:\n    description: Server entries should have descriptions\n    severity: info\n    given: '$.servers[*]'\n    then:\n      field: description\n      function: truthy\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments must use kebab-case or use path parameters\n    severity: warn\n    given: '$.paths[*]~'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^(/[a-z0-9-]+|\\\
  {[a-z_]+\\})+$'\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: warn\n    given: '$.paths[*]~'\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: '/$'\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete,options,head]'\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries must start with \"BlaBlaCar Bus\"\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].summary'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^BlaBlaCar Bus'\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete,options,head]'\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n\
  \    description: Every operation must have an operationId\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete,options,head]'\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId must use camelCase\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].operationId'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]+$'\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].parameters[*]'\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Every parameter\
  \ must define a schema\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].parameters[*]'\n    then:\n      field: schema\n      function: truthy\n\n  parameter-snake-case:\n    description: Parameter names should use snake_case\n    severity: info\n    given: '$.paths[*][get,post,put,patch,delete].parameters[*].name'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-z0-9_]*$'\n\n  # REQUEST BODIES\n  request-body-json:\n    description: Request bodies must support application/json content type\n    severity: warn\n    given: '$.paths[*][post,put,patch].requestBody.content'\n    then:\n      field: application/json\n      function: truthy\n\n  request-body-description:\n    description: Request bodies should have a description\n    severity: info\n    given: '$.paths[*][post,put,patch].requestBody'\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation\
  \ must define at least one 2xx response\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: responses\n      function: truthy\n\n  response-401-defined:\n    description: Operations should define a 401 Unauthorized response\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].responses'\n    then:\n      field: '401'\n      function: truthy\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].responses[*]'\n    then:\n      field: description\n      function: truthy\n\n  response-404-on-path-params:\n    description: Operations with path parameters should define a 404 response\n    severity: warn\n    given: '$.paths[*~.*\\{.*\\}.*][get,delete].responses'\n    then:\n      field: '404'\n      function: truthy\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-property-snake-case:\n    description: Schema property names must\
  \ use snake_case\n    severity: warn\n    given: '$.components.schemas[*].properties[*]~'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-z0-9_]*$'\n\n  schema-description-required:\n    description: Top-level schemas must have a description\n    severity: warn\n    given: '$.components.schemas[*]'\n    then:\n      field: description\n      function: truthy\n\n  schema-type-required:\n    description: Schema objects must define a type\n    severity: warn\n    given: '$.components.schemas[*]'\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: At least one security scheme must be defined in components\n    severity: error\n    given: '$.components'\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: Global security must be defined\n    severity: warn\n    given: '$'\n    then:\n      field: security\n      function: truthy\n\
  \n  # HTTP METHOD CONVENTIONS\n  post-has-request-body:\n    description: POST operations should have a request body\n    severity: warn\n    given: '$.paths[*].post'\n    then:\n      field: requestBody\n      function: truthy\n\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: '$.paths[*].get'\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-returns-success:\n    description: DELETE operations should return a success response\n    severity: warn\n    given: '$.paths[*].delete.responses'\n    then:\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: '$..description'\n    then:\n      function: pattern\n      functionOptions:\n        match: '.+'\n\n  tags-global-defined:\n    description: Global tags array should be defined\n    severity: info\n    given: '$'\n    then:\n      field: tags\n\
  \      function: truthy\n\n  external-docs-encouraged:\n    description: External documentation should be provided\n    severity: info\n    given: '$'\n    then:\n      field: externalDocs\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/blablacar-bus-api/refs/heads/main/rules/blablacar-bus-api-spectral-rules.yml
tags:
- Booking
- Buses
- Coach
- Europe
- Mobility
- Ticketing
- Transportation
- Travel
- Spectral
- Linting
- API Governance
---
