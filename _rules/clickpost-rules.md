---
categories:
- clickpost
description: Spectral linting rules defining API design standards and conventions for ClickPost.
layout: rules
name: ClickPost API Rules
provider_name: ClickPost
provider_slug: clickpost
rule_count: 8
rules:
- description: API contact information must be present.
  given: $.info
  name: clickpost-info-contact
  severity: error
- description: API license must be declared.
  given: $.info
  name: clickpost-info-license
  severity: warn
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: clickpost-server-https
  severity: error
- description: A security scheme (apiKey for token authentication) must be declared.
  given: $.components.securitySchemes
  name: clickpost-auth-required
  severity: error
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: clickpost-operation-id
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: clickpost-operation-tags
  severity: warn
- description: Every operation must include a short summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: clickpost-operation-summary
  severity: warn
- description: Mutating operations should declare 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: clickpost-error-responses
  severity: warn
rules_file: rules/clickpost-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/clickpost/refs/heads/main/rules/clickpost-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 4
slug: clickpost-rules
source_filename: clickpost-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for ClickPost APIs.\nrules:\n  clickpost-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  clickpost-info-license:\n    description: API license must be declared.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  clickpost-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  clickpost-auth-required:\n    description: A security scheme (apiKey for token authentication) must be declared.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  clickpost-operation-id:\n    description: Every operation must declare a unique operationId.\n\
  \    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  clickpost-operation-tags:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  clickpost-operation-summary:\n    description: Every operation must include a short summary.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  clickpost-error-responses:\n    description: Mutating operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required:\
  \ [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/clickpost/refs/heads/main/rules/clickpost-rules.yml
tags:
- Carriers
- Delivery
- E-Commerce Logistics
- Logistics
- Returns
- Shipping
- Supply Chain
- Tracking
- Spectral
- Linting
- API Governance
---
