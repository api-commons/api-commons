---
api_specs:
- filename: backupify-saas-protection-api.yaml
  format: yaml
  label: Backupify SaaS Protection API
  slug: saas-protection-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/backupify/refs/heads/main/openapi/backupify-saas-protection-api.yaml
categories:
- info
- openapi
- operation
- parameter
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Backupify.
layout: rules
name: Backupify API Rules
provider_name: Backupify
provider_slug: backupify
rule_count: 12
rules:
- description: Info must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: Info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.0.x
  given: $
  name: openapi-version-3
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All schemas should have a type
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Operations should define 401 response
  given: $.paths[*][get,post,put]
  name: response-401-defined
  severity: warn
rules_file: rules/backupify-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/backupify/refs/heads/main/rules/backupify-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 0
  warn: 4
slug: backupify-spectral-rules
source_filename: backupify-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info must have a title\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n  info-version-required:\n    description: Info must have a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  openapi-version-3:\n    description: Must use OpenAPI 3.0.x\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n  servers-https-only:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n  operation-id-required:\n\
  \    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n\
  \      field: description\n      function: truthy\n  schema-type-defined:\n    description: All schemas should have a type\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n  response-401-defined:\n    description: Operations should define 401 response\n    severity: warn\n    given: $.paths[*][get,post,put]\n    then:\n      field: responses.401\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/backupify/refs/heads/main/rules/backupify-spectral-rules.yml
tags:
- SaaS Backup
- Data Protection
- Cloud Backup
- Microsoft 365
- Google Workspace
- Spectral
- Linting
- API Governance
---
