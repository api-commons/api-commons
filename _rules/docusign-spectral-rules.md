---
api_specs:
- filename: docusign-openapi-original.yml
  format: yaml
  label: Docusign eSignature REST API
  slug: docusign-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/docusign/refs/heads/main/openapi/docusign-openapi-original.yml
- filename: docusign-admin-openapi-original.yml
  format: yaml
  label: Docusign Admin API
  slug: docusign-admin-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/docusign/refs/heads/main/openapi/docusign-admin-openapi-original.yml
- filename: docusign-click-openapi-original.yml
  format: yaml
  label: Docusign Click API
  slug: docusign-click-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/docusign/refs/heads/main/openapi/docusign-click-openapi-original.yml
- filename: docusign-maestro-openapi-original.yml
  format: yaml
  label: Docusign Maestro API
  slug: docusign-maestro-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/docusign/refs/heads/main/openapi/docusign-maestro-openapi-original.yml
- filename: docusign-monitor-openapi-original.yml
  format: yaml
  label: Docusign Monitor API
  slug: docusign-monitor-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/docusign/refs/heads/main/openapi/docusign-monitor-openapi-original.yml
- filename: docusign-rooms-openapi-original.yml
  format: yaml
  label: Docusign Rooms API
  slug: docusign-rooms-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/docusign/refs/heads/main/openapi/docusign-rooms-openapi-original.yml
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Docusign.
layout: rules
name: Docusign API Rules
provider_name: Docusign
provider_slug: docusign
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
rules_file: rules/docusign-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/docusign/refs/heads/main/rules/docusign-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: docusign-spectral-rules
source_filename: docusign-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: summary, function: truthy}\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  response-description-required:\n    description:\
  \ Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/docusign/refs/heads/main/rules/docusign-spectral-rules.yml
tags:
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
- Spectral
- Linting
- API Governance
---
