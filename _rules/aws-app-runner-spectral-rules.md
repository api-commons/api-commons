---
api_specs:
- filename: aws-app-runner-openapi.yml
  format: yaml
  label: AWS App Runner
  slug: aws-app-runner
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/aws-app-runner/refs/heads/main/openapi/aws-app-runner-openapi.yml
categories:
- info
- method
- 'no'
- openapi
- operation
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for AWS App Runner.
layout: rules
name: AWS App Runner API Rules
provider_name: AWS App Runner
provider_slug: aws-app-runner
rule_count: 17
rules:
- description: API title must start with "AWS App Runner"
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
- description: All specs must use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: Servers array must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "AWS App Runner"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: OperationIds should use PascalCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-pascal-case
  severity: warn
- description: All responses must have descriptions
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Every operation must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description
  severity: warn
- description: Security schemes should be defined
  given: $
  name: security-schemes-defined
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: method-get-no-body
  severity: error
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/aws-app-runner-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/aws-app-runner/refs/heads/main/rules/aws-app-runner-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 0
  warn: 5
slug: aws-app-runner-spectral-rules
source_filename: aws-app-runner-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"AWS App Runner\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^AWS App Runner\"\n\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must have a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: All specs must use OpenAPI 3.x\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers array must be defined\n    severity: error\n    given: $\n    then:\n\
  \      field: servers\n      function: truthy\n\n  servers-https:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries must start with \"AWS App Runner\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^AWS App Runner\"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n\
  \    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-pascal-case:\n    description: OperationIds should use PascalCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*$\"\n\n  # RESPONSES\n  response-description-required:\n    description: All responses must have descriptions\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-success-required:\n    description: Every operation must have at least one 2xx response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: responses\n      function: truthy\n\n  # SCHEMAS\n  schema-description:\n    description: Component schemas should have\
  \ descriptions\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes should be defined\n    severity: warn\n    given: $\n    then:\n      field: components.securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  method-get-no-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/aws-app-runner/refs/heads/main/rules/aws-app-runner-spectral-rules.yml
tags:
- CI/CD
- Containers
- Deployment
- Microservices
- Serverless
- Spectral
- Linting
- API Governance
---
