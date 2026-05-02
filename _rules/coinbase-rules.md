---
api_specs:
- filename: coinbase-advanced-trade-openapi.yml
  format: yaml
  label: Coinbase Advanced Trade API
  slug: advanced-trade-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/coinbase/refs/heads/main/openapi/coinbase-advanced-trade-openapi.yml
- filename: coinbase-exchange-openapi.yml
  format: yaml
  label: Coinbase Exchange API
  slug: exchange-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/coinbase/refs/heads/main/openapi/coinbase-exchange-openapi.yml
- filename: coinbase-prime-openapi.yml
  format: yaml
  label: Coinbase Prime API
  slug: prime-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/coinbase/refs/heads/main/openapi/coinbase-prime-openapi.yml
- filename: coinbase-onramp-openapi.yml
  format: yaml
  label: Coinbase Onramp API
  slug: onramp-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/coinbase/refs/heads/main/openapi/coinbase-onramp-openapi.yml
- filename: coinbase-commerce-openapi.yml
  format: yaml
  label: Coinbase Commerce API
  slug: commerce-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/coinbase/refs/heads/main/openapi/coinbase-commerce-openapi.yml
categories:
- coinbase
description: Spectral linting rules defining API design standards and conventions for Coinbase.
layout: rules
name: Coinbase API Rules
provider_name: Coinbase
provider_slug: coinbase
rule_count: 12
rules:
- description: API contact information must be present.
  given: $.info
  name: coinbase-info-contact
  severity: error
- description: termsOfService must reference coinbase.com.
  given: $.info.termsOfService
  name: coinbase-terms-of-service
  severity: warn
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: coinbase-server-https
  severity: error
- description: Server URLs must point to a known Coinbase host.
  given: $.servers[*].url
  name: coinbase-server-host
  severity: warn
- description: Authenticated APIs must declare a security scheme.
  given: $.components.securitySchemes
  name: coinbase-security-defined
  severity: error
- description: Security scheme should be apiKey, http, or oauth2.
  given: $.components.securitySchemes[*]
  name: coinbase-security-scheme-shape
  severity: error
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: coinbase-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: coinbase-operation-tags
  severity: warn
- description: Operations should declare a summary for documentation.
  given: $.paths[*][get,post,put,patch,delete]
  name: coinbase-operation-summary
  severity: warn
- description: Mutating operations should declare 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: coinbase-error-responses
  severity: warn
- description: Paths should be served under a versioned prefix (v1, v2, v3).
  given: $.servers[*].url
  name: coinbase-versioned-path
  severity: info
- description: List operations should expose cursor-based pagination.
  given: $.paths[*].get.parameters[?(@.name == 'cursor' || @.name == 'limit')]
  name: coinbase-pagination-cursor
  severity: info
rules_file: rules/coinbase-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/coinbase/refs/heads/main/rules/coinbase-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 2
  warn: 5
slug: coinbase-rules
source_filename: coinbase-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for the Coinbase Developer Platform APIs\n# (Advanced Trade, Exchange, Prime, Onramp, Commerce). Tuned to the\n# api.coinbase.com / api.exchange.coinbase.com / api.prime.coinbase.com\n# / api.commerce.coinbase.com host conventions, HMAC-SHA256 and JWT\n# auth schemes, versioned URI paths, and standardized error envelopes.\nrules:\n  coinbase-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  coinbase-terms-of-service:\n    description: termsOfService must reference coinbase.com.\n    severity: warn\n    given: \"$.info.termsOfService\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"coinbase.com\"\n\n  coinbase-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n\
  \      functionOptions:\n        match: \"^https://\"\n\n  coinbase-server-host:\n    description: Server URLs must point to a known Coinbase host.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(api\\\\.coinbase\\\\.com|api\\\\.exchange\\\\.coinbase\\\\.com|api\\\\.prime\\\\.coinbase\\\\.com|api\\\\.commerce\\\\.coinbase\\\\.com|api\\\\.developer\\\\.coinbase\\\\.com)\"\n\n  coinbase-security-defined:\n    description: Authenticated APIs must declare a security scheme.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  coinbase-security-scheme-shape:\n    description: Security scheme should be apiKey, http, or oauth2.\n    severity: error\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            type:\n              enum: [\"\
  apiKey\", \"http\", \"oauth2\"]\n\n  coinbase-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  coinbase-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  coinbase-operation-summary:\n    description: Operations should declare a summary for documentation.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  coinbase-error-responses:\n    description: Mutating operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n\
  \      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n            - required: [\"429\"]\n\n  coinbase-versioned-path:\n    description: Paths should be served under a versioned prefix (v1, v2, v3).\n    severity: info\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/v[0-9]+|/api/v[0-9]+\"\n\n  coinbase-pagination-cursor:\n    description: List operations should expose cursor-based pagination.\n    severity: info\n    given: \"$.paths[*].get.parameters[?(@.name == 'cursor' || @.name == 'limit')]\"\n    then:\n      field: name\n      function: enumeration\n      functionOptions:\n        values:\n          - cursor\n          - limit\n          - starting_after\n          - ending_before\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/coinbase/refs/heads/main/rules/coinbase-rules.yml
tags:
- Blockchain
- Cryptocurrency
- Custody
- Exchange
- Onramp
- Payments
- Trading
- Wallet
- Web3
- Spectral
- Linting
- API Governance
---
