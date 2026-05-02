---
api_specs:
- filename: apigen-apigen-openapi.yml
  format: yaml
  label: APIGen
  slug: apigen
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apigen/refs/heads/main/openapi/apigen-apigen-openapi.yml
categories:
- info
- operation
- response
- servers
description: Spectral linting rules defining API design standards and conventions for APIGen.
layout: rules
name: APIGen API Rules
provider_name: APIGen
provider_slug: apigen
rule_count: 7
rules:
- description: API title must start with 'APIGen'.
  given: $.info
  name: info-title-prefix
  severity: warn
- description: API must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*]
  name: servers-https
  severity: error
- description: Operation summaries must start with 'APIGen'.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have tags.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every operation must have a 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
rules_file: rules/apigen-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apigen/refs/heads/main/rules/apigen-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 3
slug: apigen-spectral-rules
source_filename: apigen-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  info-title-prefix:\n    description: API title must start with 'APIGen'.\n    severity: warn\n    given: '$.info'\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: '^APIGen'\n\n  info-description-required:\n    description: API must have a description.\n    severity: error\n    given: '$.info'\n    then:\n      field: description\n      function: truthy\n\n  servers-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: '$.servers[*]'\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: '^https://'\n\n  operation-summary-prefix:\n    description: Operation summaries must start with 'APIGen'.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: '^APIGen'\n\n  operation-id-required:\n    description: Every operation\
  \ must have an operationId.\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have tags.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: tags\n      function: truthy\n\n  response-success-required:\n    description: Every operation must have a 2xx response.\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].responses'\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apigen/refs/heads/main/rules/apigen-spectral-rules.yml
tags:
- Code
- Documentation
- Generation
- Open Source
- PHP
- Spectral
- Linting
- API Governance
---
