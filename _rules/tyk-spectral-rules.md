---
api_specs:
- filename: tyk-gateway-api-openapi.yml
  format: yaml
  label: Tyk Gateway API
  slug: tyk-gateway-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/tyk/refs/heads/main/openapi/tyk-gateway-api-openapi.yml
- filename: tyk-dashboard-api-openapi.yml
  format: yaml
  label: Tyk Dashboard API
  slug: tyk-dashboard-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/tyk/refs/heads/main/openapi/tyk-dashboard-api-openapi.yml
- filename: tyk-dashboard-admin-api-openapi.yml
  format: yaml
  label: Tyk Dashboard Admin API
  slug: tyk-dashboard-admin-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/tyk/refs/heads/main/openapi/tyk-dashboard-admin-api-openapi.yml
- filename: tyk-mdcb-api-openapi.yml
  format: yaml
  label: Tyk MDCB API
  slug: tyk-mdcb-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/tyk/refs/heads/main/openapi/tyk-mdcb-api-openapi.yml
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Tyk.
layout: rules
name: Tyk API Rules
provider_name: Tyk
provider_slug: tyk
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
rules_file: rules/tyk-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/tyk/refs/heads/main/rules/tyk-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: tyk-spectral-rules
source_filename: tyk-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: summary, function: truthy}\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  response-description-required:\n    description:\
  \ Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/tyk/refs/heads/main/rules/tyk-spectral-rules.yml
tags:
- API Gateway
- API Management
- GraphQL
- Open Source
- Spectral
- Linting
- API Governance
---
