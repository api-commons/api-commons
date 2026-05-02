---
api_specs:
- filename: amazon-device-farm-openapi.yaml
  format: yaml
  label: AWS Device Farm API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-device-farm/refs/heads/main/openapi/amazon-device-farm-openapi.yaml
categories:
- external
- get
- info
- 'no'
- openapi
- operation
- parameter
- post
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Device Farm.
layout: rules
name: Amazon Device Farm API Rules
provider_name: Amazon Device Farm
provider_slug: amazon-device-farm
rule_count: 24
rules:
- description: API title should include "Device Farm"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: All operations must have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: OperationIds should use PascalCase (AWS Device Farm convention)
  given: $.paths[*][get,post,put,delete,patch].operationId
  name: operation-id-pascal-case
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: All parameters must have a description
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters must have a schema
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-schema-required
  severity: error
- description: POST operations should typically have a request body
  given: $.paths[*].post
  name: post-should-have-request-body
  severity: info
- description: Operations must have at least one 2xx response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: error
- description: Operations should document 4xx error responses
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-error-4xx
  severity: info
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Schemas should have a type defined
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Global security should be defined
  given: $
  name: security-global-defined
  severity: warn
- description: Security schemes should be defined in components
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: API should reference external documentation
  given: $
  name: external-docs-encouraged
  severity: info
rules_file: rules/amazon-device-farm-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-device-farm/refs/heads/main/rules/amazon-device-farm-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 4
  warn: 8
slug: amazon-device-farm-spectral-rules
source_filename: amazon-device-farm-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title should include \"Device Farm\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"Device Farm\"\n\n  info-description-required:\n    description: API must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must have a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function:\
  \ truthy\n\n  servers-https-only:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: All operations must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: All operations must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-pascal-case:\n    description: OperationIds should use PascalCase (AWS Device Farm convention)\n\
  \    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: All operations must have at least one tag\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: All parameters must have a schema\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  # REQUEST BODIES\n  post-should-have-request-body:\n    description: POST operations should typically have a request body\n\
  \    severity: info\n    given: $.paths[*].post\n    then:\n      field: requestBody\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must have at least one 2xx response\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-error-4xx:\n    description: Operations should document 4xx error responses\n    severity: info\n    given: $.paths[*][get,post,put,delete,patch].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n\
  \          type: object\n          anyOf:\n            - required: ['400']\n            - required: ['404']\n            - required: ['409']\n\n  # SCHEMAS\n  schema-description-required:\n    description: Top-level schemas should have descriptions\n    severity: info\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-type-required:\n    description: Schemas should have a type defined\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-global-defined:\n    description: Global security should be defined\n    severity: warn\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes should be defined in components\n    severity: warn\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n\
  \    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: $..description\n    then:\n      function: truthy\n\n  external-docs-encouraged:\n    description: API should reference external documentation\n    severity: info\n    given: $\n    then:\n      field: externalDocs\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-device-farm/refs/heads/main/rules/amazon-device-farm-spectral-rules.yml
tags:
- Application Testing
- Device Testing
- Mobile Testing
- Quality Assurance
- Spectral
- Linting
- API Governance
---
