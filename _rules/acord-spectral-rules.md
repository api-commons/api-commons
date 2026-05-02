---
api_specs:
- filename: acord-ngds-openapi.yml
  format: yaml
  label: ACORD Next-Generation Digital Standards (NGDS) API
  slug: acord-ngds-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/openapi/acord-ngds-openapi.yml
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
- post
- request
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for ACORD.
layout: rules
name: ACORD API Rules
provider_name: ACORD
provider_slug: acord
rule_count: 33
rules:
- description: OpenAPI info.title must be present and non-empty
  given: $.info
  name: info-title-required
  severity: error
- description: OpenAPI info.description must be present with meaningful content
  given: $.info
  name: info-description-required
  severity: warn
- description: OpenAPI info.version must be defined
  given: $.info
  name: info-version-required
  severity: error
- description: API info should include contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: ACORD APIs must use OpenAPI 3.x
  given: $
  name: openapi-version-3x
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs should use HTTPS in production
  given: $.servers[*]
  name: servers-https
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not end with a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: All operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: ACORD operation summaries should start with 'ACORD'
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-acord-prefix
  severity: info
- description: Global tags array should be defined
  given: $
  name: tags-global-defined
  severity: warn
- description: All global tags should have descriptions
  given: $.tags[*]
  name: tags-description-required
  severity: warn
- description: All parameters must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should have a description
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: warn
- description: All operations must define at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All response entries must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: APIs with authentication should define 401 responses
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-defined
  severity: warn
- description: Paths with ID parameters should define 404 responses
  given: $.paths[*~[*Id}*]][get,patch,delete].responses
  name: response-404-on-id-paths
  severity: warn
- description: All top-level schemas should have a description
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should define a type
  given: $.components.schemas[*].properties[*]
  name: schema-type-required
  severity: warn
- description: Security schemes should be defined in components
  given: $
  name: security-schemes-defined
  severity: error
- description: Global security should be defined
  given: $
  name: security-global-defined
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
  name: post-has-request-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have x-microcks-operation for mock testing
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-present
  severity: info
rules_file: rules/acord-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/rules/acord-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 2
  warn: 17
slug: acord-spectral-rules
source_filename: acord-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: OpenAPI info.title must be present and non-empty\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: OpenAPI info.description must be present with meaningful content\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: OpenAPI info.version must be defined\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API info should include contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3x:\n    description: ACORD APIs must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function:\
  \ pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: At least one server must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs should use HTTPS in production\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(\\\\/[a-z][a-z0-9-]*)(\\\\/(\\\\{[a-z][a-zA-Z0-9]*\\\\}|[a-z][a-z0-9-]*))*$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not end with a trailing slash\n    severity: error\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n\
  \        notMatch: \"\\\\/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: All operations should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n\
  \    description: All operations must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  operation-summary-acord-prefix:\n    description: ACORD operation summaries should start with 'ACORD'\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^ACORD \"\n\n  # TAGS\n  tags-global-defined:\n    description: Global tags array should be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  tags-description-required:\n    description: All global tags should have descriptions\n    severity: warn\n    given: \"$.tags[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\
  \n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: All parameters must have a schema\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-description:\n    description: Request bodies should have a description\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody\"\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: All operations must define at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-description-required:\n\
  \    description: All response entries must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-401-defined:\n    description: APIs with authentication should define 401 responses\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [\"401\"]\n\n  response-404-on-id-paths:\n    description: Paths with ID parameters should define 404 responses\n    severity: warn\n    given: \"$.paths[*~[*Id}*]][get,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [\"404\"]\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-description-required:\n    description: All top-level schemas should have a description\n    severity: warn\n    given:\
  \ \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-type-required:\n    description: Schema properties should define a type\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes should be defined in components\n    severity: error\n    given: \"$\"\n    then:\n      field: components.securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: Global security should be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations\
  \ should not have a request body\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  post-has-request-body:\n    description: POST operations should have a request body\n    severity: warn\n    given: \"$.paths[*].post\"\n    then:\n      field: requestBody\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  microcks-operation-present:\n    description: Operations should have x-microcks-operation for mock testing\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/rules/acord-spectral-rules.yml
tags:
- Claims
- Insurance
- Policy
- Standards
- Underwriting
- Spectral
- Linting
- API Governance
---
