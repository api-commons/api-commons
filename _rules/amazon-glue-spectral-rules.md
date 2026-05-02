---
api_specs:
- filename: amazon-glue-openapi.yml
  format: yaml
  label: Amazon Glue API
  slug: amazon-glue-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-glue/refs/heads/main/openapi/amazon-glue-openapi.yml
categories:
- info
- microcks
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Amazon Glue.
layout: rules
name: Amazon Glue API Rules
provider_name: Amazon Glue
provider_slug: amazon-glue
rule_count: 8
rules:
- description: API title must reference Amazon Glue
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
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-company-prefix
  severity: warn
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
rules_file: rules/amazon-glue-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-glue/refs/heads/main/rules/amazon-glue-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 1
  warn: 2
slug: amazon-glue-spectral-rules
source_filename: amazon-glue-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-format:\n    description: API title must reference Amazon Glue\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Glue\"\n  info-description-required:\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  operation-summary-required:\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n  operation-id-required:\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-summary-company-prefix:\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Glue\"\n  response-success-required:\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\
  \n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n  no-empty-descriptions:\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n  microcks-operation-extension:\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-glue/refs/heads/main/rules/amazon-glue-spectral-rules.yml
tags:
- Analytics
- Data Catalog
- Data Integration
- Data Pipeline
- ETL
- Serverless
- Spectral
- Linting
- API Governance
---
