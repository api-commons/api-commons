---
api_specs:
- filename: amazon-health-dashboard-openapi.yaml
  format: yaml
  label: AWS Health API
  slug: aws-health-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-health-dashboard/refs/heads/main/openapi/amazon-health-dashboard-openapi.yaml
categories:
- info
- microcks
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Amazon Health Dashboard.
layout: rules
name: Amazon Health Dashboard API Rules
provider_name: Amazon Health Dashboard
provider_slug: amazon-health-dashboard
rule_count: 7
rules:
- description: ''
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
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/amazon-health-dashboard-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-health-dashboard/refs/heads/main/rules/amazon-health-dashboard-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 2
slug: amazon-health-dashboard-spectral-rules
source_filename: amazon-health-dashboard-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-format:\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Health|^AWS Health\"\n  info-description-required:\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  operation-summary-required:\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n  operation-id-required:\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-summary-company-prefix:\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Health Dashboard\"\n  response-success-required:\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n  \
  \  then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n  microcks-operation-extension:\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-health-dashboard/refs/heads/main/rules/amazon-health-dashboard-spectral-rules.yml
tags:
- Health Monitoring
- Notifications
- Operations
- Service Status
- Spectral
- Linting
- API Governance
---
