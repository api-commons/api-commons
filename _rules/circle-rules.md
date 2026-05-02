---
api_specs:
- filename: developer-controlled-wallets.yaml
  format: yaml
  label: Developer-Controlled Wallets
  slug: developer-controlled-wallets
  spec_type: OpenAPI
  url: https://developers.circle.com/openapi/developer-controlled-wallets.yaml
- filename: user-controlled-wallets.yaml
  format: yaml
  label: User-Controlled Wallets
  slug: user-controlled-wallets
  spec_type: OpenAPI
  url: https://developers.circle.com/openapi/user-controlled-wallets.yaml
- filename: cctp.yaml
  format: yaml
  label: Cross-Chain Transfer Protocol (CCTP)
  slug: cctp
  spec_type: OpenAPI
  url: https://developers.circle.com/openapi/cctp.yaml
- filename: gateway.yaml
  format: yaml
  label: Circle Gateway
  slug: gateway
  spec_type: OpenAPI
  url: https://developers.circle.com/openapi/gateway.yaml
- filename: smart-contract-platform.yaml
  format: yaml
  label: Smart Contract Platform
  slug: smart-contract-platform
  spec_type: OpenAPI
  url: https://developers.circle.com/openapi/smart-contract-platform.yaml
- filename: cpn-ofi.yaml
  format: yaml
  label: Circle Payments Network (CPN)
  slug: cpn
  spec_type: OpenAPI
  url: https://developers.circle.com/openapi/cpn-ofi.yaml
- filename: compliance.yaml
  format: yaml
  label: Compliance Engine
  slug: compliance-engine
  spec_type: OpenAPI
  url: https://developers.circle.com/openapi/compliance.yaml
- filename: stablefx.yaml
  format: yaml
  label: StableFX
  slug: stablefx
  spec_type: OpenAPI
  url: https://developers.circle.com/openapi/stablefx.yaml
- filename: xreserve.yaml
  format: yaml
  label: xReserve
  slug: xreserve
  spec_type: OpenAPI
  url: https://developers.circle.com/openapi/xreserve.yaml
categories:
- circle
description: Spectral linting rules defining API design standards and conventions for Circle.
layout: rules
name: Circle API Rules
provider_name: Circle
provider_slug: circle
rule_count: 9
rules:
- description: API contact information must be present.
  given: $.info
  name: circle-info-contact
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: circle-server-https
  severity: error
- description: api.circle.com servers must include /v1.
  given: $.servers[?(@.url && @.url.indexOf('api.circle.com') > -1)].url
  name: circle-server-base-path
  severity: warn
- description: A bearer-token security scheme must be defined.
  given: $.components.securitySchemes[*]
  name: circle-bearer-security
  severity: error
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: circle-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: circle-operation-tags
  severity: warn
- description: POST operations should accept an X-Idempotency-Key header.
  given: $.paths[*].post
  name: circle-idempotency-key
  severity: warn
- description: Mutating operations should declare 4xx/5xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: circle-error-responses
  severity: warn
- description: Path parameters named "id" should be UUIDs.
  given: $.paths[*].*.parameters[?(@.in == 'path' && @.name == 'id')].schema
  name: circle-uuid-identifiers
  severity: info
rules_file: rules/circle-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/circle/refs/heads/main/rules/circle-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 4
slug: circle-rules
source_filename: circle-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for Circle Web3 Services and adjacent APIs.\n# Tuned to api.circle.com conventions: HTTPS-only, /v1/w3s base path,\n# UUID identifiers, idempotency keys on POST, and bearer-token auth.\nrules:\n  circle-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  circle-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  circle-server-base-path:\n    description: api.circle.com servers must include /v1.\n    severity: warn\n    given: \"$.servers[?(@.url && @.url.indexOf('api.circle.com') > -1)].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/v1\"\n\n  circle-bearer-security:\n    description: A bearer-token security\
  \ scheme must be defined.\n    severity: error\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            type:\n              enum: [\"http\", \"apiKey\", \"oauth2\"]\n\n  circle-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  circle-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  circle-idempotency-key:\n    description: POST operations should accept an X-Idempotency-Key header.\n    severity: warn\n    given: \"$.paths[*].post\"\n    then:\n  \
  \    field: parameters\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            type: object\n            properties:\n              name:\n                enum: [\"X-Idempotency-Key\", \"idempotencyKey\"]\n\n  circle-error-responses:\n    description: Mutating operations should declare 4xx/5xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n            - required: [\"422\"]\n\n  circle-uuid-identifiers:\n    description: Path parameters named \"id\" should be UUIDs.\n    severity: info\n    given: \"$.paths[*].*.parameters[?(@.in == 'path' && @.name == 'id')].schema\"\n    then:\n      field: format\n      function: enumeration\n\
  \      functionOptions:\n        values:\n          - uuid\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/circle/refs/heads/main/rules/circle-rules.yml
tags:
- Blockchain
- Compliance
- Cross-Chain
- Currency
- Money
- Payments
- Stablecoin
- Transfers
- USDC
- Wallets
- Spectral
- Linting
- API Governance
---
