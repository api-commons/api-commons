---
api_specs:
- filename: cryptoquant-openapi.yml
  format: yaml
  label: CryptoQuant API
  slug: cryptoquant-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cryptoquant/refs/heads/main/openapi/cryptoquant-openapi.yml
categories:
- cryptoquant
description: Spectral linting rules defining API design standards and conventions for CryptoQuant.
layout: rules
name: CryptoQuant API Rules
provider_name: CryptoQuant
provider_slug: cryptoquant
rule_count: 6
rules:
- description: CryptoQuant servers must use HTTPS.
  given: $.servers[*].url
  name: cryptoquant-server-https
  severity: error
- description: CryptoQuant base URL should include /v{n} path version.
  given: $.servers[*].url
  name: cryptoquant-versioned-path
  severity: warn
- description: CryptoQuant API must declare bearer auth scheme.
  given: $.components.securitySchemes
  name: cryptoquant-bearer-auth
  severity: error
- description: Time-series operations should accept a window parameter.
  given: $.paths[*][get].parameters[?(@.name=='window')]
  name: cryptoquant-window-param
  severity: warn
- description: Operations must declare a tag.
  given: $.paths[*][get,post,put,delete]
  name: cryptoquant-tag-required
  severity: warn
- description: Operation IDs should be camelCase.
  given: $.paths[*][get,post,put,delete].operationId
  name: cryptoquant-operation-id-camel
  severity: warn
rules_file: rules/cryptoquant-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cryptoquant/refs/heads/main/rules/cryptoquant-rules.yml
severity_counts:
  error: 2
  hint: 0
  info: 0
  warn: 4
slug: cryptoquant-rules
source_filename: cryptoquant-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [[spectral:oas, all]]\nrules:\n  cryptoquant-server-https:\n    description: CryptoQuant servers must use HTTPS.\n    given: $.servers[*].url\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  cryptoquant-versioned-path:\n    description: CryptoQuant base URL should include /v{n} path version.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: '/v[0-9]+'\n  cryptoquant-bearer-auth:\n    description: CryptoQuant API must declare bearer auth scheme.\n    given: $.components.securitySchemes\n    severity: error\n    then:\n      function: truthy\n  cryptoquant-window-param:\n    description: Time-series operations should accept a window parameter.\n    given: $.paths[*][get].parameters[?(@.name=='window')]\n    severity: warn\n    then:\n      field: schema.enum\n      function: truthy\n  cryptoquant-tag-required:\n    description: Operations\
  \ must declare a tag.\n    given: $.paths[*][get,post,put,delete]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n  cryptoquant-operation-id-camel:\n    description: Operation IDs should be camelCase.\n    given: $.paths[*][get,post,put,delete].operationId\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]+$'\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cryptoquant/refs/heads/main/rules/cryptoquant-rules.yml
tags:
- Blockchain
- Cryptocurrency
- On-Chain Analytics
- Market Data
- Derivatives
- Spectral
- Linting
- API Governance
---
