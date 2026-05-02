---
api_specs:
- filename: better-stack-openapi.yml
  format: yaml
  label: Better Stack API
  slug: better-stack
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/better-stack/refs/heads/main/openapi/better-stack-openapi.yml
categories:
- examples
- http
- info
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
- tags
description: Spectral linting rules defining API design standards and conventions for Better Stack.
layout: rules
name: Better Stack API Rules
provider_name: Better Stack
provider_slug: better-stack
rule_count: 37
rules:
- description: API title should start with "Better Stack"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API description should be at least 30 characters
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: API info must specify a version
  given: $.info
  name: info-version-required
  severity: error
- description: OpenAPI version should be 3.0.x
  given: $.openapi
  name: openapi-version
  severity: warn
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Query strings must not appear in paths
  given: $.paths
  name: paths-no-query-string
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Better Stack"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-title-case
  severity: warn
- description: All operations must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: warn
- description: Global tags array should be defined
  given: $
  name: tags-global-defined
  severity: info
- description: Each global tag should have a description
  given: $.tags[*]
  name: tags-description-required
  severity: info
- description: All parameters must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Query parameter names should use snake_case
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in=='query')].name
  name: parameter-snake-case
  severity: info
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must define a 2xx success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should define a 401 Unauthorized response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-defined
  severity: info
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema property names should use snake_case
  given: $.components.schemas[*].properties
  name: schema-property-snake-case
  severity: info
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: warn
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Better Stack API should use Bearer authentication
  given: $.components.securitySchemes
  name: security-bearer-auth
  severity: info
- description: GET operations should not have a request body
  given: $.paths[*].get
  name: http-get-no-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: http-delete-no-body
  severity: warn
- description: POST operations should have a request body
  given: $.paths[*].post
  name: http-post-has-body
  severity: warn
- description: PATCH operations should have a request body
  given: $.paths[*].patch
  name: http-patch-has-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Schema properties should include example values
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/better-stack-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/better-stack/refs/heads/main/rules/better-stack-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 7
  warn: 17
slug: better-stack-spectral-rules
source_filename: better-stack-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title should start with \"Better Stack\"\n    message: \"Info title should start with 'Better Stack' — got '{{value}}'\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Better Stack\"\n\n  info-description-required:\n    description: API info must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-description-min-length:\n    description: API description should be at least 30 characters\n    message: \"Description is too short: {{value}}\"\n    severity: warn\n    given: $.info.description\n    then:\n      function: length\n      functionOptions:\n        min: 30\n\n  info-version-required:\n    description: API info must specify a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI\
  \ VERSION\n  openapi-version:\n    description: OpenAPI version should be 3.0.x\n    message: \"OpenAPI version should be 3.0.x — got '{{value}}'\"\n    severity: warn\n    given: $.openapi\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: All server URLs must use HTTPS\n    message: \"Server URL must use HTTPS — got '{{value}}'\"\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description-required:\n    description: Each server should have a description\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description:\
  \ Path segments should use kebab-case\n    message: \"Path '{{path}}' should use kebab-case segments\"\n    severity: warn\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9-{}]+)+$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    message: \"Path '{{path}}' must not end with a slash\"\n    severity: error\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  paths-no-query-string:\n    description: Query strings must not appear in paths\n    message: \"Path '{{path}}' must not contain a query string\"\n    severity: error\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\?\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field:\
  \ summary\n      function: truthy\n\n  operation-summary-title-case:\n    description: Operation summaries should start with \"Better Stack\"\n    message: \"Operation summary should start with 'Better Stack' — got '{{value}}'\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Better Stack\"\n\n  operation-description-required:\n    description: All operations must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: All operations must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId should use camelCase\n    message: \"operationId '{{value}}' should use\
  \ camelCase\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: All operations must have at least one tag\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tags-global-defined:\n    description: Global tags array should be defined\n    severity: info\n    given: $\n    then:\n      field: tags\n      function: truthy\n\n  tags-description-required:\n    description: Each global tag should have a description\n    severity: info\n    given: $.tags[*]\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n\
  \      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: All parameters must have a schema\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  parameter-snake-case:\n    description: Query parameter names should use snake_case\n    message: \"Parameter '{{value}}' should use snake_case\"\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in=='query')].name\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_]*$\"\n\n  # REQUEST BODIES\n  request-body-json-content:\n    description: Request bodies should use application/json content type\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  # RESPONSES\n  response-success-required:\n\
  \    description: Every operation must define a 2xx success response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-401-defined:\n    description: Operations should define a 401 Unauthorized response\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-description-required:\n    description: Top-level component schemas should\
  \ have descriptions\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-property-snake-case:\n    description: Schema property names should use snake_case\n    message: \"Property '{{path}}' should use snake_case\"\n    severity: info\n    given: $.components.schemas[*].properties\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n\n  # SECURITY\n  security-global-defined:\n    description: Global security must be defined\n    severity: warn\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes must be defined in components\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-bearer-auth:\n    description: Better Stack API should use Bearer authentication\n    severity: info\n    given: $.components.securitySchemes\n\
  \    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  # HTTP METHOD CONVENTIONS\n  http-get-no-body:\n    description: GET operations should not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  http-delete-no-body:\n    description: DELETE operations should not have a request body\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  http-post-has-body:\n    description: POST operations should have a request body\n    severity: warn\n    given: $.paths[*].post\n    then:\n      field: requestBody\n      function: truthy\n\n  http-patch-has-body:\n    description: PATCH operations should have a request body\n    severity: warn\n    given: $.paths[*].patch\n    then:\n      field: requestBody\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n \
  \   description: Descriptions must not be empty strings\n    message: \"Description is empty at {{path}}\"\n    severity: warn\n    given: $..description\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  examples-encouraged:\n    description: Schema properties should include example values\n    severity: info\n    given: $.components.schemas[*].properties[*]\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/better-stack/refs/heads/main/rules/better-stack-spectral-rules.yml
tags:
- Incidents
- Logs
- Monitoring
- Platform
- Status
- Uptime
- Observability
- On-Call
- Heartbeats
- Spectral
- Linting
- API Governance
---
