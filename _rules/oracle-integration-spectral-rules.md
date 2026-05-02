---
api_specs:
- filename: oracle-integration-developer-api.yaml
  format: yaml
  label: Oracle Integration Developer API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/oracle-integration/refs/heads/main/openapi/oracle-integration-developer-api.yaml
- filename: oracle-integration-process-automation-api.yaml
  format: yaml
  label: Oracle Integration Process Automation API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/oracle-integration/refs/heads/main/openapi/oracle-integration-process-automation-api.yaml
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
- request
- response
- schema
- security
- servers
- tag
description: Spectral linting rules defining API design standards and conventions for Oracle Integration.
layout: rules
name: Oracle Integration API Rules
provider_name: Oracle Integration
provider_slug: oracle-integration
rule_count: 36
rules:
- description: Info title must start with "Oracle Integration".
  given: $.info.title
  name: info-title-must-start-with-oracle
  severity: error
- description: Info description is required and must be at least 50 characters.
  given: $.info
  name: info-description-required
  severity: error
- description: Info version is required.
  given: $.info
  name: info-version-required
  severity: error
- description: Info contact information is required.
  given: $.info
  name: info-contact-required
  severity: warn
- description: Info license information is required.
  given: $.info
  name: info-license-required
  severity: warn
- description: OpenAPI version must be 3.0.x.
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https-required
  severity: error
- description: Each server must have a description.
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Path segments should use kebab-case or camelCase consistently.
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Paths must not have a trailing slash.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Paths must not contain query strings.
  given: $.paths
  name: paths-no-query-strings
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Oracle Integration".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Operation IDs should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Global tags should have descriptions.
  given: $.tags[*]
  name: tag-description-required
  severity: info
- description: Tag names should use Title Case.
  given: $.tags[*].name
  name: tag-title-case
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema with a type.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: info
- description: Every operation must have a 2xx success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should include a 401 Unauthorized response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-recommended
  severity: warn
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Schema property names should use camelCase.
  given: $.components.schemas[*].properties
  name: schema-properties-camelcase
  severity: warn
- description: Schemas must have a type defined.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: error
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*].properties[*]
  name: schema-description-recommended
  severity: info
- description: Global security must be defined.
  given: $
  name: security-global-defined
  severity: error
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: GET operations should not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings.
  given: $.paths[*][get,post,put,patch,delete].description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
- description: Operations should include x-microcks-operation for mock server compatibility.
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-extension-recommended
  severity: info
rules_file: rules/oracle-integration-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/oracle-integration/refs/heads/main/rules/oracle-integration-spectral-rules.yml
severity_counts:
  error: 19
  hint: 0
  info: 6
  warn: 11
slug: oracle-integration-spectral-rules
source_filename: oracle-integration-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # ============================================================\n  # INFO / METADATA\n  # ============================================================\n  info-title-must-start-with-oracle:\n    description: Info title must start with \"Oracle Integration\".\n    severity: error\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: ^Oracle Integration\n  info-description-required:\n    description: Info description is required and must be at least 50 characters.\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: length\n      functionOptions:\n        min: 50\n  info-version-required:\n    description: Info version is required.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  info-contact-required:\n    description: Info contact information is required.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n \
  \     function: truthy\n  info-license-required:\n    description: Info license information is required.\n    severity: warn\n    given: $.info\n    then:\n      field: license\n      function: truthy\n\n  # ============================================================\n  # OPENAPI VERSION\n  # ============================================================\n  openapi-version-3:\n    description: OpenAPI version must be 3.0.x.\n    severity: error\n    given: $.openapi\n    then:\n      function: pattern\n      functionOptions:\n        match: ^3\\.0\\.\\d+$\n\n  # ============================================================\n  # SERVERS\n  # ============================================================\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: length\n      functionOptions:\n        min: 1\n  servers-https-required:\n    description: Server URLs must use HTTPS.\n    severity:\
  \ error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: ^https://\n  servers-description-required:\n    description: Each server must have a description.\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # ============================================================\n  # PATHS — NAMING CONVENTIONS\n  # ============================================================\n  paths-kebab-case:\n    description: Path segments should use kebab-case or camelCase consistently.\n    severity: info\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        match: ^(/[a-z][a-zA-Z0-9{}-]*)+$\n  paths-no-trailing-slash:\n    description: Paths must not have a trailing slash.\n    severity: error\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: '/$'\n  paths-no-query-strings:\n    description: Paths must not contain\
  \ query strings.\n    severity: error\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: '\\?'\n\n  # ============================================================\n  # OPERATIONS\n  # ============================================================\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n  operation-summary-prefix:\n    description: Operation summaries should start with \"Oracle Integration\".\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: ^Oracle Integration\n  operation-description-required:\n    description: Every operation must have a description.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function:\
  \ truthy\n  operation-operationid-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n  operation-operationid-camelcase:\n    description: Operation IDs should use camelCase.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: ^[a-z][a-zA-Z0-9]*$\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: length\n      functionOptions:\n        min: 1\n\n  # ============================================================\n  # TAGS\n  # ============================================================\n  tag-description-required:\n    description: Global tags should have descriptions.\n    severity:\
  \ info\n    given: $.tags[*]\n    then:\n      field: description\n      function: truthy\n  tag-title-case:\n    description: Tag names should use Title Case.\n    severity: warn\n    given: $.tags[*].name\n    then:\n      function: pattern\n      functionOptions:\n        match: ^[A-Z][a-zA-Z0-9]+([ ][A-Z][a-zA-Z0-9]+)*$\n\n  # ============================================================\n  # PARAMETERS\n  # ============================================================\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n  parameter-schema-required:\n    description: Every parameter must have a schema with a type.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  # ============================================================\n\
  \  # REQUEST BODIES\n  # ============================================================\n  request-body-json-content:\n    description: Request bodies should use application/json content type.\n    severity: info\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      field: application/json\n      function: truthy\n\n  # ============================================================\n  # RESPONSES\n  # ============================================================\n  response-success-required:\n    description: Every operation must have a 2xx success response.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n  response-401-recommended:\n    description: Operations should include a 401 Unauthorized response.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n\
  \    then:\n      field: '401'\n      function: truthy\n  response-description-required:\n    description: Every response must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # ============================================================\n  # SCHEMAS — PROPERTY NAMING\n  # ============================================================\n  schema-properties-camelcase:\n    description: Schema property names should use camelCase.\n    severity: warn\n    given: $.components.schemas[*].properties\n    then:\n      function: pattern\n      functionOptions:\n        match: ^[a-z][a-zA-Z0-9]*$\n  schema-type-defined:\n    description: Schemas must have a type defined.\n    severity: error\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n  schema-description-recommended:\n    description: Top-level schemas should have descriptions.\n\
  \    severity: info\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: description\n      function: truthy\n\n  # ============================================================\n  # SECURITY\n  # ============================================================\n  security-global-defined:\n    description: Global security must be defined.\n    severity: error\n    given: $\n    then:\n      field: security\n      function: truthy\n  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # ============================================================\n  # HTTP METHOD CONVENTIONS\n  # ============================================================\n  get-no-request-body:\n    description: GET operations should not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n    \
  \  function: falsy\n  delete-no-request-body:\n    description: DELETE operations should not have a request body.\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  # ============================================================\n  # GENERAL QUALITY\n  # ============================================================\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].description\n    then:\n      function: length\n      functionOptions:\n        min: 1\n  examples-encouraged:\n    description: Schema properties should include example values.\n    severity: info\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: example\n      function: truthy\n  microcks-extension-recommended:\n    description: Operations should include x-microcks-operation for mock server compatibility.\n    severity: info\n    given:\
  \ $.paths[*][get,post,put,patch,delete]\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/oracle-integration/refs/heads/main/rules/oracle-integration-spectral-rules.yml
tags:
- API Management
- Automation
- B2B Integration
- Cloud Integration
- Enterprise Integration
- Integration
- iPaaS
- Process Automation
- Spectral
- Linting
- API Governance
---
