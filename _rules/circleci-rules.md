---
api_specs:
- filename: circleci-rest-api-v2-openapi.yml
  format: yaml
  label: CircleCI REST API V2
  slug: rest-api-v2
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/circleci/refs/heads/main/openapi/circleci-rest-api-v2-openapi.yml
- filename: circleci-rest-api-v1-openapi.yml
  format: yaml
  label: CircleCI REST API V1
  slug: rest-api-v1
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/circleci/refs/heads/main/openapi/circleci-rest-api-v1-openapi.yml
- filename: circleci-runner-api-openapi.yml
  format: yaml
  label: CircleCI Self-Hosted Runner API
  slug: runner-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/circleci/refs/heads/main/openapi/circleci-runner-api-openapi.yml
- filename: circleci-webhooks-asyncapi.yml
  format: yaml
  label: CircleCI Webhooks
  slug: webhooks
  spec_type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/circleci/refs/heads/main/asyncapi/circleci-webhooks-asyncapi.yml
categories:
- circleci
description: Spectral linting rules defining API design standards and conventions for CircleCI.
layout: rules
name: CircleCI API Rules
provider_name: CircleCI
provider_slug: circleci
rule_count: 10
rules:
- description: API contact information must be present.
  given: $.info
  name: circleci-info-contact
  severity: error
- description: API license must be declared.
  given: $.info
  name: circleci-info-license
  severity: warn
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: circleci-server-https
  severity: error
- description: REST v2 server URLs must include /api/v2.
  given: $.servers[?(@.url && @.url.indexOf('circleci.com') > -1)].url
  name: circleci-server-versioned
  severity: warn
- description: A Circle-Token API key security scheme must be defined.
  given: $.components.securitySchemes
  name: circleci-token-security
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: circleci-operation-tags
  severity: warn
- description: Every operation must include a short summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: circleci-operation-summary
  severity: warn
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: circleci-operation-id
  severity: error
- description: Mutating operations should declare 4xx/5xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: circleci-error-responses
  severity: warn
- description: List endpoints should support page-token pagination.
  given: $.paths[?(@property.match(/list$|projects$|workflows$|jobs$|pipelines$/))].get.parameters[*].name
  name: circleci-pagination-cursor
  severity: info
rules_file: rules/circleci-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/circleci/refs/heads/main/rules/circleci-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 5
slug: circleci-rules
source_filename: circleci-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules tuned for CircleCI REST APIs.\n# Validates that OpenAPI specs follow the conventions described at\n# https://circleci.com/docs/api/v2/ — token-based auth via Circle-Token,\n# JSON responses, and resource-oriented v2 paths.\nrules:\n  circleci-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  circleci-info-license:\n    description: API license must be declared.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  circleci-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  circleci-server-versioned:\n    description: REST v2 server URLs must include /api/v2.\n    severity: warn\n    given:\
  \ \"$.servers[?(@.url && @.url.indexOf('circleci.com') > -1)].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/api/v[12](\\\\.\\\\d+)?$\"\n\n  circleci-token-security:\n    description: A Circle-Token API key security scheme must be defined.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  circleci-operation-tags:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  circleci-operation-summary:\n    description: Every operation must include a short summary.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  circleci-operation-id:\n    description: Every operation must declare a unique\
  \ operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  circleci-error-responses:\n    description: Mutating operations should declare 4xx/5xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n            - required: [\"422\"]\n\n  circleci-pagination-cursor:\n    description: List endpoints should support page-token pagination.\n    severity: info\n    given: \"$.paths[?(@property.match(/list$|projects$|workflows$|jobs$|pipelines$/))].get.parameters[*].name\"\n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - page-token\n          - circle-token\n\
  \          - branch\n          - mine\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/circleci/refs/heads/main/rules/circleci-rules.yml
tags:
- CI/CD
- Continuous Integration
- Continuous Deployment
- DevOps
- Pipelines
- Workflows
- Spectral
- Linting
- API Governance
---
