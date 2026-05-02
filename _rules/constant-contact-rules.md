---
api_specs:
- filename: swagger.yaml
  format: yaml
  label: Constant Contact V3 API
  slug: v3
  spec_type: OpenAPI
  url: https://api.cc.email/v3/swagger.yaml
categories:
- constant
description: Spectral linting rules defining API design standards and conventions for Constant Contact.
layout: rules
name: Constant Contact API Rules
provider_name: Constant Contact
provider_slug: constant-contact
rule_count: 9
rules:
- description: API contact information must be present.
  given: $.info
  name: constant-contact-info-contact
  severity: error
- description: Host (Swagger 2.0) or server URL (OAS 3.x) must point to api.cc.email.
  given:
  - $.host
  - $.servers[*].url
  name: constant-contact-host
  severity: warn
- description: Base path must be /v3.
  given: $.basePath
  name: constant-contact-base-path
  severity: warn
- description: An OAuth2 security definition must be present.
  given:
  - $.securityDefinitions[*]
  - $.components.securitySchemes[*]
  name: constant-contact-oauth2
  severity: error
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: constant-contact-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: constant-contact-operation-tags
  severity: warn
- description: Operations should accept and return application/json.
  given: $.paths[*][post,put,patch]
  name: constant-contact-json-content
  severity: warn
- description: Mutating operations should declare 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: constant-contact-error-responses
  severity: warn
- description: Collection GETs should expose a `cursor` or `limit` query parameter.
  given: $.paths[?(@property.match(/(contacts|contact_lists|contact_tags|emails|events|segments)$/))].get
  name: constant-contact-cursor-pagination
  severity: info
rules_file: rules/constant-contact-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/constant-contact/refs/heads/main/rules/constant-contact-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 1
  warn: 5
slug: constant-contact-rules
source_filename: constant-contact-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for the Constant Contact V3 API.\n# Tuned to api.cc.email/v3 conventions: HTTPS, OAuth2 bearer tokens,\n# JSON request/response bodies, cursor pagination, and 4xx error\n# responses on mutating operations.\nrules:\n  constant-contact-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  constant-contact-host:\n    description: Host (Swagger 2.0) or server URL (OAS 3.x) must point to api.cc.email.\n    severity: warn\n    given:\n      - \"$.host\"\n      - \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(api\\\\.cc\\\\.email|^https://)\"\n\n  constant-contact-base-path:\n    description: Base path must be /v3.\n    severity: warn\n    given: \"$.basePath\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/v3\"\n\n  constant-contact-oauth2:\n\
  \    description: An OAuth2 security definition must be present.\n    severity: error\n    given:\n      - \"$.securityDefinitions[*]\"\n      - \"$.components.securitySchemes[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            type:\n              enum: [\"oauth2\"]\n\n  constant-contact-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  constant-contact-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  constant-contact-json-content:\n    description: Operations should accept and return\
  \ application/json.\n    severity: warn\n    given: \"$.paths[*][post,put,patch]\"\n    then:\n      field: consumes\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            const: \"application/json\"\n\n  constant-contact-error-responses:\n    description: Mutating operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n            - required: [\"409\"]\n            - required: [\"415\"]\n\n  constant-contact-cursor-pagination:\n    description: Collection GETs should expose a `cursor` or `limit` query parameter.\n    severity: info\n    given: \"$.paths[?(@property.match(/(contacts|contact_lists|contact_tags|emails|events|segments)$/))].get\"\
  \n    then:\n      field: parameters\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            type: object\n            properties:\n              name:\n                enum: [\"cursor\", \"limit\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/constant-contact/refs/heads/main/rules/constant-contact-rules.yml
tags:
- Campaigns
- Contacts
- Email Marketing
- Events
- Reporting
- SMS
- Surveys
- Spectral
- Linting
- API Governance
---
