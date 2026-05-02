---
api_specs:
- filename: amazon-connect-openapi.yml
  format: yaml
  label: Amazon Connect Service API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-connect/refs/heads/main/openapi/amazon-connect-openapi.yml
categories:
- delete
- get
- info
- instance
- 'no'
- openapi
- operation
- parameter
- paths
- request
- response
- schema
- security
- servers
- tag
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon Connect.
layout: rules
name: Amazon Connect API Rules
provider_name: Amazon Connect
provider_slug: amazon-connect
rule_count: 36
rules:
- description: API title must start with "Amazon Connect"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info object must have a description of at least 50 characters
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must have a version field
  given: $.info
  name: info-version-required
  severity: error
- description: Info object should have a contact
  given: $.info
  name: info-contact-required
  severity: warn
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3x
  severity: error
- description: Servers array must be defined and non-empty
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Each server must have a description
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Path segments must use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summary must start with "Amazon Connect"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-amazon-connect-prefix
  severity: warn
- description: All operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: OperationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: All operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Tags array should be defined at the global level
  given: $
  name: tags-defined
  severity: warn
- description: Each global tag must have a description
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: All parameters must have a description
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: All parameters must have a schema
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Query and header parameter names should use camelCase (AWS convention)
  given: $.paths[*][*].parameters[?(@.in == 'query')].name
  name: parameter-name-snake-case
  severity: info
- description: Request body should have a description
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: warn
- description: Request body should support application/json
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: All operations must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: POST operations should return a 400 Bad Request response
  given: $.paths[*].post.responses
  name: response-400-on-post
  severity: warn
- description: Error response schemas should include a message field
  given: $.components.schemas.Error.properties
  name: response-error-has-message
  severity: warn
- description: Top-level schemas should have a description
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should have a type defined
  given: $.components.schemas[*].properties[*]
  name: schema-properties-type-required
  severity: warn
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Operations should have examples in responses
  given: $.paths[*][*].responses[*].content[*]
  name: operation-examples-encouraged
  severity: info
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations using InstanceId path parameter should document it consistently
  given: $.paths[*][*].parameters[?(@.name == 'InstanceId')]
  name: instance-id-path-param
  severity: info
rules_file: rules/amazon-connect-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-connect/refs/heads/main/rules/amazon-connect-spectral-rules.yml
severity_counts:
  error: 16
  hint: 0
  info: 3
  warn: 17
slug: amazon-connect-spectral-rules
source_filename: amazon-connect-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"Amazon Connect\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Connect\"\n\n  info-description-required:\n    description: Info object must have a description of at least 50 characters\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must have a version field\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Info object should have a contact\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3x:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field:\
  \ openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers array must be defined and non-empty\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description-required:\n    description: Each server must have a description\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments must use kebab-case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}-]+)+$\"\n\n  paths-no-trailing-slash:\n    description: Paths\
  \ must not have trailing slashes\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-amazon-connect-prefix:\n    description: Operation summary must start with \"Amazon Connect\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Connect\"\n\n  operation-description-required:\n    description: All operations must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: All operations must have an\
  \ operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: OperationId must use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: All operations must have tags\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tags-defined:\n    description: Tags array should be defined at the global level\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  tag-description-required:\n    description: Each global tag must have a description\n    severity: warn\n    given: \"$.tags[*]\"\n    then:\n      field: description\n      function: truthy\n\
  \n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description\n    severity: error\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: All parameters must have a schema\n    severity: error\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  parameter-name-snake-case:\n    description: Query and header parameter names should use camelCase (AWS convention)\n    severity: info\n    given: \"$.paths[*][*].parameters[?(@.in == 'query')].name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  # REQUEST BODIES\n  request-body-description:\n    description: Request body should have a description\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody\"\n    then:\n      field: description\n      function: truthy\n\n  request-body-json-content:\n\
  \    description: Request body should support application/json\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      field: application/json\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: All operations must have at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-400-on-post:\n    description: POST operations should return a 400 Bad Request response\n    severity: warn\n    given: \"$.paths[*].post.responses\"\n    then:\n\
  \      field: \"400\"\n      function: truthy\n\n  response-error-has-message:\n    description: Error response schemas should include a message field\n    severity: warn\n    given: \"$.components.schemas.Error.properties\"\n    then:\n      field: message\n      function: truthy\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-description-required:\n    description: Top-level schemas should have a description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-properties-type-required:\n    description: Schema properties should have a type defined\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n\
  \    description: Global security must be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  operation-examples-encouraged:\n    description: Operations should have examples in responses\n    severity: info\n    given: \"$.paths[*][*].responses[*].content[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"example\"]\n            - required: [\"examples\"]\n\n  no-empty-descriptions:\n    description: Descriptions\
  \ must not be empty strings\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  instance-id-path-param:\n    description: Operations using InstanceId path parameter should document it consistently\n    severity: info\n    given: \"$.paths[*][*].parameters[?(@.name == 'InstanceId')]\"\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-connect/refs/heads/main/rules/amazon-connect-spectral-rules.yml
tags:
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
- Spectral
- Linting
- API Governance
---
