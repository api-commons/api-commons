---
api_specs:
- filename: cursor-admin-api-openapi.yml
  format: yaml
  label: Cursor Admin API
  slug: admin-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/openapi/cursor-admin-api-openapi.yml
categories:
- cursor
description: Spectral linting rules defining API design standards and conventions for Cursor.
layout: rules
name: Cursor API Rules
provider_name: Cursor
provider_slug: cursor
rule_count: 6
rules:
- description: Cursor Admin API spec must declare a contact.
  given: $.info
  name: cursor-admin-info-contact
  severity: warn
- description: Cursor Admin API server URLs must use HTTPS.
  given: $.servers[*].url
  name: cursor-admin-server-https
  severity: error
- description: Cursor Admin API base URL must be api.cursor.com.
  given: $.servers[*].url
  name: cursor-admin-base-url
  severity: error
- description: Cursor Admin API uses HTTP Basic auth via securitySchemes.
  given: $.components.securitySchemes
  name: cursor-admin-basic-auth
  severity: warn
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cursor-admin-tags-required
  severity: warn
- description: Every operation must declare an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cursor-admin-operation-id-required
  severity: error
rules_file: rules/cursor-admin-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/rules/cursor-admin-api-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 3
slug: cursor-admin-api-rules
source_filename: cursor-admin-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  cursor-admin-info-contact:\n    description: Cursor Admin API spec must declare a contact.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  cursor-admin-server-https:\n    description: Cursor Admin API server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  cursor-admin-base-url:\n    description: Cursor Admin API base URL must be api.cursor.com.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://api\\.cursor\\.com'\n  cursor-admin-basic-auth:\n    description: Cursor Admin API uses HTTP Basic auth via securitySchemes.\n    severity: warn\n    given: $.components.securitySchemes\n    then:\n      field: BasicAuth\n      function: truthy\n  cursor-admin-tags-required:\n    description: Every operation\
  \ must declare at least one tag.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n  cursor-admin-operation-id-required:\n    description: Every operation must declare an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/rules/cursor-admin-api-rules.yml
tags:
- AI
- AI Editor
- Code Generation
- Coding Assistant
- Copilot
- Developer Tools
- LLM
- Productivity
- VSCode Fork
- Spectral
- Linting
- API Governance
---
