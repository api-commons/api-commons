---
api_specs:
- filename: backblaze-b2-native-api.yaml
  format: yaml
  label: Backblaze B2 Cloud Storage API
  slug: backblaze-b2-cloud-storage-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/backblaze/refs/heads/main/openapi/backblaze-b2-native-api.yaml
categories:
- components
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
description: Spectral linting rules defining API design standards and conventions for Backblaze.
layout: rules
name: Backblaze API Rules
provider_name: Backblaze
provider_slug: backblaze
rule_count: 31
rules:
- description: Info must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: Info must have a description
  given: $.info
  name: info-description-required
  severity: warn
- description: Info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Info should have contact information
  given: $.info
  name: info-contact-required
  severity: info
- description: Must use OpenAPI 3.0.x
  given: $
  name: openapi-version-3
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: B2 Native API paths should use /b2api/v{version}/ prefix
  given: $.paths
  name: paths-b2-api-prefix
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: OperationIds should use camelCase
  given: $.paths[*][get,post,put,patch,delete,head,options].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: warn
- description: Operation summaries should start with "Backblaze B2"
  given: $.paths[*][get,post,put,patch,delete,head,options].summary
  name: operation-summary-backblaze-prefix
  severity: info
- description: Global tags array should be defined
  given: $
  name: tags-global-defined
  severity: info
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete,head,options].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters must have a schema
  given: $.paths[*][get,post,put,patch,delete,head,options].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should have descriptions
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: info
- description: Every operation must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations with auth should define 401 response
  given: $.paths[*][post,get]
  name: response-401-defined
  severity: warn
- description: All schemas should have a type
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: All component schemas should have a title
  given: $.components.schemas[*]
  name: schema-title-defined
  severity: info
- description: All component schemas should have a description
  given: $.components.schemas[*]
  name: schema-description-defined
  severity: info
- description: Security schemes must be defined in components
  given: $.components
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
- description: POST operations should have a request body
  given: $.paths[*].post
  name: post-b2-operations-have-request-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Spec should define reusable schemas in components
  given: $.components
  name: components-schemas-present
  severity: info
rules_file: rules/backblaze-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/backblaze/refs/heads/main/rules/backblaze-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 7
  warn: 12
slug: backblaze-spectral-rules
source_filename: backblaze-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: Info must have a title\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: Info must have a description\n    severity: warn\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info must have a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Info should have contact information\n    severity: info\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.0.x\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-defined:\n\
  \    description: Servers must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS — NAMING CONVENTIONS\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: warn\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  paths-b2-api-prefix:\n    description: B2 Native API paths should use /b2api/v{version}/ prefix\n    severity: warn\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/b2api/\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n\
  \    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: OperationIds should use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field:\
  \ tags\n      function: truthy\n\n  operation-summary-backblaze-prefix:\n    description: Operation summaries should start with \"Backblaze B2\"\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete,head,options].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Backblaze\"\n\n  # TAGS\n  tags-global-defined:\n    description: Global tags array should be defined\n    severity: info\n    given: $\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: All parameters must have a schema\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options].parameters[*]\n    then:\n      field: schema\n      function:\
  \ truthy\n\n  # REQUEST BODIES\n  request-body-description:\n    description: Request bodies should have descriptions\n    severity: info\n    given: $.paths[*][post,put,patch].requestBody\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have at least one 2xx response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: responses\n      function: truthy\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-401-defined:\n    description: Operations with auth should define 401 response\n    severity: warn\n    given: $.paths[*][post,get]\n    then:\n      field: responses.401\n      function: truthy\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-type-defined:\n\
  \    description: All schemas should have a type\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  schema-title-defined:\n    description: All component schemas should have a title\n    severity: info\n    given: $.components.schemas[*]\n    then:\n      field: title\n      function: truthy\n\n  schema-description-defined:\n    description: All component schemas should have a description\n    severity: info\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: Global security should be defined\n    severity: warn\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n\
  \  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  post-b2-operations-have-request-body:\n    description: POST operations should have a request body\n    severity: warn\n    given: $.paths[*].post\n    then:\n      field: requestBody\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: warn\n    given: $..description\n    then:\n      function: truthy\n\n  components-schemas-present:\n    description: Spec should define reusable schemas in components\n    severity: info\n    given: $.components\n    then:\n      field: schemas\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/backblaze/refs/heads/main/rules/backblaze-spectral-rules.yml
tags:
- Cloud Storage
- Object Storage
- Storage
- Backup
- Spectral
- Linting
- API Governance
---
