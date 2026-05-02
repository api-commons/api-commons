---
api_specs:
- filename: circana-liquid-data.yaml
  format: yaml
  label: Circana Liquid Data API
  slug: liquid-data-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/circana/refs/heads/main/openapi/circana-liquid-data.yaml
categories:
- delete
- examples
- get
- info
- microcks
- 'no'
- openapi
- operation
- pagination
- parameter
- paths
- post
- request
- response
- schema
- security
- servers
- tag
description: Spectral linting rules defining API design standards and conventions for Circana.
layout: rules
name: Circana API Rules
provider_name: Circana
provider_slug: circana
rule_count: 41
rules:
- description: Info title must be present and non-empty
  given: $.info
  name: info-title-required
  severity: error
- description: Info title should start with "Circana"
  given: $.info
  name: info-title-circana-prefix
  severity: warn
- description: Info description must be present and non-empty
  given: $.info
  name: info-description-required
  severity: error
- description: Info description should be at least 50 characters
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: API version must be specified
  given: $.info
  name: info-version-required
  severity: error
- description: Contact information should be provided
  given: $.info
  name: info-contact-required
  severity: warn
- description: OpenAPI version must be 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: Servers array must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Circana"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-circana-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Tags should have descriptions
  given: $.tags[*]
  name: tag-description
  severity: info
- description: Tag names should use Title Case
  given: $.tags[*].name
  name: tag-title-case
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Parameter names should use snake_case
  given: $.paths[*][get,post,put,patch,delete].parameters[*].name
  name: parameter-snake-case
  severity: warn
- description: Parameters must have a schema with type
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Parameters should include an example value
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-example-recommended
  severity: info
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must have a success response (2xx)
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should include a 401 Unauthorized response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Schema property names should use snake_case
  given: $.components.schemas[*].properties
  name: schema-property-snake-case
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties must define a type
  given: $.components.schemas[*].properties[*]
  name: schema-type-required
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: error
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Security schemes should have descriptions
  given: $.components.securitySchemes[*]
  name: security-scheme-description
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: POST operations should have a request body
  given: $.paths[*].post
  name: post-request-body-required
  severity: info
- description: Descriptions must not be empty strings
  given: $.paths[*][get,post,put,patch,delete].description
  name: no-empty-descriptions
  severity: error
- description: Response schemas should include examples
  given: $.paths[*][get,post,put,patch,delete].responses[*].content.application/json
  name: examples-recommended
  severity: info
- description: Paginated endpoints should use offset/limit parameters
  given: $.paths[*].get.parameters[?(@.name=='offset' || @.name=='limit')]
  name: pagination-offset-limit
  severity: info
- description: Operations should include x-microcks-operation for mock compatibility
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/circana-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/circana/refs/heads/main/rules/circana-spectral-rules.yml
severity_counts:
  error: 20
  hint: 0
  info: 6
  warn: 15
slug: circana-spectral-rules
source_filename: circana-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # ─── INFO / METADATA ───────────────────────────────────────────────\n  info-title-required:\n    description: Info title must be present and non-empty\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-title-circana-prefix:\n    description: Info title should start with \"Circana\"\n    severity: warn\n    given: $.info\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: \"^Circana \"\n\n  info-description-required:\n    description: Info description must be present and non-empty\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-description-min-length:\n    description: Info description should be at least 50 characters\n    severity: warn\n    given: $.info.description\n    then:\n      function: length\n      functionOptions:\n        min: 50\n\n  info-version-required:\n    description: API version must\
  \ be specified\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Contact information should be provided\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  # ─── OPENAPI VERSION ───────────────────────────────────────────────\n  openapi-version-3:\n    description: OpenAPI version must be 3.x\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # ─── SERVERS ────────────────────────────────────────────────────────\n  servers-defined:\n    description: Servers array must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs should use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n    \
  \    match: \"^https://\"\n\n  servers-description:\n    description: Each server should have a description\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # ─── PATHS — NAMING CONVENTIONS ────────────────────────────────────\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9\\\\-{}]+)+$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: error\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # ─── OPERATIONS ─────────────────────────────────────────────────────\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n \
  \   then:\n      field: summary\n      function: truthy\n\n  operation-summary-circana-prefix:\n    description: Operation summaries should start with \"Circana\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Circana \"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-camelcase:\n    description: operationId should use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n     \
  \ functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # ─── TAGS ───────────────────────────────────────────────────────────\n  tag-description:\n    description: Tags should have descriptions\n    severity: info\n    given: $.tags[*]\n    then:\n      field: description\n      function: truthy\n\n  tag-title-case:\n    description: Tag names should use Title Case\n    severity: warn\n    given: $.tags[*].name\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z]*(\\\\s[A-Za-z][a-zA-Z]*)*$\"\n\n  # ─── PARAMETERS ─────────────────────────────────────────────────────\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n\
  \    then:\n      field: description\n      function: truthy\n\n  parameter-snake-case:\n    description: Parameter names should use snake_case\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*].name\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9]*(_[a-z0-9]+)*$\"\n\n  parameter-schema-required:\n    description: Parameters must have a schema with type\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  parameter-example-recommended:\n    description: Parameters should include an example value\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: example\n      function: truthy\n\n  # ─── REQUEST BODIES ─────────────────────────────────────────────────\n  request-body-json-content:\n    description: Request bodies should use application/json content type\n    severity:\
  \ warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      field: application/json\n      function: truthy\n\n  # ─── RESPONSES ──────────────────────────────────────────────────────\n  response-success-required:\n    description: Every operation must have a success response (2xx)\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"202\"]\n            - required: [\"204\"]\n\n  response-401-required:\n    description: Operations should include a 401 Unauthorized response\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: \"401\"\n      function: truthy\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n\
  \    then:\n      field: description\n      function: truthy\n\n  # ─── SCHEMAS — PROPERTY NAMING ─────────────────────────────────────\n  schema-property-snake-case:\n    description: Schema property names should use snake_case\n    severity: warn\n    given: $.components.schemas[*].properties\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9]*(_[a-z0-9]+)*$\"\n\n  schema-description-required:\n    description: Top-level schemas should have descriptions\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-type-required:\n    description: Schema properties must define a type\n    severity: error\n    given: $.components.schemas[*].properties[*]\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"type\"]\n            - required: [\"$ref\"]\n            - required: [\"oneOf\"]\n \
  \           - required: [\"anyOf\"]\n            - required: [\"allOf\"]\n\n  # ─── SECURITY ───────────────────────────────────────────────────────\n  security-global-defined:\n    description: Global security must be defined\n    severity: error\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes must be defined in components\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-scheme-description:\n    description: Security schemes should have descriptions\n    severity: warn\n    given: $.components.securitySchemes[*]\n    then:\n      field: description\n      function: truthy\n\n  # ─── HTTP METHOD CONVENTIONS ────────────────────────────────────────\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n     \
  \ function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  post-request-body-required:\n    description: POST operations should have a request body\n    severity: info\n    given: $.paths[*].post\n    then:\n      field: requestBody\n      function: truthy\n\n  # ─── GENERAL QUALITY ────────────────────────────────────────────────\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].description\n    then:\n      function: truthy\n\n  examples-recommended:\n    description: Response schemas should include examples\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].responses[*].content.application/json\n    then:\n      field: examples\n      function: truthy\n\n  pagination-offset-limit:\n    description:\
  \ Paginated endpoints should use offset/limit parameters\n    severity: info\n    given: $.paths[*].get.parameters[?(@.name=='offset' || @.name=='limit')]\n    then:\n      function: truthy\n\n  microcks-operation-extension:\n    description: Operations should include x-microcks-operation for mock compatibility\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/circana/refs/heads/main/rules/circana-spectral-rules.yml
tags:
- Analytics
- Consumer Data
- Market Research
- Retail
- CPG
- Point Of Sale
- Consumer Insights
- Business Intelligence
- Spectral
- Linting
- API Governance
---
