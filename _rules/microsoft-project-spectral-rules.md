---
api_specs:
- filename: microsoft-project-rest-api.yaml
  format: yaml
  label: Microsoft Project Online REST API
  slug: rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/microsoft-project/refs/heads/main/openapi/microsoft-project-rest-api.yaml
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
- tag
- tags
- uuid
description: Spectral linting rules defining API design standards and conventions for Microsoft Project.
layout: rules
name: Microsoft Project API Rules
provider_name: Microsoft Project
provider_slug: microsoft-project
rule_count: 39
rules:
- description: Info object must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: Title should start with "Microsoft Project"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info description should be at least 50 characters
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: Info object must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Info object should have contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: OpenAPI version should be 3.0.x
  given: $.openapi
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
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Paths must not end with a trailing slash
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Paths must not contain query strings
  given: $.paths
  name: paths-no-query-strings
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Microsoft Project"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Operation IDs should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined
  given: $
  name: tags-defined
  severity: warn
- description: Each global tag should have a description
  given: $.tags[*]
  name: tag-description
  severity: info
- description: Every parameter must have a description
  given: $..parameters[*]
  name: parameter-description-required
  severity: error
- description: Every parameter must have a schema with a type
  given: $..parameters[*]
  name: parameter-schema-required
  severity: error
- description: Path parameters must be required
  given: $..parameters[?(@.in == 'path')]
  name: parameter-path-required
  severity: error
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json
  severity: warn
- description: Every operation must define a success response (2xx)
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations should define a 401 Unauthorized response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-defined
  severity: info
- description: All schemas must define a type
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: error
- description: Schema properties should use PascalCase (Microsoft convention)
  given: $.components.schemas[*].properties
  name: schema-properties-pascal-case
  severity: info
- description: Global security must be defined
  given: $
  name: security-defined
  severity: error
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: OAuth2 security scheme should be defined for SharePoint APIs
  given: $.components.securitySchemes
  name: security-oauth2-scheme
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations must not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: error
- description: POST operations should have a request body
  given: $.paths[*].post
  name: post-request-body
  severity: info
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description
  severity: info
- description: GUID/UUID properties should use format uuid
  given: $.components.schemas[*].properties[?(@.type == 'string' && @.description && /identifier|GUID|uuid/i.test(@.description))]
  name: uuid-format
  severity: info
- description: Operations should have x-microcks-operation for mock compatibility
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/microsoft-project-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/microsoft-project/refs/heads/main/rules/microsoft-project-spectral-rules.yml
severity_counts:
  error: 23
  hint: 0
  info: 7
  warn: 9
slug: microsoft-project-spectral-rules
source_filename: microsoft-project-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # ── INFO / METADATA ──────────────────────────────────────────────────\n\n  info-title-required:\n    description: Info object must have a title\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-title-prefix:\n    description: Title should start with \"Microsoft Project\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Microsoft Project\"\n\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-description-min-length:\n    description: Info description should be at least 50 characters\n    severity: warn\n    given: $.info.description\n    then:\n      function: length\n      functionOptions:\n        min: 50\n\n  info-version-required:\n    description: Info object must have a version\n    severity:\
  \ error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Info object should have contact information\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  # ── OPENAPI VERSION ──────────────────────────────────────────────────\n\n  openapi-version:\n    description: OpenAPI version should be 3.0.x\n    severity: error\n    given: $.openapi\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # ── SERVERS ──────────────────────────────────────────────────────────\n\n  servers-defined:\n    description: At least one server must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\
  \n\n  servers-description:\n    description: Each server should have a description\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # ── PATHS — NAMING CONVENTIONS ──────────────────────────────────────\n\n  paths-no-trailing-slash:\n    description: Paths must not end with a trailing slash\n    severity: error\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n\n  paths-no-query-strings:\n    description: Paths must not contain query strings\n    severity: error\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\?\"\n\n  # ── OPERATIONS ──────────────────────────────────────────────────────\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field:\
  \ summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"Microsoft Project\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Microsoft Project\"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-camel-case:\n    description: Operation IDs should use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n\
  \        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # ── TAGS ─────────────────────────────────────────────────────────────\n\n  tags-defined:\n    description: Global tags array should be defined\n    severity: warn\n    given: $\n    then:\n      field: tags\n      function: truthy\n\n  tag-description:\n    description: Each global tag should have a description\n    severity: info\n    given: $.tags[*]\n    then:\n      field: description\n      function: truthy\n\n  # ── PARAMETERS ──────────────────────────────────────────────────────\n\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: error\n    given: $..parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description:\
  \ Every parameter must have a schema with a type\n    severity: error\n    given: $..parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  parameter-path-required:\n    description: Path parameters must be required\n    severity: error\n    given: $..parameters[?(@.in == 'path')]\n    then:\n      field: required\n      function: truthy\n\n  # ── REQUEST BODIES ──────────────────────────────────────────────────\n\n  request-body-json:\n    description: Request bodies should use application/json content type\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      field: application/json\n      function: truthy\n\n  # ── RESPONSES ────────────────────────────────────────────────────────\n\n  response-success-required:\n    description: Every operation must define a success response (2xx)\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n\
  \        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-401-defined:\n    description: Operations should define a 401 Unauthorized response\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: '401'\n      function: truthy\n\n  # ── SCHEMAS — PROPERTY NAMING ────────────────────────────────────────\n\n  schema-type-defined:\n    description: All schemas must define a type\n    severity: error\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  schema-properties-pascal-case:\n    description: Schema properties should use PascalCase (Microsoft convention)\n    severity:\
  \ info\n    given: $.components.schemas[*].properties\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*$\"\n\n  # ── SECURITY ─────────────────────────────────────────────────────────\n\n  security-defined:\n    description: Global security must be defined\n    severity: error\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes must be defined in components\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-oauth2-scheme:\n    description: OAuth2 security scheme should be defined for SharePoint APIs\n    severity: warn\n    given: $.components.securitySchemes\n    then:\n      field: oauth2\n      function: truthy\n\n  # ── HTTP METHOD CONVENTIONS ──────────────────────────────────────────\n\n  get-no-request-body:\n    description: GET operations must not have\
  \ a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations must not have a request body\n    severity: error\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  post-request-body:\n    description: POST operations should have a request body\n    severity: info\n    given: $.paths[*].post\n    then:\n      field: requestBody\n      function: truthy\n\n  # ── GENERAL QUALITY ──────────────────────────────────────────────────\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: $..description\n    then:\n      function: truthy\n\n  schema-description:\n    description: Top-level schemas should have descriptions\n    severity: info\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  uuid-format:\n    description:\
  \ GUID/UUID properties should use format uuid\n    severity: info\n    given: $.components.schemas[*].properties[?(@.type == 'string' && @.description && /identifier|GUID|uuid/i.test(@.description))]\n    then:\n      field: format\n      function: pattern\n      functionOptions:\n        match: \"uuid\"\n\n  microcks-operation-extension:\n    description: Operations should have x-microcks-operation for mock compatibility\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/microsoft-project/refs/heads/main/rules/microsoft-project-spectral-rules.yml
tags:
- Budgeting
- Gantt Charts
- Microsoft
- Portfolio Management
- Project Management
- Resource Management
- Scheduling
- Task Management
- Spectral
- Linting
- API Governance
---
