---
api_specs:
- filename: amazon-sagemaker-openapi.yml
  format: yaml
  label: Amazon SageMaker API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-sagemaker/refs/heads/main/openapi/amazon-sagemaker-openapi.yml
categories:
- delete
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
description: Spectral linting rules defining API design standards and conventions for Amazon SageMaker.
layout: rules
name: Amazon SageMaker API Rules
provider_name: Amazon SageMaker
provider_slug: amazon-sagemaker
rule_count: 23
rules:
- description: Info title must be present and start with "Amazon SageMaker"
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present with at least 30 characters
  given: $.info
  name: info-description-required
  severity: warn
- description: Info version must be present
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https-only
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Amazon SageMaker"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-amazon-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId must use PascalCase (SageMaker convention)
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-pascal-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Request bodies must define content
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-content-required
  severity: error
- description: Every operation must have a 200 or 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Schema properties should have a type defined
  given: $.components.schemas[*].properties[*]
  name: schema-type-required
  severity: warn
- description: Top-level component schemas must have a description
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Security schemes should be defined in components
  given: $
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
  severity: warn
- description: Operations should have x-microcks-operation for mock support
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-present
  severity: info
rules_file: rules/amazon-sagemaker-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-sagemaker/refs/heads/main/rules/amazon-sagemaker-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 2
  warn: 11
slug: amazon-sagemaker-spectral-rules
source_filename: amazon-sagemaker-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: Info title must be present and start with \"Amazon SageMaker\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: Info description must be present with at least 30 characters\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info version must be present\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n\
  \      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-amazon-prefix:\n    description: Operation summaries must start with \"Amazon SageMaker\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon SageMaker\"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n\
  \      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-pascal-case:\n    description: operationId must use PascalCase (SageMaker convention)\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function:\
  \ truthy\n\n  # REQUEST BODIES\n  request-body-content-required:\n    description: Request bodies must define content\n    severity: error\n    given: \"$.paths[*][post,put,patch].requestBody\"\n    then:\n      field: content\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have a 200 or 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n            - required: ['2XX']\n\n  response-description-required:\n    description: Every response must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-type-required:\n    description: Schema properties should have\
  \ a type defined\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  schema-description-required:\n    description: Top-level component schemas must have a description\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes should be defined in components\n    severity: warn\n    given: \"$\"\n    then:\n      field: components.securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field:\
  \ requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  microcks-operation-present:\n    description: Operations should have x-microcks-operation for mock support\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-sagemaker/refs/heads/main/rules/amazon-sagemaker-spectral-rules.yml
tags:
- AI
- Inference
- Machine Learning
- MLOps
- Training
- Spectral
- Linting
- API Governance
---
