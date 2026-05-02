---
api_specs:
- filename: corporate-bullshit-generator-api-openapi.yml
  format: yaml
  label: Corporate Bullshit Generator API
  slug: cbsg-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/corporate-bullshit-generator-api/refs/heads/main/openapi/corporate-bullshit-generator-api-openapi.yml
categories:
- cbsg
description: Spectral linting rules defining API design standards and conventions for Corporate Bullshit Generator API.
layout: rules
name: Corporate Bullshit Generator API API Rules
provider_name: Corporate Bullshit Generator API
provider_slug: corporate-bullshit-generator-api
rule_count: 10
rules:
- description: API info object should include contact information.
  given: $.info
  name: cbsg-info-contact
  severity: warn
- description: API should declare a license.
  given: $.info
  name: cbsg-info-license
  severity: warn
- description: Servers must use HTTPS.
  given: $.servers[*].url
  name: cbsg-server-https
  severity: error
- description: Server URL must reference the public CBSG host.
  given: $.servers[*].url
  name: cbsg-server-host
  severity: error
- description: API must define the root path.
  given: $.paths
  name: cbsg-root-path
  severity: error
- description: The root path must only support GET.
  given: $.paths['/']
  name: cbsg-get-only
  severity: error
- description: The API is unauthenticated; security must be empty or absent.
  given: $.paths['/'].get
  name: cbsg-no-auth
  severity: warn
- description: 200 response must return application/json.
  given: $.paths['/'].get.responses.200.content
  name: cbsg-json-response
  severity: error
- description: Response schema must include a phrase property.
  given: $.components.schemas.Phrase.properties
  name: cbsg-phrase-property
  severity: error
- description: Operation must define an operationId.
  given: $.paths.*.get
  name: cbsg-operation-id
  severity: error
rules_file: rules/corporate-bullshit-generator-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/corporate-bullshit-generator-api/refs/heads/main/rules/corporate-bullshit-generator-api-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 3
slug: corporate-bullshit-generator-api-rules
source_filename: corporate-bullshit-generator-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [\"spectral:oas\"]\ndocumentationUrl: https://corporatebs-generator.sameerkumar.website/\nrules:\n  cbsg-info-contact:\n    description: API info object should include contact information.\n    given: \"$.info\"\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  cbsg-info-license:\n    description: API should declare a license.\n    given: \"$.info\"\n    severity: warn\n    then:\n      field: license\n      function: truthy\n  cbsg-server-https:\n    description: Servers must use HTTPS.\n    given: \"$.servers[*].url\"\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  cbsg-server-host:\n    description: Server URL must reference the public CBSG host.\n    given: \"$.servers[*].url\"\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"corporatebs-generator.sameerkumar.website\"\n  cbsg-root-path:\n    description: API must define\
  \ the root path.\n    given: \"$.paths\"\n    severity: error\n    then:\n      field: /\n      function: truthy\n  cbsg-get-only:\n    description: The root path must only support GET.\n    given: \"$.paths['/']\"\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            get:\n              type: object\n          additionalProperties: false\n  cbsg-no-auth:\n    description: The API is unauthenticated; security must be empty or absent.\n    given: \"$.paths['/'].get\"\n    severity: warn\n    then:\n      field: security\n      function: falsy\n  cbsg-json-response:\n    description: 200 response must return application/json.\n    given: \"$.paths['/'].get.responses.200.content\"\n    severity: error\n    then:\n      field: application/json\n      function: truthy\n  cbsg-phrase-property:\n    description: Response schema must include a phrase property.\n    given: \"$.components.schemas.Phrase.properties\"\
  \n    severity: error\n    then:\n      field: phrase\n      function: truthy\n  cbsg-operation-id:\n    description: Operation must define an operationId.\n    given: \"$.paths.*.get\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/corporate-bullshit-generator-api/refs/heads/main/rules/corporate-bullshit-generator-api-rules.yml
tags:
- Buzzwords
- Comedy
- Corporate Jargon
- Fake Data
- Free
- Generator
- JSON
- Mock Data
- Phrases
- Public API
- REST
- Test Data
- Unauthenticated
- Spectral
- Linting
- API Governance
---
