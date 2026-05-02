---
api_specs:
- filename: apache-giraph-job-openapi.yml
  format: yaml
  label: Apache Giraph Job Monitoring API
  slug: apache-giraph-job-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-giraph/refs/heads/main/openapi/apache-giraph-job-openapi.yml
categories:
- info
- operation
- parameter
- response
description: Spectral linting rules defining API design standards and conventions for Apache Giraph.
layout: rules
name: Apache Giraph API Rules
provider_name: Apache Giraph
provider_slug: apache-giraph
rule_count: 7
rules:
- description: Info title must be defined
  given: $.info
  name: info-title-required
  severity: error
- description: API version must be specified
  given: $.info
  name: info-version-required
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with Apache Giraph
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-apache-giraph-prefix
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-operationId-required
  severity: error
- description: All responses must have descriptions
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-description-required
  severity: warn
rules_file: rules/apache-giraph-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-giraph/refs/heads/main/rules/apache-giraph-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 3
slug: apache-giraph-spectral-rules
source_filename: apache-giraph-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Apache Giraph Job API Spectral Ruleset\nrules:\n  info-title-required:\n    description: Info title must be defined\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  info-version-required:\n    description: API version must be specified\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: summary\n      function: truthy\n  operation-summary-apache-giraph-prefix:\n    description: Operation summaries should start with Apache Giraph\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache Giraph\"\n  operation-operationId-required:\n    description: All operations must have an operationId\n    severity:\
  \ error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  response-description-required:\n    description: All responses must have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].responses[*]\n    then:\n      field: description\n      function: truthy\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].parameters[*]\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-giraph/refs/heads/main/rules/apache-giraph-spectral-rules.yml
tags:
- Apache
- Big Data
- BSP
- Graph Processing
- Hadoop
- Open Source
- Retired
- Spectral
- Linting
- API Governance
---
