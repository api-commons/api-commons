---
api_specs:
- filename: aws-api-gateway-v1-openapi.yml
  format: yaml
  label: Amazon API Gateway V1 (REST)
  slug: aws-api-gateway-v1
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/aws-api-gateway/refs/heads/main/openapi/aws-api-gateway-v1-openapi.yml
- filename: aws-api-gateway-v2-openapi.yml
  format: yaml
  label: Amazon API Gateway V2 (HTTP and WebSocket)
  slug: aws-api-gateway-v2
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/aws-api-gateway/refs/heads/main/openapi/aws-api-gateway-v2-openapi.yml
- filename: aws-api-gateway-management-openapi.yml
  format: yaml
  label: Amazon API Gateway Management API
  slug: aws-api-gateway-management
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/aws-api-gateway/refs/heads/main/openapi/aws-api-gateway-management-openapi.yml
categories:
- deprecation
- info
- method
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
description: Spectral linting rules defining API design standards and conventions for Amazon API Gateway.
layout: rules
name: Amazon API Gateway API Rules
provider_name: Amazon API Gateway
provider_slug: aws-api-gateway
rule_count: 35
rules:
- description: API title must start with "Amazon API Gateway"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info object must have a description with at least 20 characters
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Info object should have contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: All specs must use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: Servers array must be defined and non-empty
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Path segments must use kebab-case (lowercase letters, numbers, hyphens)
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Amazon API Gateway"
  given: $.paths[*][get,post,put,patch,delete,head,options].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: OperationIds must use camelCase
  given: $.paths[*][get,post,put,patch,delete,head,options].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: error
- description: All tags used in operations should be defined in the global tags array
  given: $
  name: tag-global-defined
  severity: warn
- description: Global tags should have descriptions
  given: $.tags[*]
  name: tag-description
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: All parameters must have a schema with a type
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Request bodies should have descriptions
  given: $.paths[*][*].requestBody
  name: request-body-description
  severity: warn
- description: Every operation must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: All responses must have descriptions
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Secured operations should document 401 Unauthorized response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-401-on-secured
  severity: warn
- description: Top-level component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description
  severity: warn
- description: Schema objects should define a type
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Schema property names should use snake_case
  given: $.components.schemas[*].properties[*]~
  name: schema-property-snake-case
  severity: info
- description: Security schemes must be defined in components
  given: $
  name: security-schemes-defined
  severity: error
- description: AWS SigV4 security scheme should be defined
  given: $.components.securitySchemes
  name: security-sigv4-scheme
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: method-get-no-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: method-delete-no-body
  severity: warn
- description: POST operations creating resources should have a request body
  given: $.paths[*].post
  name: method-post-has-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Deprecated operations should have a description explaining the deprecation
  given: $.paths[*][*][?(@.deprecated == true)]
  name: deprecation-documented
  severity: warn
rules_file: rules/aws-api-gateway-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/aws-api-gateway/refs/heads/main/rules/aws-api-gateway-spectral-rules.yml
severity_counts:
  error: 17
  hint: 0
  info: 1
  warn: 17
slug: aws-api-gateway-spectral-rules
source_filename: aws-api-gateway-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"Amazon API Gateway\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon API Gateway\"\n\n  info-description-required:\n    description: Info object must have a description with at least 20 characters\n    severity: error\n    given: $.info\n    then:\n      - field: description\n        function: truthy\n      - field: description\n        function: minLength\n        functionOptions:\n          value: 20\n\n  info-version-required:\n    description: Info object must have a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Info object should have contact information\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n\
  \    description: All specs must use OpenAPI 3.x\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers array must be defined and non-empty\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description:\n    description: Each server should have a description\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # PATHS - NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments must use kebab-case (lowercase letters, numbers, hyphens)\n    severity: warn\n    given: $.paths[*]~\n    then:\n      function: pattern\n\
  \      functionOptions:\n        match: \"^(/[a-z0-9{}_-]+)+$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: error\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries must start with \"Amazon API Gateway\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon API Gateway\"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n\
  \    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: OperationIds must use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tag-global-defined:\n    description: All tags used in operations should be defined in the global tags array\n    severity: warn\n    given: $\n    then:\n      field: tags\n      function:\
  \ truthy\n\n  tag-description:\n    description: Global tags should have descriptions\n    severity: warn\n    given: $.tags[*]\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: All parameters must have a schema with a type\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-json-content:\n    description: Request bodies should use application/json content type\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      field: application/json\n      function: truthy\n\n  request-body-description:\n    description: Request bodies should have descriptions\n    severity:\
  \ warn\n    given: $.paths[*][*].requestBody\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have at least one 2xx response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: responses\n      function: truthy\n\n  response-description-required:\n    description: All responses must have descriptions\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-401-on-secured:\n    description: Secured operations should document 401 Unauthorized response\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: responses.401\n      function: truthy\n\n  # SCHEMAS - PROPERTY NAMING\n  schema-description:\n    description: Top-level component schemas should have descriptions\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n\
  \      field: description\n      function: truthy\n\n  schema-type-required:\n    description: Schema objects should define a type\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  schema-property-snake-case:\n    description: Schema property names should use snake_case\n    severity: info\n    given: $.components.schemas[*].properties[*]~\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_]*$\"\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components\n    severity: error\n    given: $\n    then:\n      field: components.securitySchemes\n      function: truthy\n\n  security-sigv4-scheme:\n    description: AWS SigV4 security scheme should be defined\n    severity: warn\n    given: $.components.securitySchemes\n    then:\n      field: sigv4\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  method-get-no-body:\n    description:\
  \ GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  method-delete-no-body:\n    description: DELETE operations should not have a request body\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  method-post-has-body:\n    description: POST operations creating resources should have a request body\n    severity: warn\n    given: $.paths[*].post\n    then:\n      field: requestBody\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: $..description\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  deprecation-documented:\n    description: Deprecated operations should have a description explaining the deprecation\n    severity: warn\n    given: $.paths[*][*][?(@.deprecated == true)]\n\
  \    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/aws-api-gateway/refs/heads/main/rules/aws-api-gateway-spectral-rules.yml
tags:
- API Gateway
- Cloud
- REST
- WebSocket
- Serverless
- Spectral
- Linting
- API Governance
---
