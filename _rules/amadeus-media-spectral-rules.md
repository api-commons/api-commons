---
api_specs:
- filename: amadeus-media-hotel-content-openapi.yaml
  format: yaml
  label: Hotel Content API
  slug: hotel-content-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amadeus-media/refs/heads/main/openapi/amadeus-media-hotel-content-openapi.yaml
- filename: amadeus-media-hotel-list-openapi.yaml
  format: yaml
  label: Hotel List API
  slug: hotel-list-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amadeus-media/refs/heads/main/openapi/amadeus-media-hotel-list-openapi.yaml
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
description: Spectral linting rules defining API design standards and conventions for Amadeus Media.
layout: rules
name: Amadeus Media API Rules
provider_name: Amadeus Media
provider_slug: amadeus-media
rule_count: 31
rules:
- description: API title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: API title must start with "Amadeus".
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be present.
  given: $.info
  name: info-version-required
  severity: error
- description: APIs must use OpenAPI 3.x.
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Each server should have a description.
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Path segments must use kebab-case.
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Amadeus".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-amadeus-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId must use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Operations should include x-microcks-operation for mock compatibility.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-microcks-extension
  severity: info
- description: Every parameter must have a description.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: Every parameter must have a schema.
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Parameter names should use snake_case or camelCase.
  given: $.paths[*][*].parameters[*].name
  name: parameter-snake-case
  severity: info
- description: Every operation must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should define a 400 error response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-400-recommended
  severity: info
- description: Operations should define a 401 error response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-recommended
  severity: warn
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: warn
- description: Schema properties should define a type.
  given: $.components.schemas[*].properties[*]
  name: schema-property-type-required
  severity: warn
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: BearerAuth security scheme should have a description.
  given: $.components.securitySchemes.BearerAuth
  name: security-bearer-described
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Responses should use application/vnd.amadeus+json or application/json content type.
  given: $.paths[*][*].responses[*].content
  name: response-json-content
  severity: info
rules_file: rules/amadeus-media-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amadeus-media/refs/heads/main/rules/amadeus-media-spectral-rules.yml
severity_counts:
  error: 17
  hint: 0
  info: 4
  warn: 10
slug: amadeus-media-spectral-rules
source_filename: amadeus-media-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: API title must be present.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-title-prefix:\n    description: API title must start with \"Amadeus\".\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amadeus\"\n\n  info-description-required:\n    description: API must have a description.\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API version must be present.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: APIs must use OpenAPI 3.x.\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\
  \\.\"\n\n  # SERVERS\n  servers-required:\n    description: At least one server must be defined.\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description:\n    description: Each server should have a description.\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments must use kebab-case.\n    severity: warn\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}-]+)*$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes.\n    severity: error\n    given: $.paths\n    then:\n      function: pattern\n    \
  \  functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-amadeus-prefix:\n    description: Operation summaries must start with \"Amadeus\".\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amadeus \"\n\n  operation-description-required:\n    description: Every operation must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\
  \n  operation-id-camel-case:\n    description: operationId must use camelCase.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  operation-microcks-extension:\n    description: Operations should include x-microcks-operation for mock compatibility.\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: x-microcks-operation\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n\
  \    description: Every parameter must have a schema.\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  parameter-snake-case:\n    description: Parameter names should use snake_case or camelCase.\n    severity: info\n    given: $.paths[*][*].parameters[*].name\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9_]*$\"\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must define at least one 2xx response.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-400-recommended:\n    description: Operations should define a 400 error response.\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: '400'\n      function: truthy\n\n  response-401-recommended:\n\
  \    description: Operations should define a 401 error response.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: '401'\n      function: truthy\n\n  response-description-required:\n    description: Every response must have a description.\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-recommended:\n    description: Top-level schemas should have descriptions.\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-property-type-required:\n    description: Schema properties should define a type.\n    severity: warn\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    severity: error\n    given:\
  \ $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-bearer-described:\n    description: BearerAuth security scheme should have a description.\n    severity: warn\n    given: $.components.securitySchemes.BearerAuth\n    then:\n      field: description\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body.\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  # CONTENT TYPE\n  response-json-content:\n    description: Responses should use application/vnd.amadeus+json or application/json content type.\n    severity: info\n    given: $.paths[*][*].responses[*].content\n    then:\n      function: schema\n\
  \      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amadeus-media/refs/heads/main/rules/amadeus-media-spectral-rules.yml
tags:
- Content
- Hotels
- Images
- Media
- Travel
- Spectral
- Linting
- API Governance
---
