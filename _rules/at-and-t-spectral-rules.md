---
api_specs:
- filename: at-and-t-sms-api.yaml
  format: yaml
  label: AT&T SMS API
  slug: att-sms-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/at-and-t/refs/heads/main/openapi/at-and-t-sms-api.yaml
- filename: at-and-t-in-app-messaging-api.yaml
  format: yaml
  label: AT&T In-App Messaging API
  slug: att-in-app-messaging-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/at-and-t/refs/heads/main/openapi/at-and-t-in-app-messaging-api.yaml
- filename: at-and-t-mvnx-api.yaml
  format: yaml
  label: AT&T MVNX API
  slug: att-mvnx-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/at-and-t/refs/heads/main/openapi/at-and-t-mvnx-api.yaml
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
description: Spectral linting rules defining API design standards and conventions for AT&T.
layout: rules
name: AT&T API Rules
provider_name: AT&T
provider_slug: at-and-t
rule_count: 37
rules:
- description: API title must start with "AT&T"
  given: $.info.title
  name: info-title-pattern
  severity: warn
- description: API info must have a non-empty description
  given: $.info
  name: info-description-required
  severity: error
- description: API info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: API info should have contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: API info should include a termsOfService URL
  given: $.info
  name: info-terms-of-service
  severity: warn
- description: Must use OpenAPI 3.0.x
  given: $.openapi
  name: openapi-version
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-required
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Path segments must use kebab-case (lowercase with hyphens)
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not end with a trailing slash
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "AT&T"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-att-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-operationid-required
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined
  given: $
  name: tags-global-defined
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: Every parameter must have a schema
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Query and header parameter names should use snake_case or camelCase
  given: $.paths[*][*].parameters[?(@.in == 'query')].name
  name: parameter-snake-case
  severity: info
- description: Request bodies should have a description
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: warn
- description: Request bodies should support application/json
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Operations using security should have a 401 response
  given: $.paths[*][get,post,put,patch,delete][?(@.security)]
  name: response-401-required
  severity: warn
- description: POST operations should document a 400 Bad Request response
  given: $.paths[*].post
  name: response-400-for-post
  severity: warn
- description: Top-level component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should have a type defined
  given: $.components.schemas[*].properties[*]
  name: schema-properties-types
  severity: warn
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: OAuth2 security schemes must define scopes
  given: $.components.securitySchemes[?(@.type == 'oauth2')].flows[*]
  name: security-oauth2-scopes
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
- description: Operations should include request/response examples for Microcks compatibility
  given: $.paths[*][get,post,put,patch,delete].responses[*].content[*]
  name: operation-examples-encouraged
  severity: info
- description: Operations should include x-microcks-operation extension for mock server support
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/at-and-t-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/at-and-t/refs/heads/main/rules/at-and-t-spectral-rules.yml
severity_counts:
  error: 16
  hint: 0
  info: 3
  warn: 18
slug: at-and-t-spectral-rules
source_filename: at-and-t-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # ===========================\n  # INFO / METADATA\n  # ===========================\n  info-title-pattern:\n    description: API title must start with \"AT&T\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: '^AT&T '\n\n  info-description-required:\n    description: API info must have a non-empty description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API info must have a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API info should have contact information\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  info-terms-of-service:\n    description: API info should include a termsOfService URL\n    severity: warn\n    given: $.info\n    then:\n\
  \      field: termsOfService\n      function: truthy\n\n  # ===========================\n  # OPENAPI VERSION\n  # ===========================\n  openapi-version:\n    description: Must use OpenAPI 3.0.x\n    severity: error\n    given: $.openapi\n    then:\n      function: pattern\n      functionOptions:\n        match: '^3\\.0\\.'\n\n  # ===========================\n  # SERVERS\n  # ===========================\n  servers-required:\n    description: At least one server must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n\n  servers-description-required:\n    description: Each server should have a description\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # ===========================\n\
  \  # PATHS — NAMING CONVENTIONS\n  # ===========================\n  paths-kebab-case:\n    description: Path segments must use kebab-case (lowercase with hyphens)\n    severity: warn\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        match: '^(\\/[a-z0-9{}\\-]+)+$'\n\n  paths-no-trailing-slash:\n    description: Paths must not end with a trailing slash\n    severity: warn\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: '\\/$'\n\n  # ===========================\n  # OPERATIONS\n  # ===========================\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-att-prefix:\n    description: Operation summaries must start with \"AT&T\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n\
  \    then:\n      function: pattern\n      functionOptions:\n        match: '^AT&T '\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-camel-case:\n    description: operationId must use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]+$'\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n\
  \    then:\n      field: tags\n      function: truthy\n\n  # ===========================\n  # TAGS\n  # ===========================\n  tags-global-defined:\n    description: Global tags array should be defined\n    severity: warn\n    given: $\n    then:\n      field: tags\n      function: truthy\n\n  # ===========================\n  # PARAMETERS\n  # ===========================\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Every parameter must have a schema\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  parameter-snake-case:\n    description: Query and header parameter names should use snake_case or camelCase\n    severity: info\n    given: $.paths[*][*].parameters[?(@.in == 'query')].name\n    then:\n\
  \      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9_.]+$'\n\n  # ===========================\n  # REQUEST BODIES\n  # ===========================\n  request-body-description:\n    description: Request bodies should have a description\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody\n    then:\n      field: description\n      function: truthy\n\n  request-body-json-content:\n    description: Request bodies should support application/json\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      function: truthy\n\n  # ===========================\n  # RESPONSES\n  # ===========================\n  response-success-required:\n    description: Every operation must have at least one 2xx response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: responses\n      function: truthy\n\n  response-description-required:\n    description: Every response must have\
  \ a description\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-401-required:\n    description: Operations using security should have a 401 response\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete][?(@.security)]\n    then:\n      field: responses.401\n      function: truthy\n\n  response-400-for-post:\n    description: POST operations should document a 400 Bad Request response\n    severity: warn\n    given: $.paths[*].post\n    then:\n      field: responses.400\n      function: truthy\n\n  # ===========================\n  # SCHEMAS — PROPERTY NAMING\n  # ===========================\n  schema-description-required:\n    description: Top-level component schemas should have descriptions\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-properties-types:\n    description: Schema properties should have a type\
  \ defined\n    severity: warn\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: type\n      function: truthy\n\n  # ===========================\n  # SECURITY\n  # ===========================\n  security-schemes-defined:\n    description: Security schemes must be defined in components\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-oauth2-scopes:\n    description: OAuth2 security schemes must define scopes\n    severity: warn\n    given: $.components.securitySchemes[?(@.type == 'oauth2')].flows[*]\n    then:\n      field: scopes\n      function: truthy\n\n  # ===========================\n  # HTTP METHOD CONVENTIONS\n  # ===========================\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE\
  \ operations should not have a request body\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  post-has-request-body:\n    description: POST operations should have a request body\n    severity: warn\n    given: $.paths[*].post\n    then:\n      field: requestBody\n      function: truthy\n\n  # ===========================\n  # GENERAL QUALITY\n  # ===========================\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: $..description\n    then:\n      function: pattern\n      functionOptions:\n        match: '.+'\n\n  operation-examples-encouraged:\n    description: Operations should include request/response examples for Microcks compatibility\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].responses[*].content[*]\n    then:\n      field: examples\n      function: truthy\n\n  microcks-operation-extension:\n    description: Operations\
  \ should include x-microcks-operation extension for mock server support\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/at-and-t/refs/heads/main/rules/at-and-t-spectral-rules.yml
tags:
- Telecommunications
- Wireless
- Wireline
- Messaging
- Speech
- Mobile
- Broadband
- Enterprise
- Spectral
- Linting
- API Governance
---
