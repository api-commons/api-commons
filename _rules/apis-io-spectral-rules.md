---
api_specs:
- filename: apis-io-search-openapi.yaml
  format: yaml
  label: APIs.io Search API
  slug: search-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apis-io/refs/heads/main/openapi/apis-io-search-openapi.yaml
categories:
- apis
- components
- examples
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
- servers
- tag
- tags
description: Spectral linting rules defining API design standards and conventions for APIs.io.
layout: rules
name: APIs.io API Rules
provider_name: APIs.io
provider_slug: apis-io
rule_count: 37
rules:
- description: Info title should start with "APIs.io"
  given: $.info.title
  name: info-title-format
  severity: warn
- description: Info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Info should include contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Specs should use OpenAPI 3.1.x as established by the APIs.io API
  given: $.openapi
  name: openapi-version-31
  severity: warn
- description: Servers array must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "APIs.io"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Operation summaries should use Title Case
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-title-case
  severity: info
- description: All operations should have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: OperationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined
  given: $
  name: tags-defined
  severity: warn
- description: All global tags should have descriptions
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: All parameters must have a schema
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Parameter names should use snake_case
  given: $.paths[*][*].parameters[*].name
  name: parameter-names-snake-case
  severity: warn
- description: Request bodies should have descriptions
  given: $.paths[*][*].requestBody
  name: request-body-description-required
  severity: warn
- description: Request bodies should support application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: GET and POST operations must have a 2xx response
  given: $.paths[*][get,post]
  name: response-200-required
  severity: error
- description: All responses must have descriptions
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Operations should include a 400 Bad Request response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-400-recommended
  severity: warn
- description: Operations should include a 401 Unauthorized response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-recommended
  severity: warn
- description: Operations should include a 500 Internal Server Error response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-500-recommended
  severity: warn
- description: Schema property names should use snake_case
  given: $.components.schemas[*].properties[*]~
  name: schema-properties-snake-case
  severity: info
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: info
- description: Schema objects should have a type defined
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes should be defined in components
  given: $.components
  name: components-security-schemes-defined
  severity: info
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: POST operations should have a request body
  given: $.paths[*].post
  name: post-has-request-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should include examples
  given: $.components.schemas[*].properties[*]
  name: examples-on-schemas
  severity: info
- description: APIs submitted to APIs.io should follow APIs.json format
  given: $.paths[*][post].requestBody.content.application/json.schema
  name: apis-json-format-validation
  severity: info
rules_file: rules/apis-io-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apis-io/refs/heads/main/rules/apis-io-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 6
  warn: 18
slug: apis-io-spectral-rules
source_filename: apis-io-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-format:\n    description: Info title should start with \"APIs.io\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^APIs\\\\.io\"\n\n  info-description-required:\n    description: Info must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Info should include contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-31:\n    description: Specs should use OpenAPI 3.1.x as established by the APIs.io API\n    severity: warn\n    given: \"$.openapi\"\n    then:\n      function:\
  \ pattern\n      functionOptions:\n        match: \"^3\\\\.1\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers array must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(\\\\/([a-z0-9-{}._]+))*$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n \
  \   description: All operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"APIs.io\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^APIs\\\\.io\"\n\n  operation-summary-title-case:\n    description: Operation summaries should use Title Case\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z]\"\n\n  operation-description-required:\n    description: All operations should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n\
  \    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: OperationId should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: All operations must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tags-defined:\n    description: Global tags array should be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  tag-description-required:\n    description: All global tags should have descriptions\n    severity: warn\n    given:\
  \ \"$.tags[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: error\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: All parameters must have a schema\n    severity: error\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  parameter-names-snake-case:\n    description: Parameter names should use snake_case\n    severity: warn\n    given: \"$.paths[*][*].parameters[*].name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_]*$\"\n\n  # REQUEST BODIES\n  request-body-description-required:\n    description: Request bodies should have descriptions\n    severity: warn\n    given: \"$.paths[*][*].requestBody\"\n    then:\n      field: description\n      function:\
  \ truthy\n\n  request-body-json-content:\n    description: Request bodies should support application/json content type\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      field: application/json\n      function: truthy\n\n  # RESPONSES\n  response-200-required:\n    description: GET and POST operations must have a 2xx response\n    severity: error\n    given: \"$.paths[*][get,post]\"\n    then:\n      field: responses\n      function: truthy\n\n  response-description-required:\n    description: All responses must have descriptions\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-400-recommended:\n    description: Operations should include a 400 Bad Request response\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      field: \"400\"\n      function: truthy\n\n  response-401-recommended:\n    description:\
  \ Operations should include a 401 Unauthorized response\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      field: \"401\"\n      function: truthy\n\n  response-500-recommended:\n    description: Operations should include a 500 Internal Server Error response\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      field: \"500\"\n      function: truthy\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-properties-snake-case:\n    description: Schema property names should use snake_case\n    severity: info\n    given: \"$.components.schemas[*].properties[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_]*$\"\n\n  schema-description-recommended:\n    description: Component schemas should have descriptions\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-type-defined:\n  \
  \  description: Schema objects should have a type defined\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  components-security-schemes-defined:\n    description: Security schemes should be defined in components\n    severity: info\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  post-has-request-body:\n    description: POST operations should have a request body\n    severity: warn\n    given: \"$.paths[*].post\"\n    then:\n      field: requestBody\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: \"$..description\"\n\
  \    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  examples-on-schemas:\n    description: Schema properties should include examples\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: example\n      function: truthy\n\n  apis-json-format-validation:\n    description: APIs submitted to APIs.io should follow APIs.json format\n    severity: info\n    given: \"$.paths[*][post].requestBody.content.application/json.schema\"\n    then:\n      field: $ref\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apis-io/refs/heads/main/rules/apis-io-spectral-rules.yml
tags:
- API Aggregation
- API Directory
- API Discovery
- API Indexing
- API Rating
- API Search
- APIs.json
- Search Engine
- Spectral
- Linting
- API Governance
---
