---
api_specs:
- filename: dynamodb-openapi.yml
  format: yaml
  label: Amazon DynamoDB API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dynamodb/refs/heads/main/openapi/dynamodb-openapi.yml
- filename: dynamodb-streams-asyncapi.yml
  format: yaml
  label: Amazon DynamoDB Streams API
  slug: ''
  spec_type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/dynamodb/refs/heads/main/asyncapi/dynamodb-streams-asyncapi.yml
- filename: openapi.yaml
  format: yaml
  label: Amazon DynamoDB Accelerator (DAX) API
  slug: ''
  spec_type: OpenAPI
  url: https://api.apis.guru/v2/specs/amazonaws.com/dax/2017-04-19/openapi.yaml
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Amazon DynamoDB.
layout: rules
name: Amazon DynamoDB API Rules
provider_name: Amazon DynamoDB
provider_slug: dynamodb
rule_count: 7
rules:
- description: Info title must be present
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/dynamodb-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/dynamodb/refs/heads/main/rules/dynamodb-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: dynamodb-spectral-rules
source_filename: dynamodb-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: summary, function: truthy}\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  response-description-required:\n    description:\
  \ Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/dynamodb/refs/heads/main/rules/dynamodb-spectral-rules.yml
tags:
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
- Spectral
- Linting
- API Governance
---
