---
api_specs:
- filename: accuweather-openapi-original.yml
  format: yaml
  label: AccuWeather API
  slug: accuweather-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/openapi/accuweather-openapi-original.yml
categories:
- delete
- get
- info
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for AccuWeather.
layout: rules
name: AccuWeather API Rules
provider_name: AccuWeather
provider_slug: accuweather
rule_count: 24
rules:
- description: ''
  given: $.info.title
  name: info-title-format
  severity: warn
- description: ''
  given: $.info
  name: info-description-required
  severity: error
- description: ''
  given: $.info
  name: info-version-required
  severity: error
- description: ''
  given: $
  name: openapi-version-3
  severity: error
- description: ''
  given: $
  name: servers-defined
  severity: error
- description: ''
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: ''
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: ''
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-starts-with-accuweather
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: ''
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: ''
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: ''
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-error-401
  severity: info
- description: ''
  given: $.components.schemas[*].properties[*]
  name: schema-properties-described
  severity: info
- description: ''
  given: $.components.schemas[*].properties[*]
  name: schema-type-defined
  severity: warn
- description: ''
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: ''
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: ''
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete].responses[*].content[*]
  name: operation-examples-encouraged
  severity: info
rules_file: rules/accuweather-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/rules/accuweather-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 3
  warn: 10
slug: accuweather-spectral-rules
source_filename: accuweather-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-format:\n    message: API title should start with \"AccuWeather\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^AccuWeather\"\n\n  info-description-required:\n    message: API info must have a non-empty description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    message: API info must include a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    message: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    message: At least one server must be defined\n    severity: error\n    given: \"$\"\n    then:\n   \
  \   field: servers\n      function: truthy\n\n  servers-https-only:\n    message: All server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    message: Path segments should use kebab-case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}-]+)+$\"\n\n  paths-no-trailing-slash:\n    message: Paths should not have trailing slashes\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    message: All operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-starts-with-accuweather:\n\
  \    message: Operation summaries should start with \"AccuWeather\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^AccuWeather\"\n\n  operation-description-required:\n    message: All operations should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-tags-required:\n    message: All operations must have at least one tag\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  operation-id-required:\n    message: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    message: All parameters must have a description\n\
  \    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    message: All parameters must have a schema\n    severity: error\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    message: All operations must have at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-description-required:\n    message: All responses must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-error-401:\n    message: Protected\
  \ operations should include a 401 response\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: ['401']\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-properties-described:\n    message: Schema properties should have descriptions\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-type-defined:\n    message: All schema properties should have a type defined\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    message: Security schemes should be defined in components\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n\
  \    message: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    message: DELETE operations should not have a request body\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  operation-examples-encouraged:\n    message: Operations should include examples for mock server compatibility\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*].content[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['example']\n            - required: ['examples']\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/rules/accuweather-spectral-rules.yml
tags:
- Weather
- Forecasts
- Meteorology
- Location Services
- Air Quality
- Storms
- Spectral
- Linting
- API Governance
---
