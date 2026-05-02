---
api_specs:
- filename: amazon-supply-chain.yaml
  format: yaml
  label: AWS Supply Chain API
  slug: aws-supply-chain-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-supply-chain/refs/heads/main/openapi/amazon-supply-chain.yaml
categories:
- get
- info
- 'no'
- openapi
- operation
- paths
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon Supply Chain.
layout: rules
name: Amazon Supply Chain API Rules
provider_name: Amazon Supply Chain
provider_slug: amazon-supply-chain
rule_count: 18
rules:
- description: API title must start with "Amazon" or "AWS"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info must have description
  given: $.info
  name: info-description-required
  severity: error
- description: Info must have version
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
- description: Summary must start with "Amazon" or "AWS"
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-amazon-prefix
  severity: warn
- description: Every operation must have operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: OperationId must use PascalCase
  given: $.paths[*][get,post,put,delete,patch].operationId
  name: operation-id-pascal-case
  severity: warn
- description: Operations must have tags
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: Operations must have 2xx response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: Responses must have descriptions
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: error
- description: Security schemes must be defined
  given: $
  name: security-schemes-defined
  severity: error
- description: GET must not have request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Tags should use Title Case
  given: $.tags[*].name
  name: tags-title-case
  severity: warn
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Object schemas should have descriptions
  given: $.components.schemas[?(@.type == 'object')]
  name: schema-description-on-objects
  severity: info
rules_file: rules/amazon-supply-chain-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-supply-chain/refs/heads/main/rules/amazon-supply-chain-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 2
  warn: 5
slug: amazon-supply-chain-spectral-rules
source_filename: amazon-supply-chain-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-prefix:\n    description: API title must start with \"Amazon\" or \"AWS\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(Amazon|AWS) \"\n  info-description-required:\n    description: Info must have description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: Info must have version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n  openapi-version:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n  servers-required:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n  operation-summary-required:\n \
  \   description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n  operation-summary-amazon-prefix:\n    description: Summary must start with \"Amazon\" or \"AWS\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(Amazon|AWS) \"\n  operation-id-required:\n    description: Every operation must have operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-id-pascal-case:\n    description: OperationId must use PascalCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]+$\"\n  operation-tags-required:\n    description: Operations\
  \ must have tags\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n  response-success-required:\n    description: Operations must have 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n  response-description-required:\n    description: Responses must have descriptions\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].responses[*]\"\n    then:\n      field: description\n      function: truthy\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: \"components.securitySchemes\"\n      function: truthy\n  get-no-request-body:\n    description:\
  \ GET must not have request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: info\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}-]+)+$\"\n  tags-title-case:\n    description: Tags should use Title Case\n    severity: warn\n    given: \"$.tags[*].name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9 ]+$\"\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n  schema-description-on-objects:\n    description: Object schemas should have descriptions\n    severity: info\n    given: \"$.components.schemas[?(@.type == 'object')]\"\n    then:\n      field: description\n\
  \      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-supply-chain/refs/heads/main/rules/amazon-supply-chain-spectral-rules.yml
tags:
- ERP Integration
- Logistics
- Machine Learning
- Supply Chain
- Spectral
- Linting
- API Governance
---
