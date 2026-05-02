---
api_specs:
- filename: amdocs-connectx-openapi.yml
  format: yaml
  label: Amdocs connectX BSS API
  slug: amdocs-connectx-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amdocs/refs/heads/main/openapi/amdocs-connectx-openapi.yml
categories:
- get
- info
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amdocs.
layout: rules
name: Amdocs API Rules
provider_name: Amdocs
provider_slug: amdocs
rule_count: 21
rules:
- description: API title must start with "Amdocs"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Use OpenAPI 3.x
  given: $.openapi
  name: openapi-version-3
  severity: warn
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths should include API version prefix
  given: $.paths[*]~
  name: paths-versioned
  severity: info
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Parameters must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Operations must have a success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should define 401 Unauthorized
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: Response objects must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Component schemas should have a description
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: APIs should use OAuth 2.0 security scheme
  given: $.components.securitySchemes[*]
  name: security-oauth2
  severity: info
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/amdocs-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amdocs/refs/heads/main/rules/amdocs-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 2
  warn: 7
slug: amdocs-spectral-rules
source_filename: amdocs-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"Amdocs\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amdocs\"\n\n  info-description-required:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Use OpenAPI 3.x\n    severity: warn\n    given: \"$.openapi\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n\
  \      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(\\\\/([a-z0-9-]+|\\\\{[a-zA-Z]+\\\\}))*$\"\n\n  paths-versioned:\n    description: Paths should include API version prefix\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^\\\\/v[0-9]\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n\
  \    description: Operations must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId must use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Operations must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Parameters must have a description\n    severity:\
  \ warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must have a success response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-401-required:\n    description: Operations should define 401 Unauthorized\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [\"401\"]\n\n  response-description-required:\n    description: Response objects must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\
  \n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Component schemas should have a description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-oauth2:\n    description: APIs should use OAuth 2.0 security scheme\n    severity: info\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      field: type\n      function: pattern\n      functionOptions:\n        match: \"^oauth2$\"\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n\
  \        match: \".+\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amdocs/refs/heads/main/rules/amdocs-spectral-rules.yml
tags:
- Telecom
- BSS
- OSS
- Billing
- Customer Management
- MVNO
- 5G
- SaaS
- Spectral
- Linting
- API Governance
---
