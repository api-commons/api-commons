---
api_specs:
- filename: acquia-cloud-applications.yml
  format: yaml
  label: Acquia Cloud API
  slug: acquia-cloud-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/openapi/acquia-cloud-applications.yml
categories:
- actions
- delete
- get
- hal
- info
- 'no'
- openapi
- operation
- parameter
- paths
- post
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Acquia.
layout: rules
name: Acquia API Rules
provider_name: Acquia
provider_slug: acquia
rule_count: 32
rules:
- description: OpenAPI info.title must be present and non-empty
  given: $.info
  name: info-title-required
  severity: error
- description: OpenAPI info.description must be present
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
- description: Acquia APIs must use OpenAPI 3.x
  given: $
  name: openapi-version-3x
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https
  severity: error
- description: Acquia Cloud API server should use cloud.acquia.com domain
  given: $.servers[*]
  name: servers-acquia-cloud-domain
  severity: info
- description: Paths must not end with a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: Resource identifiers in paths should use UUID suffix pattern
  given: $.paths[*]~
  name: paths-uuid-format
  severity: info
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
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Operation summaries should start with 'Acquia'
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-acquia-prefix
  severity: info
- description: Global tags array should be defined
  given: $
  name: tags-global-defined
  severity: warn
- description: All parameters should have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: UUID path parameters should end with 'Uuid' suffix
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in == 'path')]
  name: parameter-uuid-naming
  severity: info
- description: All operations must define at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Protected endpoints should define 401 Unauthorized responses
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-unauthorized
  severity: warn
- description: Protected endpoints should define 403 Forbidden responses
  given: $.paths[*][post,put,patch,delete].responses
  name: response-403-forbidden
  severity: warn
- description: Schema components should define a type
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes must be defined in components
  given: $
  name: security-schemes-defined
  severity: error
- description: Acquia Cloud API uses OAuth2 authentication
  given: $.components.securitySchemes[*]
  name: security-oauth2-scheme
  severity: info
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: POST operations creating resources should have a request body
  given: $.paths[*].post
  name: post-has-request-body
  severity: info
- description: Action endpoints should follow /resources/{id}/actions/{action-name} pattern
  given: $.paths[*~\/actions\/]~
  name: actions-paths-pattern
  severity: info
- description: Acquia Cloud API responses use application/hal+json content type
  given: $.paths[*][get,post,put,patch,delete].responses[*].content
  name: hal-json-content-type
  severity: info
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/acquia-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/rules/acquia-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 8
  warn: 10
slug: acquia-spectral-rules
source_filename: acquia-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: OpenAPI info.title must be present and non-empty\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: OpenAPI info.description must be present\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: OpenAPI info.version must be defined\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API info should include contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3x:\n    description: Acquia APIs must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n     \
  \ functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: At least one server must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-acquia-cloud-domain:\n    description: Acquia Cloud API server should use cloud.acquia.com domain\n    severity: info\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"acquia\\\\.com\"\n\n  # PATHS — NAMING CONVENTIONS\n  paths-no-trailing-slash:\n    description: Paths must not end with a trailing slash\n    severity: error\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n\n  paths-uuid-format:\n\
  \    description: Resource identifiers in paths should use UUID suffix pattern\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^\\\\/\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: All operations should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: All operations must have at least one tag\n    severity:\
  \ error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  operation-summary-acquia-prefix:\n    description: Operation summaries should start with 'Acquia'\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Acquia \"\n\n  # TAGS\n  tags-global-defined:\n    description: Global tags array should be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: All parameters must have a schema\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\
  \n    then:\n      field: schema\n      function: truthy\n\n  parameter-uuid-naming:\n    description: UUID path parameters should end with 'Uuid' suffix\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[?(@.in == 'path')]\"\n    then:\n      field: name\n      function: pattern\n      functionOptions:\n        match: \"Uuid$|Id$|Name$\"\n\n  # RESPONSES\n  response-success-required:\n    description: All operations must define at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"202\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\
  \n    then:\n      field: description\n      function: truthy\n\n  response-401-unauthorized:\n    description: Protected endpoints should define 401 Unauthorized responses\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [\"401\"]\n\n  response-403-forbidden:\n    description: Protected endpoints should define 403 Forbidden responses\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [\"403\"]\n\n  # SCHEMAS\n  schema-type-defined:\n    description: Schema components should define a type\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be\
  \ defined in components\n    severity: error\n    given: \"$\"\n    then:\n      field: components.securitySchemes\n      function: truthy\n\n  security-oauth2-scheme:\n    description: Acquia Cloud API uses OAuth2 authentication\n    severity: info\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      field: type\n      function: pattern\n      functionOptions:\n        match: \"oauth2\"\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  post-has-request-body:\n    description: POST operations creating resources should have a request body\n    severity: info\n    given: \"$.paths[*].post\"\
  \n    then:\n      field: requestBody\n      function: truthy\n\n  # ACQUIA-SPECIFIC CONVENTIONS\n  actions-paths-pattern:\n    description: Action endpoints should follow /resources/{id}/actions/{action-name} pattern\n    severity: info\n    given: \"$.paths[*~\\\\/actions\\\\/]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"\\\\/actions\\\\/\"\n\n  hal-json-content-type:\n    description: Acquia Cloud API responses use application/hal+json content type\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*].content\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"application/hal+json\"]\n            - required: [\"application/json\"]\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: pattern\n\
  \      functionOptions:\n        match: \".+\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/rules/acquia-spectral-rules.yml
tags:
- Content
- Experience
- Spectral
- Linting
- API Governance
---
