---
api_specs:
- filename: cnh-fieldops-openapi.yml
  format: yaml
  label: CNH FieldOps API
  slug: cnh-fieldops-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cnh/refs/heads/main/openapi/cnh-fieldops-openapi.yml
categories:
- cnh
description: Spectral linting rules defining API design standards and conventions for CNH.
layout: rules
name: CNH API Rules
provider_name: CNH
provider_slug: cnh
rule_count: 9
rules:
- description: API contact information must be present.
  given: $.info
  name: cnh-info-contact
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: cnh-server-https
  severity: error
- description: Production server should target api.fieldops.cnh.com or api.cnh.com.
  given: $.servers[*].url
  name: cnh-server-host
  severity: warn
- description: An OAuth 2.0 security scheme must be defined.
  given: $.components.securitySchemes[*]
  name: cnh-oauth-security
  severity: error
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cnh-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cnh-operation-tags
  severity: warn
- description: Telemetry GET operations must accept startDate and endDate query parameters (one-day window recommended).
  given: $.paths[?(@property && @property.indexOf('/telemetry') > -1 || @property.indexOf('/metrics') > -1)].get
  name: cnh-telemetry-date-range
  severity: warn
- description: Telemetry endpoints should expose a `profile` parameter restricted to CP or MH.
  given: $.paths[?(@property && @property.indexOf('/telemetry') > -1)].get.parameters[?(@.name == 'profile')].schema
  name: cnh-iso15143-profile
  severity: info
- description: Operations should declare 401 Unauthorized response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: cnh-error-401
  severity: warn
rules_file: rules/cnh-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cnh/refs/heads/main/rules/cnh-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 4
slug: cnh-rules
source_filename: cnh-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for CNH FieldOps API.\n# Tuned to api.fieldops.cnh.com conventions: HTTPS-only, OAuth 2.0 with\n# refresh/access tokens, ISO 15143-3 telemetry profiles (CP/MH), and\n# tag-grouped resources for equipment, telemetry, operations,\n# prescriptions, farm setup, and webhooks.\nrules:\n  cnh-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  cnh-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  cnh-server-host:\n    description: Production server should target api.fieldops.cnh.com or api.cnh.com.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(api\\\\.fieldops\\\
  \\.cnh\\\\.com|api\\\\.cnh\\\\.com)\"\n\n  cnh-oauth-security:\n    description: An OAuth 2.0 security scheme must be defined.\n    severity: error\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            type:\n              enum: [\"oauth2\", \"openIdConnect\"]\n\n  cnh-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  cnh-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  cnh-telemetry-date-range:\n    description: Telemetry GET operations must accept\
  \ startDate and endDate query parameters (one-day window recommended).\n    severity: warn\n    given: \"$.paths[?(@property && @property.indexOf('/telemetry') > -1 || @property.indexOf('/metrics') > -1)].get\"\n    then:\n      field: parameters\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  cnh-iso15143-profile:\n    description: Telemetry endpoints should expose a `profile` parameter restricted to CP or MH.\n    severity: info\n    given: \"$.paths[?(@property && @property.indexOf('/telemetry') > -1)].get.parameters[?(@.name == 'profile')].schema\"\n    then:\n      field: enum\n      function: truthy\n\n  cnh-error-401:\n    description: Operations should declare 401 Unauthorized response.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [\"401\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cnh/refs/heads/main/rules/cnh-rules.yml
tags:
- Agriculture
- Construction
- Telematics
- Equipment
- FieldOps
- Spectral
- Linting
- API Governance
---
