---
categories:
- cloudability
description: Spectral linting rules defining API design standards and conventions for Cloudability.
layout: rules
name: Cloudability API Rules
provider_name: Cloudability
provider_slug: cloudability
rule_count: 11
rules:
- description: API contact information must be present.
  given: $.info
  name: cloudability-info-contact
  severity: error
- description: API license must be declared.
  given: $.info
  name: cloudability-info-license
  severity: warn
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: cloudability-server-https
  severity: error
- description: API server URLs must include /v3.
  given: $.servers[?(@.url && @.url.indexOf('cloudability.com') > -1)].url
  name: cloudability-server-versioned
  severity: warn
- description: A basic-auth security scheme (API token) must be defined.
  given: $.components.securitySchemes
  name: cloudability-basic-auth
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudability-operation-tags
  severity: warn
- description: Every operation must include a short summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudability-operation-summary
  severity: warn
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudability-operation-id
  severity: error
- description: Mutating operations should declare 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: cloudability-error-responses
  severity: warn
- description: List endpoints should accept limit and offset query params.
  given: $.paths[?(@property.match(/list$|reports$|recommendations$|anomalies$|business-mappings$/))].get.parameters[*].name
  name: cloudability-pagination-limit-offset
  severity: info
- description: Currency parameters and properties should use ISO 4217 codes.
  given: $..[?(@property === 'currency')].schema
  name: cloudability-currency-iso
  severity: warn
rules_file: rules/cloudability-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cloudability/refs/heads/main/rules/cloudability-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 6
slug: cloudability-rules
source_filename: cloudability-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules tuned for the Cloudability v3 REST API.\n# Validates conventions described at\n# https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas\n# — HTTPS only, HTTP basic auth with an API token, JSON responses,\n# limit/offset pagination, and resource-oriented v3 paths.\nrules:\n  cloudability-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  cloudability-info-license:\n    description: API license must be declared.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  cloudability-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  cloudability-server-versioned:\n    description:\
  \ API server URLs must include /v3.\n    severity: warn\n    given: \"$.servers[?(@.url && @.url.indexOf('cloudability.com') > -1)].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/v3(/|$)\"\n\n  cloudability-basic-auth:\n    description: A basic-auth security scheme (API token) must be defined.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  cloudability-operation-tags:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  cloudability-operation-summary:\n    description: Every operation must include a short summary.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  cloudability-operation-id:\n\
  \    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  cloudability-error-responses:\n    description: Mutating operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n            - required: [\"422\"]\n\n  cloudability-pagination-limit-offset:\n    description: List endpoints should accept limit and offset query params.\n    severity: info\n    given: \"$.paths[?(@property.match(/list$|reports$|recommendations$|anomalies$|business-mappings$/))].get.parameters[*].name\"\n    then:\n      function: enumeration\n\
  \      functionOptions:\n        values:\n          - limit\n          - offset\n          - sort\n          - filters\n          - dimensions\n          - metrics\n          - start_date\n          - end_date\n\n  cloudability-currency-iso:\n    description: Currency parameters and properties should use ISO 4217 codes.\n    severity: warn\n    given: \"$..[?(@property === 'currency')].schema\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            pattern:\n              type: string\n              enum:\n                - \"^[A-Z]{3}$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cloudability/refs/heads/main/rules/cloudability-rules.yml
tags:
- Cloud Cost Management
- Cost Optimization
- FinOps
- Multi-Cloud
- Recommendations
- Reporting
- Spectral
- Linting
- API Governance
---
