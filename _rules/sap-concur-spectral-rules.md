---
api_specs:
- filename: expense-report.json
  format: json
  label: Concur Expense API
  slug: ''
  spec_type: OpenAPI
  url: https://developer.concur.com/api-reference/expense/expense-report/expense-report.json
- filename: itinerary.json
  format: json
  label: Concur Travel API
  slug: ''
  spec_type: OpenAPI
  url: https://developer.concur.com/api-reference/travel/itinerary/itinerary.json
- filename: v3.invoice.json
  format: json
  label: Concur Invoice API
  slug: ''
  spec_type: OpenAPI
  url: https://developer.concur.com/api-reference/invoice/v3.invoice.json
- filename: v4.request.json
  format: json
  label: Concur Request API
  slug: ''
  spec_type: OpenAPI
  url: https://developer.concur.com/api-reference/request/v4.request.json
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for SAP Concur.
layout: rules
name: SAP Concur API Rules
provider_name: SAP Concur
provider_slug: sap-concur
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
rules_file: rules/sap-concur-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/sap-concur/refs/heads/main/rules/sap-concur-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: sap-concur-spectral-rules
source_filename: sap-concur-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: summary, function: truthy}\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  response-description-required:\n    description:\
  \ Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/sap-concur/refs/heads/main/rules/sap-concur-spectral-rules.yml
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
- Spectral
- Linting
- API Governance
---
