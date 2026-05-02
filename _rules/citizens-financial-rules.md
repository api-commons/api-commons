---
api_specs:
- filename: citizens-bank-accounts-api-openapi.yml
  format: yaml
  label: Citizens Bank Accounts API
  slug: accounts-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/citizens-financial/refs/heads/main/openapi/citizens-bank-accounts-api-openapi.yml
- filename: citizens-bank-atm-locator-api-openapi.yml
  format: yaml
  label: Citizens Bank ATM Locator API
  slug: atm-locator-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/citizens-financial/refs/heads/main/openapi/citizens-bank-atm-locator-api-openapi.yml
categories:
- citizens
description: Spectral linting rules defining API design standards and conventions for Citizens Financial.
layout: rules
name: Citizens Financial API Rules
provider_name: Citizens Financial
provider_slug: citizens-financial
rule_count: 6
rules:
- description: API info MUST contain a contact email or URL.
  given: $.info
  name: citizens-info-contact
  severity: warn
- description: All Citizens Financial API servers MUST use HTTPS.
  given: $.servers[*].url
  name: citizens-https-only
  severity: error
- description: Operations MUST have an operationId.
  given: $.paths[*][get,post,put,delete,patch]
  name: citizens-operation-id
  severity: error
- description: Operations MUST be tagged for product domain grouping.
  given: $.paths[*][get,post,put,delete,patch].tags
  name: citizens-tag-required
  severity: warn
- description: API MUST define OAuth 2.0 or other security schemes.
  given: $.components.securitySchemes
  name: citizens-security-required
  severity: error
- description: API MUST declare at least one server URL.
  given: $.servers
  name: citizens-server-url
  severity: error
rules_file: rules/citizens-financial-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/citizens-financial/refs/heads/main/rules/citizens-financial-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 2
slug: citizens-financial-rules
source_filename: citizens-financial-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  citizens-info-contact:\n    description: API info MUST contain a contact email or URL.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  citizens-https-only:\n    description: All Citizens Financial API servers MUST use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  citizens-operation-id:\n    description: Operations MUST have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  citizens-tag-required:\n    description: Operations MUST be tagged for product domain grouping.\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].tags\n    then:\n      function: truthy\n  citizens-security-required:\n    description: API MUST define OAuth 2.0 or other security schemes.\n    severity:\
  \ error\n    given: $.components.securitySchemes\n    then:\n      function: truthy\n  citizens-server-url:\n    description: API MUST declare at least one server URL.\n    severity: error\n    given: $.servers\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/citizens-financial/refs/heads/main/rules/citizens-financial-rules.yml
tags:
- Accounts
- ATMs
- Banking
- Open Banking
- Payments
- Point of Sale
- Transactions
- Spectral
- Linting
- API Governance
---
