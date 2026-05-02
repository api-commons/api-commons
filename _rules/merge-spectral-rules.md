---
api_specs:
- filename: merge-hris-api-openapi.yaml
  format: yaml
  label: Merge HRIS API
  slug: hris-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/merge/refs/heads/main/openapi/merge-hris-api-openapi.yaml
- filename: merge-ats-api-openapi.yaml
  format: yaml
  label: Merge ATS API
  slug: ats-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/merge/refs/heads/main/openapi/merge-ats-api-openapi.yaml
- filename: merge-accounting-api-openapi.yaml
  format: yaml
  label: Merge Accounting API
  slug: accounting-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/merge/refs/heads/main/openapi/merge-accounting-api-openapi.yaml
- filename: merge-ticketing-api-openapi.yaml
  format: yaml
  label: Merge Ticketing API
  slug: ticketing-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/merge/refs/heads/main/openapi/merge-ticketing-api-openapi.yaml
- filename: merge-crm-api-openapi.yaml
  format: yaml
  label: Merge CRM API
  slug: crm-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/merge/refs/heads/main/openapi/merge-crm-api-openapi.yaml
- filename: merge-file-storage-api-openapi.yaml
  format: yaml
  label: Merge File Storage API
  slug: file-storage-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/merge/refs/heads/main/openapi/merge-file-storage-api-openapi.yaml
categories:
- delete
- examples
- get
- info
- 'no'
- openapi
- operation
- pagination
- parameter
- paths
- remote
- request
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Merge.
layout: rules
name: Merge API Rules
provider_name: Merge
provider_slug: merge
rule_count: 37
rules:
- description: Info object must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: Info title should start with "Merge".
  given: $.info.title
  name: info-title-merge-prefix
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
- description: Info object should have contact information.
  given: $.info
  name: info-contact-required
  severity: warn
- description: OpenAPI version should be 3.x.
  given: $
  name: openapi-version-3
  severity: warn
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS.
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Server URL should be on api.merge.dev.
  given: $.servers[*].url
  name: servers-merge-api-domain
  severity: info
- description: Path segments should use kebab-case.
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Resource paths should use plural nouns.
  given: $.paths
  name: paths-plural-resources
  severity: info
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: operationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Merge".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-merge-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Every parameter must have a description.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Parameter names should use snake_case.
  given: $.paths[*][*].parameters[*].name
  name: parameter-snake-case
  severity: warn
- description: Merge APIs use cursor-based pagination with cursor parameter.
  given: $.paths[*].get.parameters
  name: parameter-pagination-cursor
  severity: info
- description: Request bodies should use application/json.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json
  severity: warn
- description: Every operation must have a success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Schema properties should use snake_case naming.
  given: $.components.schemas[*].properties
  name: schema-property-snake-case
  severity: warn
- description: Schemas must define a type.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description
  severity: info
- description: Global security must be defined.
  given: $
  name: security-defined
  severity: error
- description: Merge APIs should use Bearer token authentication.
  given: $.components.securitySchemes
  name: security-bearer-auth
  severity: warn
- description: Merge APIs require X-Account-Token header.
  given: $.components.securitySchemes
  name: security-account-token-header
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: List endpoints should return paginated responses with next/previous/results.
  given: $.paths[*].get.responses.200.content.application/json.schema
  name: pagination-response-format
  severity: info
- description: Merge schemas should include remote_was_deleted field for soft delete tracking.
  given: $.components.schemas[?(@.type=='object' && !@.title.match(/Paginated|Request|Error/))]
  name: remote-was-deleted-field
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/merge-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/merge/refs/heads/main/rules/merge-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 7
  warn: 15
slug: merge-spectral-rules
source_filename: merge-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # ============================================================\n  # INFO / METADATA\n  # ============================================================\n  info-title-required:\n    description: Info object must have a title.\n    given: $.info\n    severity: error\n    then:\n      field: title\n      function: truthy\n\n  info-title-merge-prefix:\n    description: Info title should start with \"Merge\".\n    given: $.info.title\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Merge\"\n\n  info-description-required:\n    description: Info object must have a description.\n    given: $.info\n    severity: error\n    then:\n      field: description\n      function: truthy\n\n  info-description-min-length:\n    description: Info description should be at least 50 characters.\n    given: $.info.description\n    severity: warn\n    then:\n      function: length\n      functionOptions:\n        min: 50\n\n  info-version-required:\n\
  \    description: Info object must have a version.\n    given: $.info\n    severity: error\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Info object should have contact information.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n\n  # ============================================================\n  # OPENAPI VERSION\n  # ============================================================\n  openapi-version-3:\n    description: OpenAPI version should be 3.x.\n    given: $\n    severity: warn\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # ============================================================\n  # SERVERS\n  # ============================================================\n  servers-defined:\n    description: At least one server must be defined.\n    given: $\n    severity: error\n    then:\n      field: servers\n   \
  \   function: truthy\n\n  servers-https:\n    description: Server URLs should use HTTPS.\n    given: $.servers[*].url\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-merge-api-domain:\n    description: Server URL should be on api.merge.dev.\n    given: $.servers[*].url\n    severity: info\n    then:\n      function: pattern\n      functionOptions:\n        match: \"api\\\\.merge\\\\.dev\"\n\n  # ============================================================\n  # PATHS - NAMING CONVENTIONS\n  # ============================================================\n  paths-kebab-case:\n    description: Path segments should use kebab-case.\n    given: $.paths\n    severity: warn\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^(\\\\/[a-z0-9-{}]+)+$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes.\n    given: $.paths\n    severity: error\n\
  \    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n\n  paths-plural-resources:\n    description: Resource paths should use plural nouns.\n    given: $.paths\n    severity: info\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/[a-z]+[^s{}]\\\\/\\\\{\"\n\n  # ============================================================\n  # OPERATIONS\n  # ============================================================\n  operation-operationid-required:\n    description: Every operation must have an operationId.\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-camel-case:\n    description: operationId should use camelCase.\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match:\
  \ \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-summary-required:\n    description: Every operation must have a summary.\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-merge-prefix:\n    description: Operation summaries should start with \"Merge\".\n    given: $.paths[*][get,post,put,patch,delete].summary\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Merge\"\n\n  operation-description-required:\n    description: Every operation must have a description.\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n    then:\n      field: description\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n    then:\n      field: tags\n      function: truthy\n\n  # ============================================================\n\
  \  # PARAMETERS\n  # ============================================================\n  parameter-description-required:\n    description: Every parameter must have a description.\n    given: $.paths[*][*].parameters[*]\n    severity: warn\n    then:\n      field: description\n      function: truthy\n\n  parameter-snake-case:\n    description: Parameter names should use snake_case.\n    given: $.paths[*][*].parameters[*].name\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_]*$\"\n\n  parameter-pagination-cursor:\n    description: Merge APIs use cursor-based pagination with cursor parameter.\n    given: $.paths[*].get.parameters\n    severity: info\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            type: object\n            properties:\n              name:\n                const: cursor\n\n  # ============================================================\n\
  \  # REQUEST BODIES\n  # ============================================================\n  request-body-json:\n    description: Request bodies should use application/json.\n    given: $.paths[*][post,put,patch].requestBody.content\n    severity: warn\n    then:\n      field: application/json\n      function: truthy\n\n  # ============================================================\n  # RESPONSES\n  # ============================================================\n  response-success-required:\n    description: Every operation must have a success response.\n    given: $.paths[*][get,post,put,patch,delete].responses\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: Every response must have a description.\n    given: $.paths[*][*].responses[*]\n    severity: error\n    then:\n\
  \      field: description\n      function: truthy\n\n  # ============================================================\n  # SCHEMAS - PROPERTY NAMING\n  # ============================================================\n  schema-property-snake-case:\n    description: Schema properties should use snake_case naming.\n    given: $.components.schemas[*].properties\n    severity: warn\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_]*$\"\n\n  schema-type-defined:\n    description: Schemas must define a type.\n    given: $.components.schemas[*]\n    severity: warn\n    then:\n      field: type\n      function: truthy\n\n  schema-description:\n    description: Top-level schemas should have descriptions.\n    given: $.components.schemas[*]\n    severity: info\n    then:\n      field: description\n      function: truthy\n\n  # ============================================================\n  # SECURITY\n  # ============================================================\n\
  \  security-defined:\n    description: Global security must be defined.\n    given: $\n    severity: error\n    then:\n      field: security\n      function: truthy\n\n  security-bearer-auth:\n    description: Merge APIs should use Bearer token authentication.\n    given: $.components.securitySchemes\n    severity: warn\n    then:\n      field: bearerAuth\n      function: truthy\n\n  security-account-token-header:\n    description: Merge APIs require X-Account-Token header.\n    given: $.components.securitySchemes\n    severity: warn\n    then:\n      field: accountToken\n      function: truthy\n\n  # ============================================================\n  # HTTP METHOD CONVENTIONS\n  # ============================================================\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    given: $.paths[*].get\n    severity: error\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description:\
  \ DELETE operations should not have a request body.\n    given: $.paths[*].delete\n    severity: warn\n    then:\n      field: requestBody\n      function: falsy\n\n  # ============================================================\n  # MERGE-SPECIFIC PATTERNS\n  # ============================================================\n  pagination-response-format:\n    description: List endpoints should return paginated responses with next/previous/results.\n    given: $.paths[*].get.responses.200.content.application/json.schema\n    severity: info\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            \"$ref\":\n              type: string\n              pattern: \"Paginated\"\n\n  remote-was-deleted-field:\n    description: Merge schemas should include remote_was_deleted field for soft delete tracking.\n    given: $.components.schemas[?(@.type=='object' && !@.title.match(/Paginated|Request|Error/))]\n    severity: info\n\
  \    then:\n      field: properties.remote_was_deleted\n      function: truthy\n\n  # ============================================================\n  # GENERAL QUALITY\n  # ============================================================\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    given: $..description\n    severity: error\n    then:\n      function: truthy\n\n  examples-encouraged:\n    description: Schema properties should include example values.\n    given: $.components.schemas[*].properties[*]\n    severity: info\n    then:\n      field: example\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/merge/refs/heads/main/rules/merge-spectral-rules.yml
tags:
- Integrations
- Platform
- Unified API
- Spectral
- Linting
- API Governance
---
