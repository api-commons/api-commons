---
api_specs:
- filename: amazon-private-ca-openapi-original.yaml
  format: yaml
  label: AWS Private CA API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-private-ca/refs/heads/main/openapi/amazon-private-ca-openapi-original.yaml
categories:
- info
- 'no'
- openapi
- operation
- parameter
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Private CA.
layout: rules
name: Amazon Private CA API Rules
provider_name: Amazon Private CA
provider_slug: amazon-private-ca
rule_count: 19
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
  given: $.paths[*][post,get,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Summaries should start with Amazon Private CA
  given: $.paths[*][post,get,put,delete,patch].summary
  name: operation-summary-amazon-private-ca-prefix
  severity: warn
- description: All operations must have a description
  given: $.paths[*][post,get,put,delete,patch]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][post,get,put,delete,patch]
  name: operation-id-required
  severity: error
- description: All operations must have tags
  given: $.paths[*][post,get,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: All operations must have a success response
  given: $.paths[*][post,get,put,delete,patch]
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
- description: Schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
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
- description: Consider adding examples to operation responses
  given: $.paths[*][*].responses[*].content[*]
  name: operation-examples-encouraged
  severity: info
rules_file: rules/amazon-private-ca-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-private-ca/refs/heads/main/rules/amazon-private-ca-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 2
  warn: 5
slug: amazon-private-ca-spectral-rules
source_filename: amazon-private-ca-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: API must have a title\n    message: Info object must have a title\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: API must have a description\n    message: Info object must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API version must be defined\n    message: Info object must have a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: API should use OpenAPI 3.x\n    severity: error\n    given: $.openapi\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers must be defined\n    severity:\
  \ error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: $.paths[*][post,get,put,delete,patch]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-amazon-private-ca-prefix:\n    description: Summaries should start with Amazon Private CA\n    message: Operation summary should start with 'Amazon Private CA'\n    severity: warn\n    given: $.paths[*][post,get,put,delete,patch].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Private CA\"\n\n  operation-description-required:\n    description: All operations must have a description\n    severity: error\n    given: $.paths[*][post,get,put,delete,patch]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: All operations must have an operationId\n    severity: error\n\
  \    given: $.paths[*][post,get,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: All operations must have tags\n    severity: warn\n    given: $.paths[*][post,get,put,delete,patch]\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: All operations must have a success response\n    severity: error\n    given: $.paths[*][post,get,put,delete,patch]\n    then:\n      field: responses\n      function: truthy\n\n  response-description-required:\n    description: All responses must have descriptions\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n\n \
  \ # SCHEMAS\n  schema-type-defined:\n    description: Schemas should define a type\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  schema-description-required:\n    description: Schemas should have descriptions\n    severity: info\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: Global security must be defined\n    severity: warn\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: warn\n    given: $..description\n    then:\n      function: truthy\n\n  operation-examples-encouraged:\n    description:\
  \ Consider adding examples to operation responses\n    severity: info\n    given: $.paths[*][*].responses[*].content[*]\n    then:\n      field: examples\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-private-ca/refs/heads/main/rules/amazon-private-ca-spectral-rules.yml
tags:
- Certificate Authority
- Certificates
- PKI
- Security
- X.509
- TLS
- IoT
- Spectral
- Linting
- API Governance
---
