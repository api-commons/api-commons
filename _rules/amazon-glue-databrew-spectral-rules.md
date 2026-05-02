---
api_specs:
- filename: amazon-glue-databrew-openapi.yaml
  format: yaml
  label: AWS Glue DataBrew API
  slug: aws-glue-databrew-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-glue-databrew/refs/heads/main/openapi/amazon-glue-databrew-openapi.yaml
categories:
- info
- microcks
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Amazon Glue DataBrew.
layout: rules
name: Amazon Glue DataBrew API Rules
provider_name: Amazon Glue DataBrew
provider_slug: amazon-glue-databrew
rule_count: 7
rules:
- description: API title must reference Amazon Glue DataBrew
  given: $.info.title
  name: info-title-format
  severity: warn
- description: ''
  given: $.info
  name: info-description-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: ''
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/amazon-glue-databrew-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-glue-databrew/refs/heads/main/rules/amazon-glue-databrew-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 1
  warn: 1
slug: amazon-glue-databrew-spectral-rules
source_filename: amazon-glue-databrew-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-format:\n    description: API title must reference Amazon Glue DataBrew\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Glue DataBrew|^AWS Glue DataBrew\"\n\n  info-description-required:\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  operation-summary-required:\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-id-required:\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  response-success-required:\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required:\
  \ [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  no-empty-descriptions:\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  microcks-operation-extension:\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-glue-databrew/refs/heads/main/rules/amazon-glue-databrew-spectral-rules.yml
tags:
- Data Analytics
- Data Preparation
- ETL
- Machine Learning
- Spectral
- Linting
- API Governance
---
