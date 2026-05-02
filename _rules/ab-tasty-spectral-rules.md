---
api_specs:
- filename: decision-api-openapi.yml
  format: yaml
  label: AB Tasty Decision API
  slug: ab-tasty-decision-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/openapi/decision-api-openapi.yml
categories:
- delete
- examples
- get
- info
- microcks
- 'no'
- openapi
- operation
- parameter
- paths
- post
- request
- response
- schema
- security
- servers
- tag
description: Spectral linting rules defining API design standards and conventions for AB Tasty.
layout: rules
name: AB Tasty API Rules
provider_name: AB Tasty
provider_slug: ab-tasty
rule_count: 40
rules:
- description: API info must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: API title should start with "AB Tasty"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API description should be meaningful (at least 30 characters)
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: API info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: API info should have contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Should use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: warn
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths should not have trailing slashes
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "AB Tasty"
  given: $.paths[*][get,post,put,patch,delete,options,head].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete,options,head].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-tags-required
  severity: error
- description: Tags used in operations should be defined at the global level
  given: $.tags
  name: tag-global-defined
  severity: warn
- description: Global tags should have descriptions
  given: $.tags[*]
  name: tag-description
  severity: info
- description: All parameters must have a description
  given: $..parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters should have a schema with type defined
  given: $..parameters[*].schema
  name: parameter-schema-type
  severity: warn
- description: API keys should be passed in headers, not query parameters
  given: $.components.securitySchemes[?(@.type == 'apiKey')]
  name: parameter-api-key-in-header
  severity: warn
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-content-type
  severity: warn
- description: Operations must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Secured endpoints should document 401 responses
  given: $.paths[*][post,get,put,delete].responses
  name: response-401-for-secured-endpoints
  severity: warn
- description: APIs with rate limits should document 429 responses
  given: $.paths[*][post].responses
  name: response-429-rate-limit
  severity: info
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should have types defined
  given: $.components.schemas[*].properties[*]
  name: schema-property-type
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Security schemes should be defined in components
  given: $.components.securitySchemes
  name: security-schemes-defined
  severity: error
- description: Security schemes should have descriptions
  given: $.components.securitySchemes[*]
  name: security-scheme-description
  severity: warn
- description: Global security should be defined
  given: $
  name: security-global-defined
  severity: warn
- description: GET operations should not have request bodies
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have request bodies
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: POST operations should have request bodies
  given: $.paths[*].post
  name: post-should-have-request-body
  severity: warn
- description: Descriptions should not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should have examples
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
- description: Operations should have x-microcks-operation extension for mock compatibility
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/ab-tasty-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/rules/ab-tasty-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 5
  warn: 22
slug: ab-tasty-spectral-rules
source_filename: ab-tasty-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: API info must have a title\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-title-prefix:\n    description: API title should start with \"AB Tasty\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^AB Tasty\"\n\n  info-description-required:\n    description: API info must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-description-min-length:\n    description: API description should be meaningful (at least 30 characters)\n    severity: warn\n    given: \"$.info.description\"\n    then:\n      function: minLength\n      functionOptions:\n        value: 30\n\n  info-version-required:\n    description: API info must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n\
  \      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API info should have contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Should use OpenAPI 3.x\n    severity: warn\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description:\n    description: Each server should have a description\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field:\
  \ description\n      function: truthy\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(\\\\/([a-z0-9-{}]+))*\\\\/?$\"\n\n  paths-no-trailing-slash:\n    description: Paths should not have trailing slashes\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"AB Tasty\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,options,head].summary\"\n    then:\n      function:\
  \ pattern\n      functionOptions:\n        match: \"^AB Tasty\"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,options,head].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\
  \n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tag-global-defined:\n    description: Tags used in operations should be defined at the global level\n    severity: warn\n    given: \"$.tags\"\n    then:\n      function: truthy\n\n  tag-description:\n    description: Global tags should have descriptions\n    severity: info\n    given: \"$.tags[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description\n    severity: warn\n    given: \"$..parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-type:\n    description: All parameters should have a schema with type defined\n    severity: warn\n    given: \"$..parameters[*].schema\"\n    then:\n      field: type\n      function: truthy\n\n  parameter-api-key-in-header:\n    description: API keys should be passed in headers, not query parameters\n    severity: warn\n\
  \    given: \"$.components.securitySchemes[?(@.type == 'apiKey')]\"\n    then:\n      field: in\n      function: pattern\n      functionOptions:\n        match: \"^header$\"\n\n  # REQUEST BODIES\n  request-body-content-type:\n    description: Request bodies should use application/json content type\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must have at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\
  \n    then:\n      field: description\n      function: truthy\n\n  response-401-for-secured-endpoints:\n    description: Secured endpoints should document 401 responses\n    severity: warn\n    given: \"$.paths[*][post,get,put,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n\n  response-429-rate-limit:\n    description: APIs with rate limits should document 429 responses\n    severity: info\n    given: \"$.paths[*][post].responses\"\n    then:\n      function: truthy\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-description-required:\n    description: Top-level schemas should have descriptions\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-property-type:\n    description: Schema properties should have types defined\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function:\
  \ truthy\n\n  schema-property-description:\n    description: Schema properties should have descriptions\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes should be defined in components\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  security-scheme-description:\n    description: Security schemes should have descriptions\n    severity: warn\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      field: description\n      function: truthy\n\n  security-global-defined:\n    description: Global security should be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations should not have request bodies\n    severity: error\n    given:\
  \ \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have request bodies\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  post-should-have-request-body:\n    description: POST operations should have request bodies\n    severity: warn\n    given: \"$.paths[*].post\"\n    then:\n      field: requestBody\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions should not be empty strings\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"^\\\\s*$\"\n\n  examples-encouraged:\n    description: Schema properties should have examples\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: example\n      function: truthy\n\n  microcks-operation-extension:\n\
  \    description: Operations should have x-microcks-operation extension for mock compatibility\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/rules/ab-tasty-spectral-rules.yml
tags:
- Aggregation
- Experimentation
- Feature Flags
- Personalization
- A/B Testing
- Spectral
- Linting
- API Governance
---
