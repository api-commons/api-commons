---
api_specs:
- filename: amazon-codedeploy-openapi-original.yaml
  format: yaml
  label: Amazon CodeDeploy API
  slug: amazon-codedeploy-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-codedeploy/refs/heads/main/openapi/amazon-codedeploy-openapi-original.yaml
categories:
- info
- 'no'
- operation
- response
- schema
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon CodeDeploy.
layout: rules
name: Amazon CodeDeploy API Rules
provider_name: Amazon CodeDeploy
provider_slug: amazon-codedeploy
rule_count: 9
rules:
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with Amazon CodeDeploy
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-company-prefix
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-operationId-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Schema components should have a type
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Operations should include x-microcks-operation
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-microcks-operation
  severity: info
rules_file: rules/amazon-codedeploy-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-codedeploy/refs/heads/main/rules/amazon-codedeploy-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 1
  warn: 3
slug: amazon-codedeploy-spectral-rules
source_filename: amazon-codedeploy-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: \"spectral:oas\"\n\nrules:\n\n  info-description-required:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  servers-https:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-company-prefix:\n    description: Operation summaries should start with Amazon CodeDeploy\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon CodeDeploy\"\n\n  operation-operationId-required:\n    description:\
  \ Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-type-required:\n    description: Schema components should have a type\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  operation-microcks-operation:\n    description: Operations should include x-microcks-operation\n    severity: info\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n \
  \     field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-codedeploy/refs/heads/main/rules/amazon-codedeploy-spectral-rules.yml
tags:
- Amazon
- Deployment
- DevOps
- CI/CD
- Release Management
- Blue/Green Deployment
- Spectral
- Linting
- API Governance
---
