---
api_specs:
- filename: coingecko-crypto-market-data-api-openapi.yml
  format: yaml
  label: CoinGecko Crypto Market Data API
  slug: crypto-market-data-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/coingecko/refs/heads/main/openapi/coingecko-crypto-market-data-api-openapi.yml
- filename: coingecko-pro-api-openapi.yml
  format: yaml
  label: CoinGecko Pro API
  slug: pro-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/coingecko/refs/heads/main/openapi/coingecko-pro-api-openapi.yml
- filename: coingecko-onchain-dex-api-openapi.yml
  format: yaml
  label: CoinGecko Onchain DEX API
  slug: onchain-dex-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/coingecko/refs/heads/main/openapi/coingecko-onchain-dex-api-openapi.yml
categories:
- coingecko
description: Spectral linting rules defining API design standards and conventions for CoinGecko.
layout: rules
name: CoinGecko API Rules
provider_name: CoinGecko
provider_slug: coingecko
rule_count: 10
rules:
- description: API contact information must be present.
  given: $.info
  name: coingecko-info-contact
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: coingecko-server-https
  severity: error
- description: Server URLs must reference a CoinGecko host.
  given: $.servers[*].url
  name: coingecko-server-host
  severity: warn
- description: Server URLs should expose /api/v3 versioning.
  given: $.servers[*].url
  name: coingecko-versioned-path
  severity: info
- description: Authenticated APIs should use x-cg-demo-api-key or x-cg-pro-api-key.
  given: $.components.securitySchemes[*]
  name: coingecko-api-key-header
  severity: warn
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: coingecko-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: coingecko-operation-tags
  severity: warn
- description: Operations should declare a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: coingecko-operation-summary
  severity: warn
- description: GET operations should declare 401 and 429 error responses.
  given: $.paths[*].get.responses
  name: coingecko-error-responses
  severity: warn
- description: Pricing endpoints should accept vs_currency or vs_currencies.
  given: $.paths[*].get.parameters[?(@.in == 'query')]
  name: coingecko-currency-param
  severity: info
rules_file: rules/coingecko-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/coingecko/refs/heads/main/rules/coingecko-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 2
  warn: 5
slug: coingecko-rules
source_filename: coingecko-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for CoinGecko APIs (Crypto Market Data, Pro,\n# Onchain DEX). Tuned to api.coingecko.com / pro-api.coingecko.com host\n# conventions, x-cg-demo-api-key / x-cg-pro-api-key auth headers, and\n# the /api/v3 versioned URI prefix.\nrules:\n  coingecko-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  coingecko-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  coingecko-server-host:\n    description: Server URLs must reference a CoinGecko host.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(api\\\\.coingecko\\\\.com|pro-api\\\\.coingecko\\\\.com)\"\n\n  coingecko-versioned-path:\n\
  \    description: Server URLs should expose /api/v3 versioning.\n    severity: info\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/api/v3\"\n\n  coingecko-api-key-header:\n    description: Authenticated APIs should use x-cg-demo-api-key or x-cg-pro-api-key.\n    severity: warn\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            type:\n              const: apiKey\n            in:\n              const: header\n            name:\n              enum:\n                - x-cg-demo-api-key\n                - x-cg-pro-api-key\n\n  coingecko-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  coingecko-operation-tags:\n    description:\
  \ Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  coingecko-operation-summary:\n    description: Operations should declare a summary.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  coingecko-error-responses:\n    description: GET operations should declare 401 and 429 error responses.\n    severity: warn\n    given: \"$.paths[*].get.responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"401\"]\n            - required: [\"429\"]\n\n  coingecko-currency-param:\n    description: Pricing endpoints should accept vs_currency or vs_currencies.\n    severity: info\n    given: \"$.paths[*].get.parameters[?(@.in\
  \ == 'query')]\"\n    then:\n      field: name\n      function: enumeration\n      functionOptions:\n        values:\n          - vs_currency\n          - vs_currencies\n          - ids\n          - id\n          - contract_address\n          - addresses\n          - days\n          - precision\n          - per_page\n          - page\n          - order\n          - category\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/coingecko/refs/heads/main/rules/coingecko-rules.yml
tags:
- Aggregator
- Blockchain
- Cryptocurrency
- Decentralized Exchanges
- DeFi
- DEX
- Exchanges
- Liquidity Pools
- Market Data
- NFTs
- Onchain Data
- Prices
- Spectral
- Linting
- API Governance
---
