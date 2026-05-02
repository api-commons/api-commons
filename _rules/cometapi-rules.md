---
api_specs:
- filename: cometapi-unified-api-openapi.yml
  format: yaml
  label: CometAPI Unified API
  slug: cometapi-unified-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cometapi/refs/heads/main/openapi/cometapi-unified-api-openapi.yml
categories:
- cometapi
description: Spectral linting rules defining API design standards and conventions for CometAPI.
layout: rules
name: CometAPI API Rules
provider_name: CometAPI
provider_slug: cometapi
rule_count: 9
rules:
- description: API info must include a contact block.
  given: $.info
  name: cometapi-info-contact
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: cometapi-server-https
  severity: error
- description: Public server URL should point to api.cometapi.com.
  given: $.servers[*].url
  name: cometapi-server-host
  severity: warn
- description: Server URL should include /v1 to match OpenAI compatibility.
  given: $.servers[*].url
  name: cometapi-versioned-base-path
  severity: info
- description: API must define a bearer-token security scheme.
  given: $.components.securitySchemes[*]
  name: cometapi-bearer-security
  severity: error
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cometapi-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cometapi-operation-tags
  severity: warn
- description: Mutating operations should declare 401 and 429 error responses.
  given: $.paths[*][post].responses
  name: cometapi-error-responses
  severity: warn
- description: Generative endpoints must accept a `model` request field for routing.
  given: $.paths[*][post].requestBody.content['application/json'].schema.properties
  name: cometapi-model-field
  severity: info
rules_file: rules/cometapi-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cometapi/refs/heads/main/rules/cometapi-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 2
  warn: 3
slug: cometapi-rules
source_filename: cometapi-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for CometAPI.\n# Tuned to api.cometapi.com/v1 conventions: OpenAI-compatible endpoints,\n# bearer-token auth, and a `model` routing field on every generative call.\nrules:\n  cometapi-info-contact:\n    description: API info must include a contact block.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  cometapi-server-https:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  cometapi-server-host:\n    description: Public server URL should point to api.cometapi.com.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"api.cometapi.com\"\n\n  cometapi-versioned-base-path:\n    description: Server URL should include /v1 to match OpenAI compatibility.\n\
  \    severity: info\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/v1\"\n\n  cometapi-bearer-security:\n    description: API must define a bearer-token security scheme.\n    severity: error\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            type:\n              enum: [\"http\"]\n            scheme:\n              enum: [\"bearer\"]\n\n  cometapi-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  cometapi-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n\
  \        schema:\n          type: array\n          minItems: 1\n\n  cometapi-error-responses:\n    description: Mutating operations should declare 401 and 429 error responses.\n    severity: warn\n    given: \"$.paths[*][post].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"401\"]\n            - required: [\"429\"]\n\n  cometapi-model-field:\n    description: Generative endpoints must accept a `model` request field for routing.\n    severity: info\n    given: \"$.paths[*][post].requestBody.content['application/json'].schema.properties\"\n    then:\n      field: model\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cometapi/refs/heads/main/rules/cometapi-rules.yml
tags:
- AI
- Aggregator
- Audio
- Chat
- Embeddings
- Generative AI
- Images
- LLM
- Multi-Model
- OpenAI-Compatible
- Video
- Spectral
- Linting
- API Governance
---
