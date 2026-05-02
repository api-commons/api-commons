---
api_specs:
- filename: solaris-zones-management-openapi.yml
  format: yaml
  label: Solaris Zones Management API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/solaris-zones/refs/heads/main/openapi/solaris-zones-management-openapi.yml
- filename: solaris-zone-configuration-openapi.yml
  format: yaml
  label: Zone Configuration API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/solaris-zones/refs/heads/main/openapi/solaris-zone-configuration-openapi.yml
- filename: solaris-zone-administration-openapi.yml
  format: yaml
  label: Zone Administration API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/solaris-zones/refs/heads/main/openapi/solaris-zone-administration-openapi.yml
- filename: solaris-zone-monitoring-openapi.yml
  format: yaml
  label: Zone Monitoring API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/solaris-zones/refs/heads/main/openapi/solaris-zone-monitoring-openapi.yml
- filename: solaris-rad-zonemgr-openapi.yml
  format: yaml
  label: RAD Zone Management REST API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/solaris-zones/refs/heads/main/openapi/solaris-rad-zonemgr-openapi.yml
- filename: solaris-zone-stats-openapi.yml
  format: yaml
  label: Zones Monitoring Statistics API (libzonestat)
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/solaris-zones/refs/heads/main/openapi/solaris-zone-stats-openapi.yml
- filename: solaris-kernel-zones-openapi.yml
  format: yaml
  label: Oracle Solaris Kernel Zones API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/solaris-zones/refs/heads/main/openapi/solaris-kernel-zones-openapi.yml
- filename: solaris-statsstore-openapi.yml
  format: yaml
  label: Oracle Solaris StatsStore and Analytics API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/solaris-zones/refs/heads/main/openapi/solaris-statsstore-openapi.yml
- filename: solaris-unified-archives-openapi.yml
  format: yaml
  label: Oracle Solaris Unified Archives Zones API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/solaris-zones/refs/heads/main/openapi/solaris-unified-archives-openapi.yml
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Solaris Zones.
layout: rules
name: Solaris Zones API Rules
provider_name: Solaris Zones
provider_slug: solaris-zones
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
rules_file: rules/solaris-zones-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/solaris-zones/refs/heads/main/rules/solaris-zones-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: solaris-zones-spectral-rules
source_filename: solaris-zones-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: summary, function: truthy}\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  response-description-required:\n    description:\
  \ Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/solaris-zones/refs/heads/main/rules/solaris-zones-spectral-rules.yml
tags:
- Containers
- Kernel Zones
- Operating Systems
- Oracle
- RAD
- Resource Management
- Solaris
- StatsStore
- Virtualization
- Zones
- Spectral
- Linting
- API Governance
---
