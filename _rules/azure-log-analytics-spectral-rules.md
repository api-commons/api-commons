---
api_specs:
- filename: azure-log-analytics-query-api.yaml
  format: yaml
  label: Azure Log Analytics Query API
  slug: azure-log-analytics-query-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/azure-log-analytics/refs/heads/main/openapi/azure-log-analytics-query-api.yaml
- filename: azure-log-analytics-management-api.yaml
  format: yaml
  label: Azure Log Analytics Management API
  slug: azure-log-analytics-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/azure-log-analytics/refs/heads/main/openapi/azure-log-analytics-management-api.yaml
- filename: azure-log-analytics-ingestion-api.yaml
  format: yaml
  label: Azure Log Analytics Ingestion API
  slug: azure-log-analytics-ingestion-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/azure-log-analytics/refs/heads/main/openapi/azure-log-analytics-ingestion-api.yaml
categories:
- delete
- examples
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
description: Spectral linting rules defining API design standards and conventions for Azure Log Analytics.
layout: rules
name: Azure Log Analytics API Rules
provider_name: Azure Log Analytics
provider_slug: azure-log-analytics
rule_count: 41
rules:
- description: Info object must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: Info title must start with "Azure Log Analytics".
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info object must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: Info description should be at least 50 characters.
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: Info object must have a version.
  given: $.info
  name: info-version-required
  severity: error
- description: Info should include contact information.
  given: $.info
  name: info-contact-required
  severity: warn
- description: Info should include license information.
  given: $.info
  name: info-license-required
  severity: info
- description: OpenAPI version must be 3.0.x.
  given: $.openapi
  name: openapi-version
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS.
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: Each server should have a description.
  given: $.servers[*]
  name: servers-description
  severity: info
- description: Path segments should use kebab-case or camelCase.
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Paths must not include query strings.
  given: $.paths
  name: paths-no-query-strings
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Azure Log Analytics".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: operationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Global tags should have descriptions.
  given: $.tags[*]
  name: tag-description
  severity: info
- description: Tag names should use Title Case.
  given: $.tags[*].name
  name: tag-title-case
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: Every parameter must have a schema with type.
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Parameter names should use camelCase.
  given: $.paths[*][*].parameters[*].name
  name: parameter-camelcase
  severity: info
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Operations with security should include a 401 response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-error-401
  severity: info
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schemas must define a type.
  given: $.components.schemas[*]
  name: schema-type-required
  severity: error
- description: Schema property names should use camelCase or PascalCase.
  given: $.components.schemas[*].properties
  name: schema-property-camelcase
  severity: info
- description: Global security must be defined.
  given: $
  name: security-defined
  severity: error
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Security schemes should have descriptions.
  given: $.components.securitySchemes[*]
  name: security-scheme-description
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: POST operations should have a request body.
  given: $.paths[*].post
  name: post-request-body-required
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should include examples.
  given: $.paths[*][get,post,put,patch].responses.200.content.application/json
  name: examples-encouraged
  severity: info
- description: Operations should include x-microcks-operation extension.
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/azure-log-analytics-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/azure-log-analytics/refs/heads/main/rules/azure-log-analytics-spectral-rules.yml
severity_counts:
  error: 20
  hint: 0
  info: 10
  warn: 11
slug: azure-log-analytics-spectral-rules
source_filename: azure-log-analytics-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # ──────────────────────────────────────────────\n  # INFO / METADATA\n  # ──────────────────────────────────────────────\n\n  info-title-required:\n    description: Info object must have a title.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-title-prefix:\n    description: Info title must start with \"Azure Log Analytics\".\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: ^Azure Log Analytics\n\n  info-description-required:\n    description: Info object must have a description.\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-description-min-length:\n    description: Info description should be at least 50 characters.\n    severity: warn\n    given: $.info.description\n    then:\n      function: length\n      functionOptions:\n        min: 50\n\n  info-version-required:\n\
  \    description: Info object must have a version.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Info should include contact information.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  info-license-required:\n    description: Info should include license information.\n    severity: info\n    given: $.info\n    then:\n      field: license\n      function: truthy\n\n  # ──────────────────────────────────────────────\n  # OPENAPI VERSION\n  # ──────────────────────────────────────────────\n\n  openapi-version:\n    description: OpenAPI version must be 3.0.x.\n    severity: error\n    given: $.openapi\n    then:\n      function: pattern\n      functionOptions:\n        match: ^3\\.0\\.\\d+$\n\n  # ──────────────────────────────────────────────\n  # SERVERS\n  # ──────────────────────────────────────────────\n\n  servers-defined:\n    description:\
  \ At least one server must be defined.\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs should use HTTPS.\n    severity: warn\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: ^https://\n\n  servers-description:\n    description: Each server should have a description.\n    severity: info\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # ──────────────────────────────────────────────\n  # PATHS — NAMING CONVENTIONS\n  # ──────────────────────────────────────────────\n\n  paths-kebab-case:\n    description: Path segments should use kebab-case or camelCase.\n    severity: info\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: ^(/[a-zA-Z0-9{}_-]+)+$\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes.\n\
  \    severity: error\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: .+/$\n\n  paths-no-query-strings:\n    description: Paths must not include query strings.\n    severity: error\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \\?\n\n  # ──────────────────────────────────────────────\n  # OPERATIONS\n  # ──────────────────────────────────────────────\n\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"Azure Log Analytics\".\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: ^Azure Log Analytics\n\
  \n  operation-description-required:\n    description: Every operation must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-camelcase:\n    description: operationId should use camelCase.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: ^[a-z][a-zA-Z0-9]*$\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # ──────────────────────────────────────────────\n  #\
  \ TAGS\n  # ──────────────────────────────────────────────\n\n  tag-description:\n    description: Global tags should have descriptions.\n    severity: info\n    given: $.tags[*]\n    then:\n      field: description\n      function: truthy\n\n  tag-title-case:\n    description: Tag names should use Title Case.\n    severity: warn\n    given: $.tags[*].name\n    then:\n      function: pattern\n      functionOptions:\n        match: ^[A-Z][a-zA-Z0-9]*(\\s[A-Z][a-zA-Z0-9]*)*$\n\n  # ──────────────────────────────────────────────\n  # PARAMETERS\n  # ──────────────────────────────────────────────\n\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Every parameter must have a schema with type.\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field:\
  \ schema\n      function: truthy\n\n  parameter-camelcase:\n    description: Parameter names should use camelCase.\n    severity: info\n    given: $.paths[*][*].parameters[*].name\n    then:\n      function: pattern\n      functionOptions:\n        match: ^[a-z][a-zA-Z0-9_-]*$\n\n  # ──────────────────────────────────────────────\n  # REQUEST BODIES\n  # ──────────────────────────────────────────────\n\n  request-body-json-content:\n    description: Request bodies should use application/json content type.\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      field: application/json\n      function: truthy\n\n  # ──────────────────────────────────────────────\n  # RESPONSES\n  # ──────────────────────────────────────────────\n\n  response-success-required:\n    description: Every operation must define at least one 2xx response.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n\
  \      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"202\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: Every response must have a description.\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-error-401:\n    description: Operations with security should include a 401 response.\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"401\"]\n            - required: [\"default\"]\n\n  # ──────────────────────────────────────────────\n  # SCHEMAS — PROPERTY NAMING\n  # ──────────────────────────────────────────────\n\n  schema-description-required:\n    description: Top-level schemas should have descriptions.\n    severity:\
  \ warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-type-required:\n    description: Schemas must define a type.\n    severity: error\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  schema-property-camelcase:\n    description: Schema property names should use camelCase or PascalCase.\n    severity: info\n    given: $.components.schemas[*].properties\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: ^[a-zA-Z][a-zA-Z0-9_]*$\n\n  # ──────────────────────────────────────────────\n  # SECURITY\n  # ──────────────────────────────────────────────\n\n  security-defined:\n    description: Global security must be defined.\n    severity: error\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    severity: error\n    given:\
  \ $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-scheme-description:\n    description: Security schemes should have descriptions.\n    severity: warn\n    given: $.components.securitySchemes[*]\n    then:\n      field: description\n      function: truthy\n\n  # ──────────────────────────────────────────────\n  # HTTP METHOD CONVENTIONS\n  # ──────────────────────────────────────────────\n\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body.\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  post-request-body-required:\n    description: POST operations should have a request body.\n    severity: info\n    given: $.paths[*].post\n    then:\n     \
  \ field: requestBody\n      function: truthy\n\n  # ──────────────────────────────────────────────\n  # GENERAL QUALITY\n  # ──────────────────────────────────────────────\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: error\n    given: $..description\n    then:\n      function: truthy\n\n  examples-encouraged:\n    description: Operations should include examples.\n    severity: info\n    given: $.paths[*][get,post,put,patch].responses.200.content.application/json\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"example\"]\n            - required: [\"examples\"]\n\n  microcks-operation-extension:\n    description: Operations should include x-microcks-operation extension.\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/azure-log-analytics/refs/heads/main/rules/azure-log-analytics-spectral-rules.yml
tags:
- Analytics
- Azure
- Cloud
- Logging
- Monitoring
- Spectral
- Linting
- API Governance
---
