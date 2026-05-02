---
api_specs:
- filename: airbyte-openapi.yml
  format: yaml
  label: Airbyte
  slug: airbyte
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/airbyte/refs/heads/main/openapi/airbyte-openapi.yml
categories:
- delete
- get
- info
- microcks
- 'no'
- openapi
- operation
- parameter
- paths
- request
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Airbyte.
layout: rules
name: Airbyte API Rules
provider_name: Airbyte
provider_slug: airbyte
rule_count: 28
rules:
- description: Info title must be defined.
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be defined and non-empty.
  given: $.info
  name: info-description-required
  severity: warn
- description: Info version must be defined.
  given: $.info
  name: info-version-required
  severity: error
- description: OpenAPI version must be 3.x.
  given: $
  name: openapi-version-3
  severity: error
- description: Servers array must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS.
  given: $.servers[*]
  name: servers-https
  severity: warn
- description: Path segments should use kebab-case.
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes.
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: operationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationId-camelCase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Operation summaries should start with "Airbyte".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-starts-with-airbyte
  severity: info
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters must have a schema.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: info
- description: Every operation must have at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Secured operations should document 401 response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-on-secured-ops
  severity: info
- description: Schema property names should use snake_case.
  given: $.components.schemas[*].properties[*]~
  name: schema-properties-snake-case
  severity: info
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Security schemes should be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: Bearer security should use bearerFormat JWT or similar.
  given: $.components.securitySchemes[*][?(@.scheme == 'bearer')]
  name: security-bearer-format
  severity: info
- description: GET operations should not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Operations should include x-microcks-operation for mock compatibility.
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/airbyte-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/airbyte/refs/heads/main/rules/airbyte-spectral-rules.yml
severity_counts:
  error: 9
  hint: 0
  info: 7
  warn: 12
slug: airbyte-spectral-rules
source_filename: airbyte-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: Info title must be defined.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: Info description must be defined and non-empty.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info version must be defined.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: OpenAPI version must be 3.x.\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers array must be defined.\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function:\
  \ truthy\n\n  servers-https:\n    description: Server URLs should use HTTPS.\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case.\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}-]+)+$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes.\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description:\
  \ Every operation should have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-operationId-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationId-camelCase:\n    description: operationId should use camelCase.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  operation-summary-starts-with-airbyte:\n    description: Operation summaries should start\
  \ with \"Airbyte\".\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Airbyte \"\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: All parameters must have a schema.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-json-content:\n    description: Request bodies should use application/json content type.\n    severity: info\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation\
  \ must have at least one 2xx response.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-description-required:\n    description: All responses must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-401-on-secured-ops:\n    description: Secured operations should document 401 response.\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: truthy\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-properties-snake-case:\n    description: Schema property names should use snake_case.\n    severity: info\n    given: \"$.components.schemas[*].properties[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_]*$\"\
  \n\n  schema-description-required:\n    description: Top-level schemas should have a description.\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes should be defined in components.\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-bearer-format:\n    description: Bearer security should use bearerFormat JWT or similar.\n    severity: info\n    given: \"$.components.securitySchemes[*][?(@.scheme == 'bearer')]\"\n    then:\n      field: bearerFormat\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations should not have a request body.\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations\
  \ should not have a request body.\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: truthy\n\n  microcks-operation-extension:\n    description: Operations should include x-microcks-operation for mock compatibility.\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/airbyte/refs/heads/main/rules/airbyte-spectral-rules.yml
tags:
- Data Integration
- ETL
- ELT
- Open Source
- Data Pipeline
- Connectors
- Data
- Spectral
- Linting
- API Governance
---
