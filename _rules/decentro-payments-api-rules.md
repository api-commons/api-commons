---
api_specs:
- filename: decentro-kyc-api-openapi.yml
  format: yaml
  label: Decentro KYC & Onboarding API
  slug: kyc-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/decentro/refs/heads/main/openapi/decentro-kyc-api-openapi.yml
- filename: decentro-payments-api-openapi.yml
  format: yaml
  label: Decentro Payments API
  slug: payments-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/decentro/refs/heads/main/openapi/decentro-payments-api-openapi.yml
- filename: decentro-virtual-accounts-api-openapi.yml
  format: yaml
  label: Decentro Virtual Accounts API
  slug: virtual-accounts-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/decentro/refs/heads/main/openapi/decentro-virtual-accounts-api-openapi.yml
- filename: decentro-ledger-api-openapi.yml
  format: yaml
  label: Decentro Ledger API
  slug: ledger-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/decentro/refs/heads/main/openapi/decentro-ledger-api-openapi.yml
categories:
- decentro
description: Spectral linting rules defining API design standards and conventions for Decentro.
layout: rules
name: Decentro API Rules
provider_name: Decentro
provider_slug: decentro
rule_count: 5
rules:
- description: API info should declare a Decentro contact.
  given: $.info
  name: decentro-info-contact
  severity: warn
- description: Servers should reference decentro.tech.
  given: $.servers[*].url
  name: decentro-base-url
  severity: warn
- description: API should declare client_secret API key authentication.
  given: $.components.securitySchemes
  name: decentro-api-key-security
  severity: error
- description: API resources should be versioned under /v2.
  given: $.paths
  name: decentro-v2-paths
  severity: warn
- description: Operations should be tagged Collections, Payouts, Mandates, or Settlements.
  given: $.paths[*][*]
  name: decentro-operation-tags
  severity: warn
rules_file: rules/decentro-payments-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/decentro/refs/heads/main/rules/decentro-payments-api-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 4
slug: decentro-payments-api-rules
source_filename: decentro-payments-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  decentro-info-contact:\n    description: API info should declare a Decentro contact.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  decentro-base-url:\n    description: Servers should reference decentro.tech.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"decentro\\\\.tech\"\n  decentro-api-key-security:\n    description: API should declare client_secret API key authentication.\n    given: $.components.securitySchemes\n    severity: error\n    then:\n      field: apiKey\n      function: truthy\n  decentro-v2-paths:\n    description: API resources should be versioned under /v2.\n    given: $.paths\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/v2/\"\n  decentro-operation-tags:\n    description: Operations should be tagged Collections, Payouts, Mandates, or\
  \ Settlements.\n    given: $.paths[*][*]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/decentro/refs/heads/main/rules/decentro-payments-api-rules.yml
tags:
- Banking
- Banking-as-a-Service
- FinTech
- India
- KYC
- Ledger
- Payments
- UPI
- Virtual Accounts
- Spectral
- Linting
- API Governance
---
