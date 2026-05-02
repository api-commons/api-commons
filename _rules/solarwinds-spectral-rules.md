---
api_specs:
- filename: solarwinds-orion-openapi.yml
  format: yaml
  label: SolarWinds Orion API
  slug: solarwinds-orion-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/solarwinds/refs/heads/main/openapi/solarwinds-orion-openapi.yml
- filename: solarwinds-service-desk-openapi.yml
  format: yaml
  label: SolarWinds Service Desk API
  slug: solarwinds-service-desk-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/solarwinds/refs/heads/main/openapi/solarwinds-service-desk-openapi.yml
- filename: openapi.json
  format: json
  label: SolarWinds Observability API
  slug: solarwinds-observability-api
  spec_type: OpenAPI
  url: https://api.na-01.cloud.solarwinds.com/v1/openapi.json
- filename: solarwinds-pingdom-openapi.yml
  format: yaml
  label: SolarWinds Pingdom API
  slug: solarwinds-pingdom-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/solarwinds/refs/heads/main/openapi/solarwinds-pingdom-openapi.yml
- filename: solarwinds-loggly-openapi.yml
  format: yaml
  label: SolarWinds Loggly API
  slug: solarwinds-loggly-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/solarwinds/refs/heads/main/openapi/solarwinds-loggly-openapi.yml
- filename: solarwinds-papertrail-openapi.yml
  format: yaml
  label: SolarWinds Papertrail API
  slug: solarwinds-papertrail-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/solarwinds/refs/heads/main/openapi/solarwinds-papertrail-openapi.yml
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for SolarWinds.
layout: rules
name: SolarWinds API Rules
provider_name: SolarWinds
provider_slug: solarwinds
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
rules_file: rules/solarwinds-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/solarwinds/refs/heads/main/rules/solarwinds-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: solarwinds-spectral-rules
source_filename: solarwinds-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: summary, function: truthy}\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  response-description-required:\n    description:\
  \ Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/solarwinds/refs/heads/main/rules/solarwinds-spectral-rules.yml
tags:
- Application Monitoring
- Database Monitoring
- Infrastructure
- IP Address Management
- IT Management
- ITSM
- Log Management
- Network Monitoring
- Observability
- Spectral
- Linting
- API Governance
---
