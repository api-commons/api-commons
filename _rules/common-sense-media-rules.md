---
api_specs:
- filename: common-sense-media-reviews-api-openapi.yml
  format: yaml
  label: Common Sense Media Reviews API
  slug: common-sense-media-reviews-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/common-sense-media/refs/heads/main/openapi/common-sense-media-reviews-api-openapi.yml
categories:
- csm
description: Spectral linting rules defining API design standards and conventions for Common Sense Media.
layout: rules
name: Common Sense Media API Rules
provider_name: Common Sense Media
provider_slug: common-sense-media
rule_count: 9
rules:
- description: API info must include a contact block.
  given: $.info
  name: csm-info-contact
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: csm-server-https
  severity: error
- description: Server URL should point to api.commonsense.org.
  given: $.servers[*].url
  name: csm-server-host
  severity: warn
- description: Server URL should include the /api/v3 path prefix.
  given: $.servers[*].url
  name: csm-version-prefix
  severity: info
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: csm-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: csm-operation-tags
  severity: warn
- description: Common Sense Media v3 only supports GET methods.
  given: $.paths[*]
  name: csm-only-get
  severity: warn
- description: API key security scheme must be declared.
  given: $.components.securitySchemes
  name: csm-api-key-security
  severity: error
- description: Item-scoped paths should be keyed by a UUID parameter.
  given: $.paths[?(@property.indexOf('reviewId') > -1)]
  name: csm-uuid-paths
  severity: info
rules_file: rules/common-sense-media-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/common-sense-media/refs/heads/main/rules/common-sense-media-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 2
  warn: 3
slug: common-sense-media-rules
source_filename: common-sense-media-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for the Common Sense Media Reviews API (v3).\n# Tuned to api.commonsense.org conventions: x-api-key header, GET-only\n# review browsing, and UUID-keyed entities.\nrules:\n  csm-info-contact:\n    description: API info must include a contact block.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  csm-server-https:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  csm-server-host:\n    description: Server URL should point to api.commonsense.org.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"api\\\\.commonsense\\\\.org\"\n\n  csm-version-prefix:\n    description: Server URL should include the /api/v3 path prefix.\n    severity: info\n    given:\
  \ \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/api/v3\"\n\n  csm-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  csm-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  csm-only-get:\n    description: Common Sense Media v3 only supports GET methods.\n    severity: warn\n    given: \"$.paths[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          not:\n            anyOf:\n              - required: [post]\n              - required: [put]\n              - required:\
  \ [patch]\n              - required: [delete]\n\n  csm-api-key-security:\n    description: API key security scheme must be declared.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            ApiKey:\n              type: object\n              properties:\n                type:\n                  const: apiKey\n                in:\n                  const: header\n                name:\n                  const: X-Api-Key\n\n  csm-uuid-paths:\n    description: Item-scoped paths should be keyed by a UUID parameter.\n    severity: info\n    given: \"$.paths[?(@property.indexOf('reviewId') > -1)]\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"{reviewId}\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/common-sense-media/refs/heads/main/rules/common-sense-media-rules.yml
tags:
- Apps
- Books
- Media
- Movies
- Non-Profit
- Podcasts
- Ratings
- Reviews
- Television
- Video Games
- YouTube
- Spectral
- Linting
- API Governance
---
