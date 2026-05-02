---
api_specs:
- filename: openapi.yaml
  format: yaml
  label: Microsoft Graph API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/openapi.yaml
- filename: mail.yaml
  format: yaml
  label: Outlook Mail API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/mail.yaml
- filename: calendar.yaml
  format: yaml
  label: Outlook Calendar API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/calendar.yaml
- filename: files.yaml
  format: yaml
  label: OneDrive API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/files.yaml
- filename: sites.yaml
  format: yaml
  label: SharePoint API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/sites.yaml
- filename: teams.yaml
  format: yaml
  label: Microsoft Teams API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/teams.yaml
- filename: users.yaml
  format: yaml
  label: Office 365 Users API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/users.yaml
- filename: planner.yaml
  format: yaml
  label: Planner API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/planner.yaml
- filename: microsoft-graph-api-openapi.yml
  format: yaml
  label: Office 365 Groups API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/microsoft-office-365/refs/heads/main/openapi/microsoft-graph-api-openapi.yml
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Microsoft Office 365.
layout: rules
name: Microsoft Office 365 API Rules
provider_name: Microsoft Office 365
provider_slug: microsoft-office-365
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
rules_file: rules/microsoft-office-365-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/microsoft-office-365/refs/heads/main/rules/microsoft-office-365-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: microsoft-office-365-spectral-rules
source_filename: microsoft-office-365-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: summary, function: truthy}\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  response-description-required:\n    description:\
  \ Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/microsoft-office-365/refs/heads/main/rules/microsoft-office-365-spectral-rules.yml
tags:
- Cloud
- Collaboration
- Enterprise
- Microsoft
- Productivity
- Spectral
- Linting
- API Governance
---
