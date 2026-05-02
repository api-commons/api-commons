---
api_specs:
- filename: cloudrf-openapi.yml
  format: yaml
  label: CloudRF API
  slug: cloudrf-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cloudrf/refs/heads/main/openapi/cloudrf-openapi.yml
categories:
- cloudrf
description: Spectral linting rules defining API design standards and conventions for CloudRF.
layout: rules
name: CloudRF API Rules
provider_name: CloudRF
provider_slug: cloudrf
rule_count: 10
rules:
- description: API contact information must be present.
  given: $.info
  name: cloudrf-info-contact
  severity: error
- description: API license must be declared.
  given: $.info
  name: cloudrf-info-license
  severity: warn
- description: All server URLs must use HTTPS for the CloudRF API.
  given: $.servers[*].url
  name: cloudrf-server-https
  severity: error
- description: Server URLs should target api.cloudrf.com or dev.cloudrf.com.
  given: $.servers[*].url
  name: cloudrf-server-host
  severity: warn
- description: An ApiKey security scheme using the `key` HTTP header must be declared.
  given: $.components.securitySchemes
  name: cloudrf-apikey-required
  severity: error
- description: The CloudRF API key is delivered via the `key` HTTP header.
  given: $.components.securitySchemes[?(@.type=='apiKey')]
  name: cloudrf-apikey-header-name
  severity: warn
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudrf-operation-id
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudrf-operation-tags
  severity: warn
- description: Every operation must include a short summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudrf-operation-summary
  severity: warn
- description: Mutating operations should declare 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: cloudrf-error-responses
  severity: warn
rules_file: rules/cloudrf-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cloudrf/refs/heads/main/rules/cloudrf-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 6
slug: cloudrf-rules
source_filename: cloudrf-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for the CloudRF REST API at api.cloudrf.com.\nrules:\n  cloudrf-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  cloudrf-info-license:\n    description: API license must be declared.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  cloudrf-server-https:\n    description: All server URLs must use HTTPS for the CloudRF API.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  cloudrf-server-host:\n    description: Server URLs should target api.cloudrf.com or dev.cloudrf.com.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(api|dev)\\\\.cloudrf\\\\.com\"\n\n  cloudrf-apikey-required:\n\
  \    description: An ApiKey security scheme using the `key` HTTP header must be declared.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  cloudrf-apikey-header-name:\n    description: The CloudRF API key is delivered via the `key` HTTP header.\n    severity: warn\n    given: \"$.components.securitySchemes[?(@.type=='apiKey')]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            in:\n              const: \"header\"\n            name:\n              const: \"key\"\n          required: [\"in\", \"name\"]\n\n  cloudrf-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  cloudrf-operation-tags:\n    description: Every operation must declare at least one tag.\n    severity: warn\n  \
  \  given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  cloudrf-operation-summary:\n    description: Every operation must include a short summary.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  cloudrf-error-responses:\n    description: Mutating operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cloudrf/refs/heads/main/rules/cloudrf-rules.yml
tags:
- Coverage Modeling
- HF Propagation
- Mesh Network
- Radio Frequency
- RF
- Satellite
- Signal Analysis
- Telecommunications
- Wireless Planning
- Spectral
- Linting
- API Governance
---
