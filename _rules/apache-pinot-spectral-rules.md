---
api_specs:
- filename: apache-pinot-rest-api.yaml
  format: yaml
  label: Apache Pinot REST API
  slug: apache-pinot-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-pinot/refs/heads/main/openapi/apache-pinot-rest-api.yaml
categories:
- info
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Apache Pinot.
layout: rules
name: Apache Pinot API Rules
provider_name: Apache Pinot
provider_slug: apache-pinot
rule_count: 5
rules:
- description: ''
  given: $.info
  name: info-title-required
  severity: error
- description: ''
  given: $.paths[*][*]
  name: operation-summary-required
  severity: error
- description: ''
  given: $.paths[*][*]
  name: operation-operationId-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-apache-prefix
  severity: info
- description: ''
  given: $.paths[*][get,post,put].responses
  name: response-success-required
  severity: error
rules_file: rules/apache-pinot-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-pinot/refs/heads/main/rules/apache-pinot-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 0
slug: apache-pinot-spectral-rules
source_filename: apache-pinot-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: \"spectral:oas\"\nrules:\n  info-title-required:\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n  operation-summary-required:\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: summary\n      function: truthy\n  operation-operationId-required:\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-summary-apache-prefix:\n    severity: info\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache Pinot\"\n  response-success-required:\n    severity: error\n    given: \"$.paths[*][get,post,put].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          required: [\"200\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-pinot/refs/heads/main/rules/apache-pinot-spectral-rules.yml
tags:
- Analytics
- Database
- Low Latency
- OLAP
- Real-Time
- Apache
- Open Source
- Spectral
- Linting
- API Governance
---
