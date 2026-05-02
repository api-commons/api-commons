---
categories:
- citi
description: Spectral linting rules defining API design standards and conventions for Citigroup.
layout: rules
name: Citigroup API Rules
provider_name: Citigroup
provider_slug: citigroup
rule_count: 6
rules:
- description: All Citi API servers MUST use HTTPS.
  given: $.servers[*].url
  name: citi-https-only
  severity: error
- description: Citi APIs MUST declare OAuth 2.0 security schemes.
  given: $.components.securitySchemes
  name: citi-oauth-required
  severity: error
- description: Operations MUST have an operationId.
  given: $.paths[*][get,post,put,delete,patch]
  name: citi-operation-id
  severity: error
- description: Operations MUST be tagged for product domain grouping.
  given: $.paths[*][get,post,put,delete,patch].tags
  name: citi-tag-required
  severity: warn
- description: Operations MUST have a summary.
  given: $.paths[*][get,post,put,delete,patch]
  name: citi-summary-required
  severity: warn
- description: API info MUST contain a contact for security disclosures.
  given: $.info
  name: citi-info-contact
  severity: warn
rules_file: rules/citigroup-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/citigroup/refs/heads/main/rules/citigroup-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 3
slug: citigroup-rules
source_filename: citigroup-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  citi-https-only:\n    description: All Citi API servers MUST use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n  citi-oauth-required:\n    description: Citi APIs MUST declare OAuth 2.0 security schemes.\n    severity: error\n    given: $.components.securitySchemes\n    then:\n      function: truthy\n  citi-operation-id:\n    description: Operations MUST have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n  citi-tag-required:\n    description: Operations MUST be tagged for product domain grouping.\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].tags\n    then:\n      function: truthy\n  citi-summary-required:\n    description: Operations MUST have a summary.\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch]\n\
  \    then:\n      field: summary\n      function: truthy\n  citi-info-contact:\n    description: API info MUST contain a contact for security disclosures.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/citigroup/refs/heads/main/rules/citigroup-rules.yml
tags:
- Banking
- Financial Services
- FX
- Open Banking
- Payments
- Treasury
- Spectral
- Linting
- API Governance
---
