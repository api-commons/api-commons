---
api_specs:
- filename: bettercloud-platform-api.yaml
  format: yaml
  label: BetterCloud Platform API
  slug: bettercloud-platform-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/bettercloud/refs/heads/main/openapi/bettercloud-platform-api.yaml
categories:
- http
- info
- 'no'
- openapi
- operation
- pagination
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for BetterCloud.
layout: rules
name: BetterCloud API Rules
provider_name: BetterCloud
provider_slug: bettercloud
rule_count: 28
rules:
- description: API title should start with "BetterCloud"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must specify a version
  given: $.info
  name: info-version-required
  severity: error
- description: Should use OpenAPI 3.0.x
  given: $.openapi
  name: openapi-version
  severity: warn
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "BetterCloud"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Operations should have descriptions
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: All operations must have operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: Operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Parameters must have schemas
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Operations must define a success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Response descriptions are required
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Error schema must have code, id, href, and reason fields
  given: $.components.schemas.ErrorResponse.required
  name: schema-error-required-fields
  severity: error
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security should be defined
  given: $
  name: security-global-defined
  severity: warn
- description: BetterCloud uses API key in header (X-API-Key)
  given: $.components.securitySchemes[*][?(@.type=='apiKey')]
  name: security-api-key-header
  severity: info
- description: GET operations should not have request bodies
  given: $.paths[*].get
  name: http-get-no-body
  severity: error
- description: DELETE operations should not have request bodies
  given: $.paths[*].delete
  name: http-delete-no-body
  severity: warn
- description: POST operations creating resources should have request bodies
  given: $.paths[*].post
  name: http-post-has-body
  severity: warn
- description: List endpoints should support page parameter
  given: $.paths[*].get.parameters[?(@.name=='page')].schema.type
  name: pagination-page-parameter
  severity: info
- description: Descriptions should not be empty
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/bettercloud-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/bettercloud/refs/heads/main/rules/bettercloud-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 2
  warn: 13
slug: bettercloud-spectral-rules
source_filename: bettercloud-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title should start with \"BetterCloud\"\n    message: \"Info title should start with 'BetterCloud' — got '{{value}}'\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^BetterCloud\"\n\n  info-description-required:\n    description: API info must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must specify a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description: Should use OpenAPI 3.0.x\n    severity: warn\n    given: $.openapi\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be\
  \ defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9-{}]+)+$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: error\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n\
  \    description: Operation summaries should start with \"BetterCloud\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^BetterCloud\"\n\n  operation-description-required:\n    description: Operations should have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: All operations must have operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId should use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: Operations\
  \ must have tags\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Parameters must have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Parameters must have schemas\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must define a success response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-description-required:\n    description: Response descriptions\
  \ are required\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-error-required-fields:\n    description: Error schema must have code, id, href, and reason fields\n    severity: error\n    given: $.components.schemas.ErrorResponse.required\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            type: string\n            enum:\n              - code\n              - id\n              - href\n              - reason\n\n  schema-description-required:\n    description: Component schemas should have descriptions\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n\
  \      function: truthy\n\n  security-global-defined:\n    description: Global security should be defined\n    severity: warn\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  security-api-key-header:\n    description: BetterCloud uses API key in header (X-API-Key)\n    severity: info\n    given: $.components.securitySchemes[*][?(@.type=='apiKey')]\n    then:\n      field: in\n      function: enumeration\n      functionOptions:\n        values:\n          - header\n\n  # HTTP METHODS\n  http-get-no-body:\n    description: GET operations should not have request bodies\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  http-delete-no-body:\n    description: DELETE operations should not have request bodies\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  http-post-has-body:\n    description: POST operations creating resources should have\
  \ request bodies\n    severity: warn\n    given: $.paths[*].post\n    then:\n      field: requestBody\n      function: truthy\n\n  # PAGINATION\n  pagination-page-parameter:\n    description: List endpoints should support page parameter\n    severity: info\n    given: $.paths[*].get.parameters[?(@.name=='page')].schema.type\n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - integer\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions should not be empty\n    severity: warn\n    given: $..description\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/bettercloud/refs/heads/main/rules/bettercloud-spectral-rules.yml
tags:
- Automation
- Compliance
- Enterprise
- IT Operations
- SaaS Management
- Security
- Workflows
- User Lifecycle
- Spectral
- Linting
- API Governance
---
