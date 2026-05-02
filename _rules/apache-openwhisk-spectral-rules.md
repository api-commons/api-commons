---
api_specs:
- filename: apache-openwhisk-rest-api.yaml
  format: yaml
  label: Apache OpenWhisk REST API
  slug: apache-openwhisk-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-openwhisk/refs/heads/main/openapi/apache-openwhisk-rest-api.yaml
categories:
- info
- operation
- paths
- response
- schema
- security
description: Spectral linting rules defining API design standards and conventions for Apache OpenWhisk.
layout: rules
name: Apache OpenWhisk API Rules
provider_name: Apache OpenWhisk
provider_slug: apache-openwhisk
rule_count: 10
rules:
- description: API must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: Operations must have summaries
  given: $.paths[*][*]
  name: operation-summary-required
  severity: error
- description: Operations must have operationIds
  given: $.paths[*][*]
  name: operation-operationId-required
  severity: error
- description: Operations must have tags
  given: $.paths[*][*]
  name: operation-tags-required
  severity: warn
- description: Summaries should start with Apache OpenWhisk
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-apache-prefix
  severity: info
- description: Paths should be versioned under /api/v1
  given: $.servers[*].url
  name: paths-api-versioned
  severity: info
- description: API should use HTTP Basic authentication
  given: $.components.securitySchemes
  name: security-basic-auth
  severity: warn
- description: Operations must have a 200 success response
  given: $.paths[*][get,post,put].responses
  name: response-success-required
  severity: error
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-properties-described
  severity: info
- description: Parameters should have descriptions
  given: $.paths[*][*].parameters[*]
  name: operation-parameters-described
  severity: warn
rules_file: rules/apache-openwhisk-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-openwhisk/refs/heads/main/rules/apache-openwhisk-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 3
  warn: 3
slug: apache-openwhisk-spectral-rules
source_filename: apache-openwhisk-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: \"spectral:oas\"\nrules:\n  info-title-required:\n    description: \"API must have a title\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n  operation-summary-required:\n    description: \"Operations must have summaries\"\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: summary\n      function: truthy\n  operation-operationId-required:\n    description: \"Operations must have operationIds\"\n    severity: error\n    given: \"$.paths[*][*]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-tags-required:\n    description: \"Operations must have tags\"\n    severity: warn\n    given: \"$.paths[*][*]\"\n    then:\n      field: tags\n      function: truthy\n  operation-summary-apache-prefix:\n    description: \"Summaries should start with Apache OpenWhisk\"\n    severity: info\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\n    then:\n      function:\
  \ pattern\n      functionOptions:\n        match: \"^Apache OpenWhisk\"\n  paths-api-versioned:\n    description: \"Paths should be versioned under /api/v1\"\n    severity: info\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/api/v1$\"\n  security-basic-auth:\n    description: \"API should use HTTP Basic authentication\"\n    severity: warn\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n  response-success-required:\n    description: \"Operations must have a 200 success response\"\n    severity: error\n    given: \"$.paths[*][get,post,put].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          required: [\"200\"]\n  schema-properties-described:\n    description: \"Schema properties should have descriptions\"\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n  operation-parameters-described:\n\
  \    description: \"Parameters should have descriptions\"\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-openwhisk/refs/heads/main/rules/apache-openwhisk-spectral-rules.yml
tags:
- Cloud Native
- Event-Driven
- FaaS
- Serverless
- Apache
- Open Source
- Functions
- Spectral
- Linting
- API Governance
---
