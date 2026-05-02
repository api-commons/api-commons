---
api_specs:
- filename: amazon-signer.yaml
  format: yaml
  label: AWS Signer API
  slug: aws-signer-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-signer/refs/heads/main/openapi/amazon-signer.yaml
categories:
- delete
- get
- info
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon Signer.
layout: rules
name: Amazon Signer API Rules
provider_name: Amazon Signer
provider_slug: amazon-signer
rule_count: 25
rules:
- description: API title must start with "Amazon" or "AWS"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version
  severity: error
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summary must start with "Amazon"
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: OperationId must use PascalCase
  given: $.paths[*][get,post,put,delete,patch].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have tags
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Parameter names should use camelCase or snake_case
  given: $.paths[*][get,post,put,delete,patch].parameters[*].name
  name: parameter-name-snake-case
  severity: info
- description: Every operation must have a 2xx response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: error
- description: Operations should document 403 responses
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-error-unauthorized
  severity: info
- description: Schema properties should have a type defined
  given: $.components.schemas[*].properties[*]
  name: schema-type-required
  severity: warn
- description: Top-level schemas should have a description
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Security schemes must be defined in components
  given: $
  name: security-schemes-defined
  severity: error
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
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Tags in the global tags array should use Title Case
  given: $.tags[*].name
  name: tags-title-case
  severity: warn
rules_file: rules/amazon-signer-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-signer/refs/heads/main/rules/amazon-signer-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 4
  warn: 9
slug: amazon-signer-spectral-rules
source_filename: amazon-signer-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"Amazon\" or \"AWS\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(Amazon|AWS) \"\n\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n\
  \      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summary must start with \"Amazon\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon \"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n\
  \    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: OperationId must use PascalCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-name-snake-case:\n    description: Parameter names should\
  \ use camelCase or snake_case\n    severity: info\n    given: \"$.paths[*][get,post,put,delete,patch].parameters[*].name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9_]*$\"\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have a 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-error-unauthorized:\n    description: Operations should document 403 responses\n    severity: info\n    given:\
  \ \"$.paths[*][get,post,put,delete,patch].responses\"\n    then:\n      field: \"403\"\n      function: truthy\n\n  # SCHEMAS\n  schema-type-required:\n    description: Schema properties should have a type defined\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"type\"]\n            - required: [\"$ref\"]\n            - required: [\"allOf\"]\n            - required: [\"oneOf\"]\n            - required: [\"anyOf\"]\n            - required: [\"enum\"]\n\n  schema-description-required:\n    description: Top-level schemas should have a description\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components\n    severity: error\n    given: \"$\"\n    then:\n\
  \      field: \"components.securitySchemes\"\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: info\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}-]+)+$\"\n\n  tags-title-case:\n    description:\
  \ Tags in the global tags array should use Title Case\n    severity: warn\n    given: \"$.tags[*].name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9 ]+$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-signer/refs/heads/main/rules/amazon-signer-spectral-rules.yml
tags:
- Code Signing
- IoT
- Lambda
- Security
- Spectral
- Linting
- API Governance
---
