---
api_specs:
- filename: amazon-proton-openapi-original.yaml
  format: yaml
  label: AWS Proton API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-proton/refs/heads/main/openapi/amazon-proton-openapi-original.yaml
categories:
- info
- 'no'
- openapi
- operation
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Proton.
layout: rules
name: Amazon Proton API Rules
provider_name: Amazon Proton
provider_slug: amazon-proton
rule_count: 16
rules:
- description: API must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be defined
  given: $.info
  name: info-version-required
  severity: error
- description: API should use OpenAPI 3.x
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Summaries should start with Amazon Proton
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-amazon-proton-prefix
  severity: warn
- description: All operations must have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: All operations must have tags
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: All operations must have a success response
  given: $.paths[*][get,post,put,delete,patch]
  name: response-success-required
  severity: error
- description: All responses must have descriptions
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Schemas should define a type
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: warn
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/amazon-proton-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-proton/refs/heads/main/rules/amazon-proton-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 0
  warn: 5
slug: amazon-proton-spectral-rules
source_filename: amazon-proton-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  info-title-required:\n    description: API must have a title\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: API must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API version must be defined\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  openapi-version-3:\n    description: API should use OpenAPI 3.x\n    severity: error\n    given: $.openapi\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  servers-defined:\n    description: Servers must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given:\
  \ $.paths[*][get,post,put,delete,patch]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-amazon-proton-prefix:\n    description: Summaries should start with Amazon Proton\n    message: Operation summary should start with 'Amazon Proton'\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Proton\"\n\n  operation-description-required:\n    description: All operations must have a description\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: All operations must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: All operations must have tags\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch]\n\
  \    then:\n      field: tags\n      function: truthy\n\n  response-success-required:\n    description: All operations must have a success response\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: responses\n      function: truthy\n\n  response-description-required:\n    description: All responses must have descriptions\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-type-defined:\n    description: Schemas should define a type\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: Global security must be defined\n    severity: warn\n    given: $\n    then:\n      field:\
  \ security\n      function: truthy\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: warn\n    given: $..description\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-proton/refs/heads/main/rules/amazon-proton-spectral-rules.yml
tags:
- DevOps
- Infrastructure as Code
- Platform Engineering
- Serverless
- Templates
- Self-Service
- CI/CD
- Spectral
- Linting
- API Governance
---
