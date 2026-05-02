---
api_specs:
- filename: apache-geode-rest-openapi.yml
  format: yaml
  label: Apache Geode REST API
  slug: apache-geode-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-geode/refs/heads/main/openapi/apache-geode-rest-openapi.yml
categories:
- info
- operation
- parameter
- paths
- response
description: Spectral linting rules defining API design standards and conventions for Apache Geode.
layout: rules
name: Apache Geode API Rules
provider_name: Apache Geode
provider_slug: apache-geode
rule_count: 9
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
- description: Operation summaries should start with Apache Geode
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-apache-geode-prefix
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-operationId-required
  severity: error
- description: Operations should have tags
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: Paths should include API version prefix
  given: $.paths
  name: paths-versioned
  severity: info
- description: All responses must have descriptions
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-description-required
  severity: warn
rules_file: rules/apache-geode-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-geode/refs/heads/main/rules/apache-geode-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 4
slug: apache-geode-spectral-rules
source_filename: apache-geode-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Apache Geode REST API Spectral Ruleset\nrules:\n  info-title-required:\n    description: Info title must be defined\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  info-version-required:\n    description: API version must be specified\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: summary\n      function: truthy\n  operation-summary-apache-geode-prefix:\n    description: Operation summaries should start with Apache Geode\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Apache Geode\"\n  operation-operationId-required:\n    description: All operations must have an operationId\n    severity: error\n\
  \    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  operation-tags-required:\n    description: Operations should have tags\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: tags\n      function: truthy\n  paths-versioned:\n    description: Paths should include API version prefix\n    severity: info\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^/geode/v[0-9]+\"\n  response-description-required:\n    description: All responses must have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].responses[*]\n    then:\n      field: description\n      function: truthy\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].parameters[*]\n    then:\n      field: description\n      function:\
  \ truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-geode/refs/heads/main/rules/apache-geode-spectral-rules.yml
tags:
- Apache
- Caching
- Data Grid
- Distributed Systems
- In-Memory
- Open Source
- Spectral
- Linting
- API Governance
---
