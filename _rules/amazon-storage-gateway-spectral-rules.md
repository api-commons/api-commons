---
api_specs:
- filename: amazon-storage-gateway.yaml
  format: yaml
  label: Amazon Storage Gateway REST API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-storage-gateway/refs/heads/main/openapi/amazon-storage-gateway.yaml
categories:
- get
- info
- 'no'
- openapi
- operation
- parameter
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon Storage Gateway.
layout: rules
name: Amazon Storage Gateway API Rules
provider_name: Amazon Storage Gateway
provider_slug: amazon-storage-gateway
rule_count: 19
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
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summary must start with "Amazon" or "AWS"
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-amazon-prefix
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
  name: operation-id-pascal-case
  severity: warn
- description: Every operation must have tags
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must have a 2xx or 200 response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: error
- description: Object schemas should have descriptions
  given: $.components.schemas[?(@.type == 'object')]
  name: schema-description-on-objects
  severity: info
- description: Security schemes must be defined in components
  given: $
  name: security-schemes-defined
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Tags should use Title Case
  given: $.tags[*].name
  name: tags-title-case
  severity: warn
rules_file: rules/amazon-storage-gateway-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-storage-gateway/refs/heads/main/rules/amazon-storage-gateway-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 1
  warn: 7
slug: amazon-storage-gateway-spectral-rules
source_filename: amazon-storage-gateway-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"Amazon\" or \"AWS\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(Amazon|AWS) \"\n\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n\
  \      field: servers\n      function: truthy\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-amazon-prefix:\n    description: Operation summary must start with \"Amazon\" or \"AWS\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(Amazon|AWS) \"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n\
  \      function: truthy\n\n  operation-id-pascal-case:\n    description: OperationId must use PascalCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have a 2xx or 200 response\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].responses\"\n    then:\n      function: schema\n      functionOptions:\n\
  \        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-on-objects:\n    description: Object schemas should have descriptions\n    severity: info\n    given: \"$.components.schemas[?(@.type == 'object')]\"\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components\n    severity: error\n    given: \"$\"\n    then:\n      field: \"components.securitySchemes\"\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n\
  \    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  tags-title-case:\n    description: Tags should use Title Case\n    severity: warn\n    given: \"$.tags[*].name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9 ]+$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-storage-gateway/refs/heads/main/rules/amazon-storage-gateway-spectral-rules.yml
tags:
- Backup
- File Storage
- Gateway
- Hybrid Cloud
- Storage
- Spectral
- Linting
- API Governance
---
