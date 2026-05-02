---
api_specs:
- filename: amazon-gamelift-openapi.yaml
  format: yaml
  label: Amazon GameLift API
  slug: amazon-gamelift-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-gamelift/refs/heads/main/openapi/amazon-gamelift-openapi.yaml
categories:
- info
- microcks
- 'no'
- openapi
- operation
- request
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon GameLift.
layout: rules
name: Amazon GameLift API Rules
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
rule_count: 18
rules:
- description: API title must start with "Amazon GameLift"
  given: $.info.title
  name: info-title-format
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.0.x
  given: $.openapi
  name: openapi-version
  severity: warn
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs should use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with Amazon GameLift
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-company-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: Operations must have at least one success (2xx) response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Responses must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Request bodies should have descriptions
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: info
- description: Security schemes should be defined in components
  given: $
  name: security-schemes-defined
  severity: warn
- description: Schema properties should have types defined
  given: $.components.schemas[*].properties[*]
  name: schema-properties-typed
  severity: info
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have x-microcks-operation for mock support
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/amazon-gamelift-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-gamelift/refs/heads/main/rules/amazon-gamelift-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 3
  warn: 8
slug: amazon-gamelift-spectral-rules
source_filename: amazon-gamelift-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-format:\n    description: API title must start with \"Amazon GameLift\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon GameLift\"\n\n  info-description-required:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description: Must use OpenAPI 3.0.x\n    severity: warn\n    given: \"$.openapi\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n\
  \      function: truthy\n\n  servers-https:\n    description: Server URLs should use HTTPS\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-company-prefix:\n    description: Operation summaries must start with Amazon GameLift\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon GameLift\"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n\
  \    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId must use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must have at least one success (2xx) response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: Responses must have descriptions\n    severity: warn\n \
  \   given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # REQUEST BODY\n  request-body-description:\n    description: Request bodies should have descriptions\n    severity: info\n    given: \"$.paths[*][post,put,patch].requestBody\"\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes should be defined in components\n    severity: warn\n    given: \"$\"\n    then:\n      field: components.securitySchemes\n      function: truthy\n\n  # SCHEMAS\n  schema-properties-typed:\n    description: Schema properties should have types defined\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # GENERAL\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: \"$..description\"\n    then:\n      function:\
  \ pattern\n      functionOptions:\n        match: \".+\"\n\n  microcks-operation-extension:\n    description: Operations should have x-microcks-operation for mock support\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-gamelift/refs/heads/main/rules/amazon-gamelift-spectral-rules.yml
tags:
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
- Spectral
- Linting
- API Governance
---
