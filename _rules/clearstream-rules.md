---
categories:
- clearstream
description: Spectral linting rules defining API design standards and conventions for Clearstream.
layout: rules
name: Clearstream API Rules
provider_name: Clearstream
provider_slug: clearstream
rule_count: 11
rules:
- description: API contact information must be present.
  given: $.info
  name: clearstream-info-contact
  severity: error
- description: API license must be declared.
  given: $.info
  name: clearstream-info-license
  severity: warn
- description: Info description should reference ISO 15022 or ISO 20022.
  given: $.info.description
  name: clearstream-info-iso-version
  severity: warn
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: clearstream-server-https
  severity: error
- description: Server URLs must point at a clearstream.com host.
  given: $.servers[*].url
  name: clearstream-server-domain
  severity: warn
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: clearstream-operation-tags
  severity: warn
- description: Every operation must include a short summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: clearstream-operation-summary
  severity: warn
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: clearstream-operation-id
  severity: error
- description: Mutating operations should declare 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: clearstream-error-responses
  severity: warn
- description: Counterparty BIC parameters should be 8 or 11 character ISO 9362 BICs.
  given: $.paths[*][*].parameters[?(@.name && @.name.match(/bic/i))].schema
  name: clearstream-bic-format
  severity: warn
- description: ISIN parameters should be 12-character ISO 6166 identifiers.
  given: $.paths[*][*].parameters[?(@.name && @.name.match(/isin/i))].schema
  name: clearstream-isin-format
  severity: warn
rules_file: rules/clearstream-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/clearstream/refs/heads/main/rules/clearstream-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 8
slug: clearstream-rules
source_filename: clearstream-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules tuned for Clearstream connectivity.\n# Clearstream's developer surface is largely message-based (SWIFT FIN/FileAct,\n# ISO 15022 MT and ISO 20022 MX), so these rules focus on the descriptive\n# OpenAPI / AsyncAPI overlays that catalogue those channels rather than a\n# public REST API.\nrules:\n  clearstream-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  clearstream-info-license:\n    description: API license must be declared.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  clearstream-info-iso-version:\n    description: Info description should reference ISO 15022 or ISO 20022.\n    severity: warn\n    given: \"$.info.description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"ISO\\\\s?(15022|20022)\"\n\n\
  \  clearstream-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  clearstream-server-domain:\n    description: Server URLs must point at a clearstream.com host.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"clearstream\\\\.com\"\n\n  clearstream-operation-tags:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  clearstream-operation-summary:\n    description: Every operation must include a short summary.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n  \
  \    function: truthy\n\n  clearstream-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  clearstream-error-responses:\n    description: Mutating operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n            - required: [\"422\"]\n\n  clearstream-bic-format:\n    description: Counterparty BIC parameters should be 8 or 11 character ISO 9362 BICs.\n    severity: warn\n    given: \"$.paths[*][*].parameters[?(@.name && @.name.match(/bic/i))].schema\"\n    then:\n      function: schema\n   \
  \   functionOptions:\n        schema:\n          type: object\n          properties:\n            pattern:\n              type: string\n              enum:\n                - \"^[A-Z0-9]{8}([A-Z0-9]{3})?$\"\n\n  clearstream-isin-format:\n    description: ISIN parameters should be 12-character ISO 6166 identifiers.\n    severity: warn\n    given: \"$.paths[*][*].parameters[?(@.name && @.name.match(/isin/i))].schema\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            pattern:\n              type: string\n              enum:\n                - \"^[A-Z]{2}[A-Z0-9]{9}\\\\d$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/clearstream/refs/heads/main/rules/clearstream-rules.yml
tags:
- Capital Markets
- Collateral Management
- Custody
- Financial Services
- ISO 15022
- ISO 20022
- Post-Trade Infrastructure
- Securities
- Settlement
- SWIFT
- Spectral
- Linting
- API Governance
---
