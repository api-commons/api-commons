---
categories:
- clerk
description: Spectral linting rules defining API design standards and conventions for Clerk.io.
layout: rules
name: Clerk.io API Rules
provider_name: Clerk.io
provider_slug: clerk-io
rule_count: 8
rules:
- description: API contact information must be present.
  given: $.info
  name: clerk-io-info-contact
  severity: error
- description: API license must be declared.
  given: $.info
  name: clerk-io-info-license
  severity: warn
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: clerk-io-server-https
  severity: error
- description: A security scheme (apiKey for public/private keys) must be declared.
  given: $.components.securitySchemes
  name: clerk-io-auth-required
  severity: error
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: clerk-io-operation-id
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: clerk-io-operation-tags
  severity: warn
- description: Every operation must include a short summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: clerk-io-operation-summary
  severity: warn
- description: Mutating operations should declare 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: clerk-io-error-responses
  severity: warn
rules_file: rules/clerk-io-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/clerk-io/refs/heads/main/rules/clerk-io-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 4
slug: clerk-io-rules
source_filename: clerk-io-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for Clerk.io APIs.\nrules:\n  clerk-io-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  clerk-io-info-license:\n    description: API license must be declared.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  clerk-io-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  clerk-io-auth-required:\n    description: A security scheme (apiKey for public/private keys) must be declared.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  clerk-io-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity:\
  \ error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  clerk-io-operation-tags:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  clerk-io-operation-summary:\n    description: Every operation must include a short summary.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  clerk-io-error-responses:\n    description: Mutating operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n\
  \            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/clerk-io/refs/heads/main/rules/clerk-io-rules.yml
tags:
- AI
- Commerce
- E-Commerce
- Email Marketing
- Personalization
- Recommendations
- Search
- Spectral
- Linting
- API Governance
---
