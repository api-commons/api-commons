---
api_specs:
- filename: apache-flume-monitoring-openapi.yml
  format: yaml
  label: Apache Flume Monitoring API
  slug: apache-flume-monitoring-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-flume/refs/heads/main/openapi/apache-flume-monitoring-openapi.yml
categories:
- info
- operation
- response
- schema
description: Spectral linting rules defining API design standards and conventions for Apache Flume.
layout: rules
name: Apache Flume API Rules
provider_name: Apache Flume
provider_slug: apache-flume
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
- description: Operation summaries should start with Apache Flume
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-apache-flume-prefix
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-operationId-required
  severity: error
- description: All responses must have descriptions
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: warn
- description: Schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: info
rules_file: rules/apache-flume-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-flume/refs/heads/main/rules/apache-flume-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 2
slug: apache-flume-spectral-rules
source_filename: apache-flume-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Apache Flume Monitoring API Spectral Ruleset\nrules:\n  info-title-required:\n    description: Info title must be defined\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  info-version-required:\n    description: API version must be specified\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: summary\n      function: truthy\n  operation-summary-apache-flume-prefix:\n    description: Operation summaries should start with Apache Flume\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache Flume\"\n  operation-operationId-required:\n    description: All operations must have an operationId\n    severity:\
  \ error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  response-description-required:\n    description: All responses must have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].responses[*]\n    then:\n      field: description\n      function: truthy\n  schema-description-recommended:\n    description: Schemas should have descriptions\n    severity: info\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-flume/refs/heads/main/rules/apache-flume-spectral-rules.yml
tags:
- Apache
- Data Collection
- ETL
- Log Aggregation
- Open Source
- Streaming
- Spectral
- Linting
- API Governance
---
