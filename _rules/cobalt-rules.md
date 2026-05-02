---
api_specs:
- filename: cobalt-api-openapi.yml
  format: yaml
  label: Cobalt API
  slug: cobalt-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cobalt/refs/heads/main/openapi/cobalt-api-openapi.yml
categories:
- cobalt
description: Spectral linting rules defining API design standards and conventions for Cobalt.
layout: rules
name: Cobalt API Rules
provider_name: Cobalt
provider_slug: cobalt
rule_count: 13
rules:
- description: API contact information must be present.
  given: $.info
  name: cobalt-info-contact
  severity: error
- description: API license must be declared.
  given: $.info
  name: cobalt-info-license
  severity: warn
- description: API termsOfService link should be declared.
  given: $.info
  name: cobalt-info-terms
  severity: warn
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: cobalt-server-https
  severity: error
- description: Cobalt server URLs must include /api/v2.
  given: $.servers[?(@.url && @.url.indexOf('gocobalt.io') > -1)].url
  name: cobalt-server-versioned
  severity: warn
- description: An apiKey security scheme must be defined.
  given: $.components.securitySchemes
  name: cobalt-apikey-security
  severity: error
- description: All Cobalt API paths should live under /public.
  given: $.paths
  name: cobalt-public-path-prefix
  severity: warn
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cobalt-operation-tags
  severity: warn
- description: Every operation must include a short summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: cobalt-operation-summary
  severity: warn
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cobalt-operation-id
  severity: error
- description: Operation IDs should be camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: cobalt-operation-id-camelcase
  severity: warn
- description: Mutating operations should declare 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: cobalt-error-responses
  severity: warn
- description: List endpoints should expose page/limit pagination.
  given: $.paths[?(@property.match(/linked-account$|application$|execution$|records$/))].get.parameters[*].name
  name: cobalt-pagination-page-limit
  severity: info
rules_file: rules/cobalt-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cobalt/refs/heads/main/rules/cobalt-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 8
slug: cobalt-rules
source_filename: cobalt-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules tuned for the Cobalt embedded iPaaS API.\n# Validates that OpenAPI specs follow the conventions documented at\n# https://docs.gocobalt.io/api-reference/overview - apiKey-based auth,\n# JSON responses, and resource-oriented /public/* paths under\n# https://api.gocobalt.io/api/v2.\nrules:\n  cobalt-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  cobalt-info-license:\n    description: API license must be declared.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  cobalt-info-terms:\n    description: API termsOfService link should be declared.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: termsOfService\n      function: truthy\n\n  cobalt-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n\
  \    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  cobalt-server-versioned:\n    description: Cobalt server URLs must include /api/v2.\n    severity: warn\n    given: \"$.servers[?(@.url && @.url.indexOf('gocobalt.io') > -1)].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/api/v2$\"\n\n  cobalt-apikey-security:\n    description: An apiKey security scheme must be defined.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  cobalt-public-path-prefix:\n    description: All Cobalt API paths should live under /public.\n    severity: warn\n    given: \"$.paths\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          patternProperties:\n            \"^/public/\":\n              type: object\n          additionalProperties: false\n\n  cobalt-operation-tags:\n    description:\
  \ Every operation must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  cobalt-operation-summary:\n    description: Every operation must include a short summary.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  cobalt-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  cobalt-operation-id-camelcase:\n    description: Operation IDs should be camelCase.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n\
  \  cobalt-error-responses:\n    description: Mutating operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n            - required: [\"422\"]\n\n  cobalt-pagination-page-limit:\n    description: List endpoints should expose page/limit pagination.\n    severity: info\n    given: \"$.paths[?(@property.match(/linked-account$|application$|execution$|records$/))].get.parameters[*].name\"\n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - page\n          - limit\n          - linked_account_id\n          - workflow_id\n          - status\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cobalt/refs/heads/main/rules/cobalt-rules.yml
tags:
- Automation
- Embedded iPaaS
- Integrations
- Spectral
- Linting
- API Governance
---
