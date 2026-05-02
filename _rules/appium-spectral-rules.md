---
api_specs:
- filename: appium-server-openapi.yaml
  format: yaml
  label: Appium Server API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/appium/refs/heads/main/openapi/appium-server-openapi.yaml
categories:
- http
- info
- microcks
- 'no'
- openapi
- operation
- parameter
- paths
- request
- response
- schema
- servers
description: Spectral linting rules defining API design standards and conventions for Appium.
layout: rules
name: Appium API Rules
provider_name: Appium
provider_slug: appium
rule_count: 27
rules:
- description: Info title must be present and follow "Appium ..." pattern
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present and have minimum length
  given: $.info
  name: info-description-required
  severity: warn
- description: API version must be specified
  given: $.info
  name: info-version-required
  severity: error
- description: License information must be present (Appium is Apache 2.0)
  given: $.info
  name: info-license-required
  severity: warn
- description: OpenAPI version must be 3.0.x
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-required
  severity: error
- description: Each server must have a description
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Path segments must use kebab-case (lowercase, hyphens)
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not end with a trailing slash
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summary must start with "Appium"
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-appium-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: OperationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must have a 2xx response defined
  given: $.paths[*][get,post,put,patch,delete].responses
  name: operation-success-response-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have a description
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Component schemas must have a title
  given: $.components.schemas[*]
  name: schema-title-required
  severity: warn
- description: Schema property names should use camelCase or snake_case consistently
  given: $.components.schemas[*].properties
  name: schema-properties-snake-case
  severity: info
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: http-get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: http-delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Operations should include x-microcks-operation extension for mock server compatibility
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/appium-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/appium/refs/heads/main/rules/appium-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 2
  warn: 15
slug: appium-spectral-rules
source_filename: appium-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: Info title must be present and follow \"Appium ...\" pattern\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: Info description must be present and have minimum length\n    severity: warn\n    given: $.info\n    then:\n      field: description\n      function: minLength\n      functionOptions:\n        min: 20\n\n  info-version-required:\n    description: API version must be specified\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-license-required:\n    description: License information must be present (Appium is Apache 2.0)\n    severity: warn\n    given: $.info\n    then:\n      field: license\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: OpenAPI version must be 3.0.x\n    severity: error\n    given: $\n    then:\n\
  \      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: At least one server must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-description-required:\n    description: Each server must have a description\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments must use kebab-case (lowercase, hyphens)\n    severity: warn\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}/_-]+)+$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not end with a trailing slash\n    severity: warn\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch:\
  \ \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-appium-prefix:\n    description: Operation summary must start with \"Appium\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^Appium \"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n \
  \   description: OperationId must use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Every parameter must have a schema\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-json-content:\n    description:\
  \ Request bodies should use application/json content type\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      field: application/json\n      function: truthy\n\n  # RESPONSES\n  operation-success-response-required:\n    description: Every operation must have a 2xx response defined\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-description-required:\n    description: Top-level schemas should have a description\n    severity: warn\n    given: $.components.schemas[*]\n\
  \    then:\n      field: description\n      function: truthy\n\n  schema-title-required:\n    description: Component schemas must have a title\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: title\n      function: truthy\n\n  schema-properties-snake-case:\n    description: Schema property names should use camelCase or snake_case consistently\n    severity: info\n    given: $.components.schemas[*].properties\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9_-]*$\"\n\n  # HTTP METHOD CONVENTIONS\n  http-get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  http-delete-no-request-body:\n    description: DELETE operations should not have a request body\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function:\
  \ falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: warn\n    given: $..description\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  microcks-operation-extension:\n    description: Operations should include x-microcks-operation extension for mock server compatibility\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/appium/refs/heads/main/rules/appium-spectral-rules.yml
tags:
- Android
- Cross-Platform
- iOS
- Mobile Testing
- Open Source
- OpenJS Foundation
- Test Automation
- WebDriver
- Spectral
- Linting
- API Governance
---
