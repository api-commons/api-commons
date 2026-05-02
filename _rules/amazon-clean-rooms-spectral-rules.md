---
api_specs:
- filename: amazon-clean-rooms-openapi.yml
  format: yaml
  label: Amazon Clean Rooms API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-clean-rooms/refs/heads/main/openapi/amazon-clean-rooms-openapi.yml
categories:
- delete
- get
- info
- microcks
- 'no'
- openapi
- operation
- pagination
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Clean Rooms.
layout: rules
name: Amazon Clean Rooms API Rules
provider_name: Amazon Clean Rooms
provider_slug: amazon-clean-rooms
rule_count: 29
rules:
- description: API title must start with "Amazon Clean Rooms"
  given: $.info.title
  name: info-title-prefix
  severity: error
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: API must have contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version
  severity: error
- description: API must define at least one server
  given: $
  name: servers-required
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: operationId must use PascalCase (AWS convention)
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationId-pascal-case
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Amazon Clean Rooms"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Path and query parameters should use camelCase (AWS convention)
  given: $.paths[*][get,post,put,patch,delete].parameters[*].name
  name: parameter-camel-case
  severity: warn
- description: Every operation must have a success response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: All response codes must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations should document 400 bad request
  given: $.paths[*][post,put,patch].responses
  name: response-400-required
  severity: warn
- description: Operations should document 403 access denied
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-403-required
  severity: warn
- description: Operations should document 500 internal server error
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-500-required
  severity: warn
- description: Top-level component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-on-top-level
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return 200 or 204
  given: $.paths[*].delete.responses
  name: delete-returns-200-or-204
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have x-microcks-operation extension
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-present
  severity: info
- description: List operations should use nextToken for pagination (AWS convention)
  given: $.paths[*].get.parameters[?(@.name == 'nextToken')]
  name: pagination-uses-next-token
  severity: info
rules_file: rules/amazon-clean-rooms-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-clean-rooms/refs/heads/main/rules/amazon-clean-rooms-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 2
  warn: 13
slug: amazon-clean-rooms-spectral-rules
source_filename: amazon-clean-rooms-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"Amazon Clean Rooms\"\n    severity: error\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Clean Rooms\"\n\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API must have contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n\
  \      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: API must define at least one server\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z][a-zA-Z0-9-]*|/{[a-zA-Z][a-zA-Z0-9]*})*$\"\n\n  # OPERATIONS\n  operation-operationId-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationId-pascal-case:\n\
  \    description: operationId must use PascalCase (AWS convention)\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]+$\"\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries must start with \"Amazon Clean Rooms\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Clean Rooms\"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-tags-required:\n\
  \    description: Every operation must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-camel-case:\n    description: Path and query parameters should use camelCase (AWS convention)\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*].name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have a success response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses\n      function: truthy\n\n  response-description-required:\n\
  \    description: All response codes must have descriptions\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-400-required:\n    description: Operations should document 400 bad request\n    severity: warn\n    given: \"$.paths[*][post,put,patch].responses\"\n    then:\n      field: \"400\"\n      function: truthy\n\n  response-403-required:\n    description: Operations should document 403 access denied\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      field: \"403\"\n      function: truthy\n\n  response-500-required:\n    description: Operations should document 500 internal server error\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      field: \"500\"\n      function: truthy\n\n  # SCHEMAS\n  schema-description-on-top-level:\n    description: Top-level component schemas should\
  \ have descriptions\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: Global security must be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-returns-200-or-204:\n    description: DELETE operations should return 200 or 204\n    severity: warn\n    given: \"$.paths[*].delete.responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n         \
  \ anyOf:\n            - required: [\"200\"]\n            - required: [\"204\"]\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: \"$..description\"\n    then:\n      function: truthy\n\n  microcks-operation-present:\n    description: Operations should have x-microcks-operation extension\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n\n  pagination-uses-next-token:\n    description: List operations should use nextToken for pagination (AWS convention)\n    severity: info\n    given: \"$.paths[*].get.parameters[?(@.name == 'nextToken')]\"\n    then:\n      field: name\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-clean-rooms/refs/heads/main/rules/amazon-clean-rooms-spectral-rules.yml
tags:
- Clean Rooms
- Data Collaboration
- Privacy
- Analytics
- Marketing
- Spectral
- Linting
- API Governance
---
