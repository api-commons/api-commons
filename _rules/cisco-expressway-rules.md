---
api_specs:
- filename: cisco-expressway-configuration-api-openapi.yml
  format: yaml
  label: Cisco Expressway Configuration API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-expressway/refs/heads/main/openapi/cisco-expressway-configuration-api-openapi.yml
- filename: cisco-expressway-status-api-openapi.yml
  format: yaml
  label: Cisco Expressway Status API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cisco-expressway/refs/heads/main/openapi/cisco-expressway-status-api-openapi.yml
categories:
- expressway
description: Spectral linting rules defining API design standards and conventions for Cisco Expressway.
layout: rules
name: Cisco Expressway API Rules
provider_name: Cisco Expressway
provider_slug: cisco-expressway
rule_count: 8
rules:
- description: API contact information must be present.
  given: $.info
  name: expressway-info-contact
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: expressway-server-https
  severity: error
- description: Servers must include /api/provisioning or /api/status.
  given: $.servers[*].url
  name: expressway-server-base-path
  severity: warn
- description: A basic-auth security scheme must be defined.
  given: $.components.securitySchemes[*]
  name: expressway-basic-auth
  severity: error
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: expressway-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: expressway-operation-tags
  severity: warn
- description: Provisioning collection paths should be plural nouns.
  given: $.paths[?(@property.indexOf('/api/provisioning/') > -1)]~
  name: expressway-zone-collection-naming
  severity: info
- description: Mutating operations should declare 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: expressway-error-responses
  severity: warn
rules_file: rules/cisco-expressway-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cisco-expressway/refs/heads/main/rules/cisco-expressway-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 3
slug: cisco-expressway-rules
source_filename: cisco-expressway-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting tuned for Cisco Expressway REST APIs.\n# Per the X14.x REST API summary guide, Expressway uses HTTP Basic auth\n# over HTTPS, /api/provisioning/* for configuration, /api/status/* for\n# observability, JSON Schema Draft-04 request/response shapes, and\n# returns 200/201/204 on success.\nrules:\n  expressway-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  expressway-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  expressway-server-base-path:\n    description: Servers must include /api/provisioning or /api/status.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match:\
  \ \"/api/(provisioning|status|xmlapi)\"\n\n  expressway-basic-auth:\n    description: A basic-auth security scheme must be defined.\n    severity: error\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            type:\n              enum: [\"http\"]\n            scheme:\n              enum: [\"basic\"]\n\n  expressway-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  expressway-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  expressway-zone-collection-naming:\n\
  \    description: Provisioning collection paths should be plural nouns.\n    severity: info\n    given: \"$.paths[?(@property.indexOf('/api/provisioning/') > -1)]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(zones|searchrules|transforms|dns|ntp|users|peers)\"\n\n  expressway-error-responses:\n    description: Mutating operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n            - required: [\"409\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cisco-expressway/refs/heads/main/rules/cisco-expressway-rules.yml
tags:
- Collaboration
- Firewall Traversal
- H.323
- Session Border Controller
- SIP
- Unified Communications
- Video Conferencing
- Spectral
- Linting
- API Governance
---
