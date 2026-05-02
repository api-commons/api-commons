---
api_specs:
- filename: arch-coal-investor-relations-api.yaml
  format: yaml
  label: Arch Coal Investor Relations
  slug: arch-coal-investor-relations
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/arch-coal/refs/heads/main/openapi/arch-coal-investor-relations-api.yaml
categories:
- get
- info
- openapi
- operation
- parameter
- response
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Arch Coal.
layout: rules
name: Arch Coal API Rules
provider_name: Arch Coal
provider_slug: arch-coal
rule_count: 13
rules:
- description: API title must start with "Arch Coal"
  given: $.info
  name: info-title-arch-coal-prefix
  severity: error
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: warn
- description: Use OpenAPI 3.0.x
  given: $
  name: openapi-version-3
  severity: error
- description: Server URLs must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Arch Coal"
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-prefix
  severity: warn
- description: All operations must have tags
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: error
- description: Parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Operations must define success responses
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: GET operations must not have request bodies
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
rules_file: rules/arch-coal-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/arch-coal/refs/heads/main/rules/arch-coal-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 0
  warn: 3
slug: arch-coal-spectral-rules
source_filename: arch-coal-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-arch-coal-prefix:\n    description: API title must start with \"Arch Coal\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: \"^Arch Coal\"\n  info-description-required:\n    description: API must have a description\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  openapi-version-3:\n    description: Use OpenAPI 3.0.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n  servers-defined:\n    description: Server URLs must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n\
  \        match: \"^https://\"\n  operation-id-required:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n  operation-summary-prefix:\n    description: Operation summaries should start with \"Arch Coal\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^Arch Coal\"\n  operation-tags-required:\n    description: All operations must have tags\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n  parameter-description-required:\n    description:\
  \ Parameters must have descriptions\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n  response-success-required:\n    description: Operations must define success responses\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].responses\"\n    then:\n      function: truthy\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n  get-no-request-body:\n    description: GET operations must not have request bodies\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/arch-coal/refs/heads/main/rules/arch-coal-spectral-rules.yml
tags:
- Mining
- Coal
- Metallurgical Coal
- Thermal Coal
- Energy
- Fortune 500
- Spectral
- Linting
- API Governance
---
