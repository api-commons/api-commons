---
api_specs:
- filename: openapi.json
  format: json
  label: Webex Admin API
  slug: webex-admin-api
  spec_type: OpenAPI
  url: https://developer.webex.com/docs/api/v1/openapi.json
- filename: openapi.json
  format: json
  label: Webex Calling API
  slug: webex-calling-api
  spec_type: OpenAPI
  url: https://developer.webex.com/docs/api/v1/openapi.json
- filename: openapi.json
  format: json
  label: Webex Devices API
  slug: webex-devices-api
  spec_type: OpenAPI
  url: https://developer.webex.com/docs/api/v1/openapi.json
- filename: openapi.json
  format: json
  label: Webex Workspaces API
  slug: webex-workspaces-api
  spec_type: OpenAPI
  url: https://developer.webex.com/docs/api/v1/openapi.json
- filename: openapi.json
  format: json
  label: Webex People API
  slug: webex-people-api
  spec_type: OpenAPI
  url: https://developer.webex.com/docs/api/v1/openapi.json
- filename: openapi.json
  format: json
  label: Webex Organizations API
  slug: webex-organizations-api
  spec_type: OpenAPI
  url: https://developer.webex.com/docs/api/v1/openapi.json
- filename: openapi.json
  format: json
  label: Webex Licenses API
  slug: webex-licenses-api
  spec_type: OpenAPI
  url: https://developer.webex.com/docs/api/v1/openapi.json
- filename: openapi.json
  format: json
  label: Webex Locations API
  slug: webex-locations-api
  spec_type: OpenAPI
  url: https://developer.webex.com/docs/api/v1/openapi.json
- filename: openapi.json
  format: json
  label: Webex Reports API
  slug: webex-reports-api
  spec_type: OpenAPI
  url: https://developer.webex.com/docs/api/v1/openapi.json
categories:
- webex
description: Spectral linting rules defining API design standards and conventions for Cisco Control Hub.
layout: rules
name: Cisco Control Hub API Rules
provider_name: Cisco Control Hub
provider_slug: cisco-control-hub
rule_count: 8
rules:
- description: API contact information must be present.
  given: $.info
  name: webex-info-contact
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: webex-server-https
  severity: error
- description: webexapis.com servers must include /v1.
  given: $.servers[?(@.url && @.url.indexOf('webexapis.com') > -1)].url
  name: webex-server-base-path
  severity: warn
- description: An OAuth 2.0 security scheme must be defined.
  given: $.components.securitySchemes[*]
  name: webex-oauth-security
  severity: warn
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: webex-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: webex-operation-tags
  severity: warn
- description: List endpoints should support max/cursor or start pagination.
  given: $.paths[*].get.parameters[*].name
  name: webex-pagination-cursor
  severity: info
- description: Mutating operations should declare 4xx/5xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: webex-error-responses
  severity: warn
rules_file: rules/cisco-control-hub-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cisco-control-hub/refs/heads/main/rules/cisco-control-hub-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 1
  warn: 4
slug: cisco-control-hub-rules
source_filename: cisco-control-hub-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting tuned for the Cisco Control Hub / Webex Admin APIs\n# at webexapis.com. Validates HTTPS, /v1 base path, OAuth bearer auth,\n# operationId/tag conventions, and standard error responses.\nrules:\n  webex-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  webex-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  webex-server-base-path:\n    description: webexapis.com servers must include /v1.\n    severity: warn\n    given: \"$.servers[?(@.url && @.url.indexOf('webexapis.com') > -1)].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/v1\"\n\n  webex-oauth-security:\n    description: An OAuth 2.0 security scheme\
  \ must be defined.\n    severity: warn\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            type:\n              enum: [\"oauth2\", \"http\"]\n\n  webex-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  webex-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  webex-pagination-cursor:\n    description: List endpoints should support max/cursor or start pagination.\n    severity: info\n    given: \"$.paths[*].get.parameters[*].name\"\n    then:\n  \
  \    function: enumeration\n      functionOptions:\n        values:\n          - max\n          - start\n          - cursor\n          - orgId\n          - personId\n          - email\n\n  webex-error-responses:\n    description: Mutating operations should declare 4xx/5xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n            - required: [\"409\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cisco-control-hub/refs/heads/main/rules/cisco-control-hub-rules.yml
tags:
- Administration
- Calling
- Collaboration
- Communications
- Device Management
- Identity Management
- Licenses
- Reporting
- Webex
- Spectral
- Linting
- API Governance
---
