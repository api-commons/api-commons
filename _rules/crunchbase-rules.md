---
api_specs:
- filename: crunchbase-openapi.yml
  format: yaml
  label: Crunchbase API
  slug: crunchbase-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/crunchbase/refs/heads/main/openapi/crunchbase-openapi.yml
categories:
- crunchbase
description: Spectral linting rules defining API design standards and conventions for Crunchbase.
layout: rules
name: Crunchbase API Rules
provider_name: Crunchbase
provider_slug: crunchbase
rule_count: 7
rules:
- description: Crunchbase API specs must declare a contact.
  given: $.info
  name: crunchbase-info-contact
  severity: warn
- description: Crunchbase API servers must use HTTPS.
  given: $.servers[*].url
  name: crunchbase-server-https
  severity: error
- description: Crunchbase server URL must include a versioned path (e.g. /api/v4).
  given: $.servers[*].url
  name: crunchbase-api-version-path
  severity: warn
- description: Crunchbase endpoints must declare API key security.
  given: $.components.securitySchemes
  name: crunchbase-api-key-auth
  severity: error
- description: Every Crunchbase operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: crunchbase-operation-tag
  severity: warn
- description: Crunchbase operation IDs should be camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: crunchbase-operation-id-camel
  severity: warn
- description: Entity lookup paths should use entity_id path parameter.
  given: $.paths[?(@property.match(/^\/entities\//))][get].parameters[*].name
  name: crunchbase-entity-id-param
  severity: warn
rules_file: rules/crunchbase-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/crunchbase/refs/heads/main/rules/crunchbase-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 0
  warn: 5
slug: crunchbase-rules
source_filename: crunchbase-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [[spectral:oas, all]]\nrules:\n  crunchbase-info-contact:\n    description: Crunchbase API specs must declare a contact.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  crunchbase-server-https:\n    description: Crunchbase API servers must use HTTPS.\n    given: $.servers[*].url\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  crunchbase-api-version-path:\n    description: Crunchbase server URL must include a versioned path (e.g. /api/v4).\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: '/api/v[0-9]+'\n  crunchbase-api-key-auth:\n    description: Crunchbase endpoints must declare API key security.\n    given: $.components.securitySchemes\n    severity: error\n    then:\n      function: truthy\n  crunchbase-operation-tag:\n    description: Every Crunchbase operation must have at\
  \ least one tag.\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n  crunchbase-operation-id-camel:\n    description: Crunchbase operation IDs should be camelCase.\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]+$'\n  crunchbase-entity-id-param:\n    description: Entity lookup paths should use entity_id path parameter.\n    given: \"$.paths[?(@property.match(/^\\\\/entities\\\\//))][get].parameters[*].name\"\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: '^(entity_id|field_ids|card_ids)$'\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/crunchbase/refs/heads/main/rules/crunchbase-rules.yml
tags:
- Business Data
- Funding
- Investments
- Startups
- Private Markets
- Firmographics
- Spectral
- Linting
- API Governance
---
