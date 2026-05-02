---
categories:
- citizens
description: Spectral linting rules defining API design standards and conventions for Citizens Financial Group.
layout: rules
name: Citizens Financial Group API Rules
provider_name: Citizens Financial Group
provider_slug: citizens-financial-group
rule_count: 6
rules:
- description: All Citizens API servers MUST use HTTPS.
  given: $.servers[*].url
  name: citizens-https-only
  severity: error
- description: Citizens APIs MUST declare an OAuth 2.0 security scheme for consented data access.
  given: $.components.securitySchemes
  name: citizens-oauth-required
  severity: error
- description: Operations MUST have an operationId.
  given: $.paths[*][get,post,put,delete,patch]
  name: citizens-operation-id
  severity: error
- description: Operations MUST be tagged for product domain grouping.
  given: $.paths[*][get,post,put,delete,patch].tags
  name: citizens-tag-required
  severity: warn
- description: API info MUST contain a contact for security disclosures.
  given: $.info
  name: citizens-info-contact
  severity: warn
- description: Open banking endpoints SHOULD align with Financial Data Exchange (FDX) field names.
  given: $.components.schemas
  name: citizens-fdx-alignment
  severity: warn
rules_file: rules/citizens-financial-group-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/citizens-financial-group/refs/heads/main/rules/citizens-financial-group-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 3
slug: citizens-financial-group-rules
source_filename: citizens-financial-group-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  citizens-https-only:\n    description: All Citizens API servers MUST use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  citizens-oauth-required:\n    description: Citizens APIs MUST declare an OAuth 2.0 security scheme for consented data access.\n    severity: error\n    given: $.components.securitySchemes\n    then:\n      function: truthy\n  citizens-operation-id:\n    description: Operations MUST have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  citizens-tag-required:\n    description: Operations MUST be tagged for product domain grouping.\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].tags\n    then:\n      function: truthy\n  citizens-info-contact:\n    description: API info MUST contain a contact for security\
  \ disclosures.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n  citizens-fdx-alignment:\n    description: Open banking endpoints SHOULD align with Financial Data Exchange (FDX) field names.\n    severity: warn\n    given: $.components.schemas\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/citizens-financial-group/refs/heads/main/rules/citizens-financial-group-rules.yml
tags:
- Banking
- Buy Now Pay Later
- Financial Services
- FDX
- Locator
- Open Banking
- Payments
- Spectral
- Linting
- API Governance
---
