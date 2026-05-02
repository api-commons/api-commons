---
api_specs:
- filename: splunk-enterprise-rest-api.yml
  format: yaml
  label: Splunk Enterprise REST API
  slug: splunk-enterprise-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/splunk/refs/heads/main/openapi/splunk-enterprise-rest-api.yml
- filename: openapi.json
  format: json
  label: Splunk Cloud ACS OpenAPI Specification
  slug: splunk-cloud-admin-config-service-openapi
  spec_type: OpenAPI
  url: https://admin.splunk.com/service/info/specs/v2/openapi.json
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Splunk.
layout: rules
name: Splunk API Rules
provider_name: Splunk
provider_slug: splunk
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
rules_file: rules/splunk-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/splunk/refs/heads/main/rules/splunk-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: splunk-spectral-rules
source_filename: splunk-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: summary, function: truthy}\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  response-description-required:\n    description:\
  \ Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/splunk/refs/heads/main/rules/splunk-spectral-rules.yml
tags:
- Analytics
- Data Analysis
- Logging
- Machine Data
- Monitoring
- Observability
- Platform
- Security
- SIEM
- Spectral
- Linting
- API Governance
---
