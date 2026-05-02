---
api_specs:
- filename: apidog-apidog-openapi.yml
  format: yaml
  label: Apidog
  slug: apidog
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/apidog/refs/heads/main/openapi/apidog-apidog-openapi.yml
categories:
- info
- openapi
- operation
- parameter
- paths
- post
- response
- security
- servers
- tag
description: Spectral linting rules defining API design standards and conventions for Apidog.
layout: rules
name: Apidog API Rules
provider_name: Apidog
provider_slug: apidog
rule_count: 20
rules:
- description: API title must start with 'Apidog'.
  given: $.info
  name: info-title-prefix
  severity: warn
- description: API must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version.
  given: $.info
  name: info-version-required
  severity: error
- description: Specs must use OpenAPI 3.x.
  given: $
  name: openapi-version-3
  severity: warn
- description: Servers must be defined.
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*]
  name: servers-https
  severity: error
- description: Path segments must use kebab-case.
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have a trailing slash.
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with 'Apidog'.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: OperationId must use camelCase.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-camelcase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: All tags must have a description.
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must have a 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Protected operations should have a 401 response.
  given: $.paths[*][post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: Security schemes must be defined in components.
  given: $.components.securitySchemes
  name: security-scheme-defined
  severity: error
- description: POST operations should have a request body.
  given: $.paths[*].post
  name: post-has-request-body
  severity: warn
rules_file: rules/apidog-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/apidog/refs/heads/main/rules/apidog-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 0
  warn: 12
slug: apidog-spectral-rules
source_filename: apidog-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with 'Apidog'.\n    severity: warn\n    given: '$.info'\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: '^Apidog'\n\n  info-description-required:\n    description: API must have a description.\n    severity: error\n    given: '$.info'\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must have a version.\n    severity: error\n    given: '$.info'\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Specs must use OpenAPI 3.x.\n    severity: warn\n    given: '$'\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: '^3\\.'\n\n  # SERVERS\n  servers-defined:\n    description: Servers must be defined.\n    severity: error\n    given: '$'\n    then:\n \
  \     field: servers\n      function: truthy\n\n  servers-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: '$.servers[*]'\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: '^https://'\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments must use kebab-case.\n    severity: warn\n    given: '$.paths'\n    then:\n      field: '@key'\n      function: pattern\n      functionOptions:\n        match: '^(/[a-z0-9{}-]+)+$'\n\n  paths-no-trailing-slash:\n    description: Paths must not have a trailing slash.\n    severity: warn\n    given: '$.paths'\n    then:\n      field: '@key'\n      function: pattern\n      functionOptions:\n        notMatch: '/$'\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: summary\n      function: truthy\n\
  \n  operation-summary-prefix:\n    description: Operation summaries must start with 'Apidog'.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: '^Apidog'\n\n  operation-description-required:\n    description: Every operation must have a description.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camelcase:\n    description: OperationId must use camelCase.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]*$'\n\
  \n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tag-description-required:\n    description: All tags must have a description.\n    severity: warn\n    given: '$.tags[*]'\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].parameters[*]'\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have a 2xx response.\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].responses'\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n        \
  \    - required: ['201']\n            - required: ['204']\n\n  response-401-required:\n    description: Protected operations should have a 401 response.\n    severity: warn\n    given: '$.paths[*][post,put,patch,delete].responses'\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          required: ['401']\n\n  # SECURITY\n  security-scheme-defined:\n    description: Security schemes must be defined in components.\n    severity: error\n    given: '$.components.securitySchemes'\n    then:\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  post-has-request-body:\n    description: POST operations should have a request body.\n    severity: warn\n    given: '$.paths[*].post'\n    then:\n      field: requestBody\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/apidog/refs/heads/main/rules/apidog-spectral-rules.yml
tags:
- API Design
- API Lifecycle
- API Testing
- Collaboration
- Design-First
- Documentation
- Mocking
- Platform
- Spectral
- Linting
- API Governance
---
