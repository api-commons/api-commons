---
api_specs:
- filename: nav-webservices.yaml
  format: yaml
  label: Dynamics NAV Web Services API
  slug: ''
  spec_type: OpenAPI
  url: https://example.com/openapi/nav-webservices.yaml
- filename: nav-odata.yaml
  format: yaml
  label: Dynamics NAV OData API
  slug: ''
  spec_type: OpenAPI
  url: https://example.com/openapi/nav-odata.yaml
- filename: business-central-api-v2.yml
  format: yaml
  label: Business Central API v2.0
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/navision/refs/heads/main/openapi/business-central-api-v2.yml
- filename: admin-center-api.yml
  format: yaml
  label: Business Central Administration Center API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/navision/refs/heads/main/openapi/admin-center-api.yml
- filename: automation-api.yml
  format: yaml
  label: Business Central Automation API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/navision/refs/heads/main/openapi/automation-api.yml
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Microsoft Dynamics NAV.
layout: rules
name: Microsoft Dynamics NAV API Rules
provider_name: Microsoft Dynamics NAV
provider_slug: navision
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
rules_file: rules/navision-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/navision/refs/heads/main/rules/navision-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: navision-spectral-rules
source_filename: navision-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: summary, function: truthy}\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  response-description-required:\n    description:\
  \ Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/navision/refs/heads/main/rules/navision-spectral-rules.yml
tags:
- Business Management
- Dynamics NAV
- ERP
- Finance
- Inventory
- Microsoft
- Navision
- Spectral
- Linting
- API Governance
---
