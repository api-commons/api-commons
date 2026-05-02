---
api_specs:
- filename: apache-jmeter-rest-api.yaml
  format: yaml
  label: Apache JMeter REST API
  slug: rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apache-jmeter/refs/heads/main/openapi/apache-jmeter-rest-api.yaml
categories:
- get
- info
- 'no'
- openapi
- operation
- response
- schema
- servers
description: Spectral linting rules defining API design standards and conventions for Apache JMeter.
layout: rules
name: Apache JMeter API Rules
provider_name: Apache JMeter
provider_slug: apache-jmeter
rule_count: 12
rules:
- description: Info title should start with Apache JMeter
  given: $.info
  name: info-title-prefix
  severity: warn
- description: Info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Responses must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Every operation must have a 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-2xx-required
  severity: error
- description: GET operations must not have request bodies
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/apache-jmeter-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apache-jmeter/refs/heads/main/rules/apache-jmeter-spectral-rules.yml
severity_counts:
  error: 9
  hint: 0
  info: 1
  warn: 2
slug: apache-jmeter-spectral-rules
source_filename: apache-jmeter-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-prefix:\n    description: Info title should start with Apache JMeter\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: \"^Apache JMeter\"\n\n  info-version-required:\n    description: Info must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  openapi-version:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  servers-defined:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n \
  \     function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  response-description-required:\n    description: Responses must have descriptions\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-2xx-required:\n    description: Every operation must have a 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n       \
  \     - required: [\"201\"]\n            - required: [\"204\"]\n\n  get-no-request-body:\n    description: GET operations must not have request bodies\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  schema-description-required:\n    description: Component schemas should have descriptions\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apache-jmeter/refs/heads/main/rules/apache-jmeter-spectral-rules.yml
tags:
- API Testing
- Java
- Load Testing
- Open Source
- Performance Testing
- Stress Testing
- Spectral
- Linting
- API Governance
---
