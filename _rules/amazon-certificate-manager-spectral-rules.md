---
api_specs:
- filename: amazon-certificate-manager-openapi.yml
  format: yaml
  label: Amazon Certificate Manager API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-certificate-manager/refs/heads/main/openapi/amazon-certificate-manager-openapi.yml
categories:
- delete
- external
- get
- info
- microcks
- 'no'
- openapi
- operation
- parameter
- request
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Certificate Manager.
layout: rules
name: Amazon Certificate Manager API Rules
provider_name: Amazon Certificate Manager
provider_slug: amazon-certificate-manager
rule_count: 29
rules:
- description: API title must start with "Amazon Certificate Manager"
  given: $.info.title
  name: info-title-prefix
  severity: error
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: API must have contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version
  severity: error
- description: API must define at least one server
  given: $
  name: servers-required
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: All servers must have a description
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-operationId-required
  severity: error
- description: operationId must use PascalCase (matches AWS convention)
  given: $.paths[*][get,post,put,patch,delete,head,options].operationId
  name: operation-operationId-pascal-case
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Amazon Certificate Manager"
  given: $.paths[*][get,post,put,patch,delete,head,options].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: error
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: error
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must have a 2xx success response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: All response codes must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations should include 400 bad request response
  given: $.paths[*][post,put,patch,delete].responses
  name: response-401-for-secured
  severity: warn
- description: Operations should document 500 internal server error
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-500-required
  severity: info
- description: Top-level component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-on-top-level
  severity: warn
- description: Schema properties must define a type
  given: $.components.schemas[*].properties[*]
  name: schema-properties-have-types
  severity: warn
- description: Security schemes must be defined if security is referenced
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: APIs should have external documentation links
  given: $
  name: external-docs-encouraged
  severity: info
- description: Operations should have x-microcks-operation extension for mock server support
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-present
  severity: info
rules_file: rules/amazon-certificate-manager-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-certificate-manager/refs/heads/main/rules/amazon-certificate-manager-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 3
  warn: 11
slug: amazon-certificate-manager-spectral-rules
source_filename: amazon-certificate-manager-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"Amazon Certificate Manager\"\n    severity: error\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Certificate Manager\"\n\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API must have contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function:\
  \ pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: API must define at least one server\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description-required:\n    description: All servers must have a description\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # OPERATIONS\n  operation-operationId-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationId-pascal-case:\n    description: operationId must\
  \ use PascalCase (matches AWS convention)\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]+$\"\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries must start with \"Amazon Certificate Manager\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Certificate Manager\"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field:\
  \ description\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: All parameters must have a schema\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-json-content:\n    description: Request bodies should use application/json content type\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      field: application/json\n\
  \      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have a 2xx success response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses\n      function: truthy\n\n  response-description-required:\n    description: All response codes must have descriptions\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-401-for-secured:\n    description: Operations should include 400 bad request response\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      field: \"400\"\n      function: truthy\n\n  response-500-required:\n    description: Operations should document 500 internal server error\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      field: \"500\"\n      function: truthy\n\n  #\
  \ SCHEMAS\n  schema-description-on-top-level:\n    description: Top-level component schemas should have descriptions\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-properties-have-types:\n    description: Schema properties must define a type\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined if security is referenced\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have\
  \ a request body\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: \"$..description\"\n    then:\n      function: truthy\n\n  external-docs-encouraged:\n    description: APIs should have external documentation links\n    severity: info\n    given: \"$\"\n    then:\n      field: externalDocs\n      function: truthy\n\n  microcks-operation-present:\n    description: Operations should have x-microcks-operation extension for mock server support\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-certificate-manager/refs/heads/main/rules/amazon-certificate-manager-spectral-rules.yml
tags:
- Certificates
- Encryption
- Security
- SSL
- TLS
- Spectral
- Linting
- API Governance
---
