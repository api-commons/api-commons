---
api_specs:
- filename: amazon-data-exchange-openapi.yml
  format: yaml
  label: AWS Data Exchange API
  slug: aws-data-exchange-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-data-exchange/refs/heads/main/openapi/amazon-data-exchange-openapi.yml
categories:
- arn
- create
- delete
- get
- info
- list
- 'no'
- openapi
- operation
- paths
- request
- response
- schema
- security
- servers
- tag
- tags
- update
description: Spectral linting rules defining API design standards and conventions for Amazon Data Exchange.
layout: rules
name: Amazon Data Exchange API Rules
provider_name: Amazon Data Exchange
provider_slug: amazon-data-exchange
rule_count: 30
rules:
- description: API title must start with "AWS Data Exchange"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must have a version
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
- description: Servers array must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: AWS Data Exchange API paths should include version prefix /v1/
  given: $.paths[*]~
  name: paths-versioned
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
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
- description: Create operations should use POST method
  given: $.paths[*][post].operationId
  name: create-uses-post
  severity: info
- description: Get/List operations should use GET method
  given: $.paths[*][get].operationId
  name: get-uses-get-method
  severity: info
- description: Update operations should use PATCH method
  given: $.paths[*][patch].operationId
  name: update-uses-patch
  severity: info
- description: Delete/Cancel operations should use DELETE method
  given: $.paths[*][delete].operationId
  name: delete-uses-delete-method
  severity: info
- description: Tags array should be defined globally
  given: $
  name: tags-defined
  severity: warn
- description: Each tag must have a description
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: POST/PATCH request bodies should support application/json
  given: $.paths[*][post,patch].requestBody.content
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
- description: Error response schemas should include a message field
  given: $.components.schemas.Error.properties
  name: response-error-has-message
  severity: warn
- description: Top-level schemas should have a description
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: List operations should support pagination via NextToken
  given: $.paths[*][get].responses.200.content.application/json.schema.properties
  name: list-response-has-next-token
  severity: info
- description: ARN fields should have descriptions documenting them as unique identifiers
  given: $.components.schemas[*].properties.Arn.description
  name: arn-field-documented
  severity: info
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have examples in request/response bodies
  given: $.paths[*][*].requestBody.content[*]
  name: operation-examples-encouraged
  severity: info
rules_file: rules/amazon-data-exchange-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-data-exchange/refs/heads/main/rules/amazon-data-exchange-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 7
  warn: 10
slug: amazon-data-exchange-spectral-rules
source_filename: amazon-data-exchange-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"AWS Data Exchange\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^AWS Data Exchange\"\n\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Info object should have a contact\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3x:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function:\
  \ pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers array must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS\n  paths-versioned:\n    description: AWS Data Exchange API paths should include version prefix /v1/\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/v1/|^/tags/\"\n\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}-]+)+$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description:\
  \ All operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: All operations must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: OperationId must use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: All operations must have tags\n    severity: error\n    given: \"\
  $.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  # CRUD CONVENTIONS\n  create-uses-post:\n    description: Create operations should use POST method\n    severity: info\n    given: \"$.paths[*][post].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(create|import|start)\"\n\n  get-uses-get-method:\n    description: Get/List operations should use GET method\n    severity: info\n    given: \"$.paths[*][get].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(get|list)\"\n\n  update-uses-patch:\n    description: Update operations should use PATCH method\n    severity: info\n    given: \"$.paths[*][patch].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(update|start)\"\n\n  delete-uses-delete-method:\n    description: Delete/Cancel operations should use DELETE method\n    severity: info\n    given: \"$.paths[*][delete].operationId\"\
  \n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(delete|cancel|untag)\"\n\n  # TAGS\n  tags-defined:\n    description: Tags array should be defined globally\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  tag-description-required:\n    description: Each tag must have a description\n    severity: warn\n    given: \"$.tags[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-json-content:\n    description: POST/PATCH request bodies should support application/json\n    severity: warn\n    given: \"$.paths[*][post,patch].requestBody.content\"\n    then:\n      field: application/json\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: All operations must have at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n\
  \        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"202\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-error-has-message:\n    description: Error response schemas should include a message field\n    severity: warn\n    given: \"$.components.schemas.Error.properties\"\n    then:\n      field: message\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Top-level schemas should have a description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # PAGINATION\n  list-response-has-next-token:\n    description: List operations should support pagination via NextToken\n    severity: info\n\
  \    given: \"$.paths[*][get].responses.200.content.application/json.schema.properties\"\n    then:\n      field: NextToken\n      function: truthy\n\n  # ARN IDENTIFIERS\n  arn-field-documented:\n    description: ARN fields should have descriptions documenting them as unique identifiers\n    severity: info\n    given: \"$.components.schemas[*].properties.Arn.description\"\n    then:\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  operation-examples-encouraged:\n    description: Operations should have examples in request/response bodies\n    severity: info\n  \
  \  given: \"$.paths[*][*].requestBody.content[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"examples\"]\n            - required: [\"example\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-data-exchange/refs/heads/main/rules/amazon-data-exchange-spectral-rules.yml
tags:
- Data Exchange
- Data Marketplace
- Third-Party Data
- Analytics
- Subscriptions
- Spectral
- Linting
- API Governance
---
