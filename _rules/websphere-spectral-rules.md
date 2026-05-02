---
api_specs:
- filename: 9.0.5
  format: yaml
  label: WebSphere Application Server Admin API
  slug: websphere-admin-rest-api
  spec_type: OpenAPI
  url: https://www.ibm.com/docs/en/was/9.0.5?topic=api-openapi-specification
- filename: websphere-liberty-admin-rest-api.yml
  format: yaml
  label: WebSphere Liberty Admin REST API
  slug: websphere-liberty-admin-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/websphere/refs/heads/main/openapi/websphere-liberty-admin-rest-api.yml
- filename: websphere-liberty-rest-connector-api.yml
  format: yaml
  label: WebSphere Liberty REST Connector API
  slug: websphere-liberty-rest-connector-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/websphere/refs/heads/main/openapi/websphere-liberty-rest-connector-api.yml
- filename: websphere-mq-rest-api.yml
  format: yaml
  label: WebSphere MQ REST API
  slug: websphere-mq-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/websphere/refs/heads/main/openapi/websphere-mq-rest-api.yml
- filename: websphere-liberty-collective-controller-rest-api.yml
  format: yaml
  label: WebSphere Liberty Collective Controller REST API
  slug: websphere-liberty-collective-controller-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/websphere/refs/heads/main/openapi/websphere-liberty-collective-controller-rest-api.yml
- filename: websphere-automation-rest-api.yml
  format: yaml
  label: WebSphere Automation REST API
  slug: websphere-automation-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/websphere/refs/heads/main/openapi/websphere-automation-rest-api.yml
- filename: open-liberty-apis.yml
  format: yaml
  label: Open Liberty APIs
  slug: open-liberty-apis
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/websphere/refs/heads/main/openapi/open-liberty-apis.yml
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for IBM WebSphere.
layout: rules
name: IBM WebSphere API Rules
provider_name: IBM WebSphere
provider_slug: websphere
rule_count: 7
rules:
- description: Info title must be present
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/websphere-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/websphere/refs/heads/main/rules/websphere-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: websphere-spectral-rules
source_filename: websphere-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: summary, function: truthy}\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  response-description-required:\n    description:\
  \ Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/websphere/refs/heads/main/rules/websphere-spectral-rules.yml
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
- Spectral
- Linting
- API Governance
---
