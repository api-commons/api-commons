---
api_specs:
- filename: cloudzero-api-openapi.yml
  format: yaml
  label: CloudZero API
  slug: api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cloudzero/refs/heads/main/openapi/cloudzero-api-openapi.yml
categories:
- cloudzero
description: Spectral linting rules defining API design standards and conventions for CloudZero.
layout: rules
name: CloudZero API Rules
provider_name: CloudZero
provider_slug: cloudzero
rule_count: 12
rules:
- description: API contact information must be present.
  given: $.info
  name: cloudzero-info-contact
  severity: error
- description: API license must be declared.
  given: $.info
  name: cloudzero-info-license
  severity: warn
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: cloudzero-server-https
  severity: error
- description: Server URL must reference api.cloudzero.com.
  given: $.servers[*].url
  name: cloudzero-server-host
  severity: warn
- description: An apiKey security scheme must be defined.
  given: $.components.securitySchemes
  name: cloudzero-api-key-auth
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudzero-operation-tags
  severity: warn
- description: Every operation must include a short summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudzero-operation-summary
  severity: warn
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudzero-operation-id
  severity: error
- description: Mutating operations should declare 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: cloudzero-error-responses
  severity: warn
- description: List endpoints should accept page and page_size query parameters.
  given: $.paths[?(@property.match(/insights$|budgets$|costs$|dimensions$/))].get.parameters[*].name
  name: cloudzero-pagination-page
  severity: info
- description: Date parameters and properties should use ISO 8601 (date or date-time).
  given: $..[?(@property === 'start_date' || @property === 'end_date')].schema
  name: cloudzero-iso-date
  severity: warn
- description: Currency fields should use ISO 4217 codes.
  given: $..[?(@property === 'currency')].schema
  name: cloudzero-currency-iso
  severity: warn
rules_file: rules/cloudzero-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cloudzero/refs/heads/main/rules/cloudzero-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 7
slug: cloudzero-rules
source_filename: cloudzero-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules tuned for the CloudZero V2 REST API.\n# Validates conventions described at\n# https://docs.cloudzero.com/reference/introduction\n# - HTTPS only, API key authentication, JSON request/response,\n#   page/page_size pagination, and resource-oriented v1/v2 paths.\nrules:\n  cloudzero-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  cloudzero-info-license:\n    description: API license must be declared.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  cloudzero-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  cloudzero-server-host:\n    description: Server URL must reference api.cloudzero.com.\n\
  \    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"api\\\\.cloudzero\\\\.com\"\n\n  cloudzero-api-key-auth:\n    description: An apiKey security scheme must be defined.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  cloudzero-operation-tags:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  cloudzero-operation-summary:\n    description: Every operation must include a short summary.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  cloudzero-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity:\
  \ error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  cloudzero-error-responses:\n    description: Mutating operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n            - required: [\"422\"]\n\n  cloudzero-pagination-page:\n    description: List endpoints should accept page and page_size query parameters.\n    severity: info\n    given: \"$.paths[?(@property.match(/insights$|budgets$|costs$|dimensions$/))].get.parameters[*].name\"\n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - page\n          - page_size\n          - filter\n          -\
  \ dimensions\n          - metrics\n          - start_date\n          - end_date\n\n  cloudzero-iso-date:\n    description: Date parameters and properties should use ISO 8601 (date or date-time).\n    severity: warn\n    given: \"$..[?(@property === 'start_date' || @property === 'end_date')].schema\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            format:\n              type: string\n              enum:\n                - date\n                - date-time\n\n  cloudzero-currency-iso:\n    description: Currency fields should use ISO 4217 codes.\n    severity: warn\n    given: \"$..[?(@property === 'currency')].schema\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            pattern:\n              type: string\n              enum:\n                - \"^[A-Z]{3}$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cloudzero/refs/heads/main/rules/cloudzero-rules.yml
tags:
- Budgets
- Cloud Cost Management
- Cost Allocation
- Cost Optimization
- FinOps
- Telemetry
- Unit Economics
- Spectral
- Linting
- API Governance
---
