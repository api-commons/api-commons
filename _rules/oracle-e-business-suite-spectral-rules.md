---
api_specs:
- filename: isg-rest-api.yml
  format: yaml
  label: Oracle EBS Integrated SOA Gateway REST API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/oracle-e-business-suite/refs/heads/main/openapi/isg-rest-api.yml
- filename: financial-services-api.yml
  format: yaml
  label: Oracle EBS Financial Services API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/oracle-e-business-suite/refs/heads/main/openapi/financial-services-api.yml
- filename: supply-chain-api.yml
  format: yaml
  label: Oracle EBS Supply Chain Management API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/oracle-e-business-suite/refs/heads/main/openapi/supply-chain-api.yml
- filename: human-resources-api.yml
  format: yaml
  label: Oracle EBS Human Resources API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/oracle-e-business-suite/refs/heads/main/openapi/human-resources-api.yml
- filename: manufacturing-api.yml
  format: yaml
  label: Oracle EBS Manufacturing API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/oracle-e-business-suite/refs/heads/main/openapi/manufacturing-api.yml
- filename: ecommerce-gateway-api.yml
  format: yaml
  label: Oracle EBS e-Commerce Gateway API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/oracle-e-business-suite/refs/heads/main/openapi/ecommerce-gateway-api.yml
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Oracle E-Business Suite.
layout: rules
name: Oracle E-Business Suite API Rules
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
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
rules_file: rules/oracle-e-business-suite-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/oracle-e-business-suite/refs/heads/main/rules/oracle-e-business-suite-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: oracle-e-business-suite-spectral-rules
source_filename: oracle-e-business-suite-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: summary, function: truthy}\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  response-description-required:\n    description:\
  \ Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/oracle-e-business-suite/refs/heads/main/rules/oracle-e-business-suite-spectral-rules.yml
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
- Spectral
- Linting
- API Governance
---
