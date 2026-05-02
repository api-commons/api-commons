---
api_specs:
- filename: completedns-v2-openapi.yml
  format: yaml
  label: CompleteDNS API v2
  slug: dns-history-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/completedns/refs/heads/main/openapi/completedns-v2-openapi.yml
- filename: completedns-v1-openapi.yml
  format: yaml
  label: CompleteDNS API v1
  slug: ns-history-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/completedns/refs/heads/main/openapi/completedns-v1-openapi.yml
categories:
- completedns
description: Spectral linting rules defining API design standards and conventions for CompleteDNS.
layout: rules
name: CompleteDNS API Rules
provider_name: CompleteDNS
provider_slug: completedns
rule_count: 10
rules:
- description: API contact information must be present.
  given: $.info
  name: completedns-info-contact
  severity: error
- description: API terms of service must be declared.
  given: $.info
  name: completedns-info-terms
  severity: warn
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: completedns-server-https
  severity: error
- description: Server URLs must include the API version segment.
  given: $.servers[*].url
  name: completedns-server-versioned
  severity: warn
- description: The apiKey query security scheme must be defined.
  given: $.components.securitySchemes
  name: completedns-apikey-security
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: completedns-operation-tags
  severity: warn
- description: Every operation must include a short summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: completedns-operation-summary
  severity: warn
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: completedns-operation-id
  severity: error
- description: Lookup endpoints should accept a domain path parameter.
  given: $.paths[?(@property.indexOf('{domain}') > -1)]
  name: completedns-domain-parameter
  severity: info
- description: Lookup operations should declare 4xx error responses.
  given: $.paths[*].get.responses
  name: completedns-error-responses
  severity: warn
rules_file: rules/completedns-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/completedns/refs/heads/main/rules/completedns-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 5
slug: completedns-rules
source_filename: completedns-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules tuned for the CompleteDNS API.\n# Validates that OpenAPI specs follow CompleteDNS conventions described at\n# https://completedns.com/api/documentation/v2 — API key in the `key`\n# query parameter, JSON responses, and domain-scoped paths.\nrules:\n  completedns-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  completedns-info-terms:\n    description: API terms of service must be declared.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: termsOfService\n      function: truthy\n\n  completedns-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  completedns-server-versioned:\n    description: Server URLs must include the\
  \ API version segment.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/v[12]$\"\n\n  completedns-apikey-security:\n    description: The apiKey query security scheme must be defined.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  completedns-operation-tags:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  completedns-operation-summary:\n    description: Every operation must include a short summary.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  completedns-operation-id:\n    description: Every operation must declare a unique operationId.\n\
  \    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  completedns-domain-parameter:\n    description: Lookup endpoints should accept a domain path parameter.\n    severity: info\n    given: \"$.paths[?(@property.indexOf('{domain}') > -1)]\"\n    then:\n      function: truthy\n\n  completedns-error-responses:\n    description: Lookup operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*].get.responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/completedns/refs/heads/main/rules/completedns-rules.yml
tags:
- DNS
- DNS History
- Domain Intelligence
- Domains
- Nameservers
- Threat Intelligence
- Spectral
- Linting
- API Governance
---
