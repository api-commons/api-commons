---
api_specs:
- filename: swagger.json
  format: json
  label: CloudGuard CNAPP REST API
  slug: cloudguard-cnapp-api
  spec_type: OpenAPI
  url: https://api.dome9.com/v2/swagger.json
categories:
- cloudguard
description: Spectral linting rules defining API design standards and conventions for CloudGuard.
layout: rules
name: CloudGuard API Rules
provider_name: CloudGuard
provider_slug: cloudguard
rule_count: 9
rules:
- description: API contact information must be present.
  given: $.info
  name: cloudguard-info-contact
  severity: error
- description: API license must be declared.
  given: $.info
  name: cloudguard-info-license
  severity: warn
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: cloudguard-server-https
  severity: error
- description: CloudGuard control-plane paths must be versioned (/v{N}/).
  given: $.paths
  name: cloudguard-server-versioned
  severity: warn
- description: A security scheme must be declared (CloudGuard uses HTTP Basic with API key + secret).
  given: $.components.securitySchemes
  name: cloudguard-auth-required
  severity: error
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudguard-operation-id
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudguard-operation-tags
  severity: warn
- description: Every operation must include a short summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: cloudguard-operation-summary
  severity: warn
- description: Mutating operations should declare 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: cloudguard-error-responses
  severity: warn
rules_file: rules/cloudguard-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cloudguard/refs/heads/main/rules/cloudguard-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 5
slug: cloudguard-rules
source_filename: cloudguard-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for the CloudGuard CNAPP (Dome9 v2) REST API\n# and any OpenAPI describing CloudGuard-related services.\nrules:\n  cloudguard-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  cloudguard-info-license:\n    description: API license must be declared.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  cloudguard-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  cloudguard-server-versioned:\n    description: CloudGuard control-plane paths must be versioned (/v{N}/).\n    severity: warn\n    given: \"$.paths\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n\
  \          type: object\n          patternProperties:\n            \"^/v\\\\d+/.*\": {}\n          additionalProperties: true\n\n  cloudguard-auth-required:\n    description: A security scheme must be declared (CloudGuard uses HTTP Basic with API key + secret).\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  cloudguard-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  cloudguard-operation-tags:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  cloudguard-operation-summary:\n    description: Every operation must include a short\
  \ summary.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  cloudguard-error-responses:\n    description: Mutating operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cloudguard/refs/heads/main/rules/cloudguard-rules.yml
tags:
- Check Point
- CNAPP
- Cloud Security
- Compliance
- CSPM
- CWPP
- Posture Management
- Spectral
- Linting
- API Governance
---
