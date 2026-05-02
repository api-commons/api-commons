---
api_specs:
- filename: cloudally-openapi.yml
  format: yaml
  label: CloudAlly API
  slug: cloudally-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cloudally/refs/heads/main/openapi/cloudally-openapi.yml
categories:
- cloudally
description: Spectral linting rules defining API design standards and conventions for CloudAlly.
layout: rules
name: CloudAlly API Rules
provider_name: CloudAlly
provider_slug: cloudally
rule_count: 6
rules:
- description: API info MUST contain a contact email or URL.
  given: $.info
  name: cloudally-info-contact
  severity: warn
- description: All CloudAlly API servers MUST use HTTPS.
  given: $.servers[*].url
  name: cloudally-https-only
  severity: error
- description: Operations MUST have an operationId.
  given: $.paths[*][get,post,put,delete,patch]
  name: cloudally-operation-id
  severity: error
- description: Operations MUST be tagged for resource grouping (Authentication, Partners, Users, Backups, Restore, Billing, Tasks).
  given: $.paths[*][get,post,put,delete,patch].tags
  name: cloudally-tag-required
  severity: warn
- description: API MUST define a bearer-token security scheme since CloudAlly authenticates with access tokens issued via /auth or /auth/partner.
  given: $.components.securitySchemes
  name: cloudally-bearer-auth-required
  severity: error
- description: API MUST declare at least one server URL pointing at api.cloudally.com.
  given: $.servers
  name: cloudally-server-url
  severity: error
rules_file: rules/cloudally-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cloudally/refs/heads/main/rules/cloudally-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 2
slug: cloudally-rules
source_filename: cloudally-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  cloudally-info-contact:\n    description: API info MUST contain a contact email or URL.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  cloudally-https-only:\n    description: All CloudAlly API servers MUST use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  cloudally-operation-id:\n    description: Operations MUST have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  cloudally-tag-required:\n    description: Operations MUST be tagged for resource grouping (Authentication, Partners, Users, Backups, Restore, Billing, Tasks).\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].tags\n    then:\n      function: truthy\n  cloudally-bearer-auth-required:\n    description: API\
  \ MUST define a bearer-token security scheme since CloudAlly authenticates with access tokens issued via /auth or /auth/partner.\n    severity: error\n    given: $.components.securitySchemes\n    then:\n      function: truthy\n  cloudally-server-url:\n    description: API MUST declare at least one server URL pointing at api.cloudally.com.\n    severity: error\n    given: $.servers\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cloudally/refs/heads/main/rules/cloudally-rules.yml
tags:
- Backup
- Box
- Data Protection
- Disaster Recovery
- Dropbox
- Google Workspace
- Microsoft 365
- OpenText
- SaaS Backup
- Salesforce
- Spectral
- Linting
- API Governance
---
