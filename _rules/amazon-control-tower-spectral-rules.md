---
api_specs:
- filename: amazon-control-tower-openapi.yml
  format: yaml
  label: AWS Control Tower API
  slug: aws-control-tower-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-control-tower/refs/heads/main/openapi/amazon-control-tower-openapi.yml
categories:
- arn
- async
- info
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
description: Spectral linting rules defining API design standards and conventions for Amazon Control Tower.
layout: rules
name: Amazon Control Tower API Rules
provider_name: Amazon Control Tower
provider_slug: amazon-control-tower
rule_count: 27
rules:
- description: API title must start with "AWS Control Tower"
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
- description: AWS Control Tower API paths use POST for all non-tag operations
  given: $.paths[*]~
  name: paths-post-convention
  severity: info
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "AWS Control Tower"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-aws-prefix
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
- description: Tags array should be defined globally
  given: $
  name: tags-defined
  severity: warn
- description: Each tag must have a description
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: POST request bodies should support application/json
  given: $.paths[*].post.requestBody.content
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
- description: Asynchronous operations (create, update, delete, reset, enable, disable) should return an operationIdentifier
  given: $.paths[?(@ =~ /create|update|delete|reset|enable|disable/)].post.responses.200.content.application/json.schema.properties
  name: async-operation-identifier-in-response
  severity: info
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have examples in request bodies
  given: $.paths[*][*].requestBody.content[*]
  name: operation-examples-encouraged
  severity: info
- description: Control Tower uses ARNs as resource identifiers - document them consistently
  given: $.paths[*][*].requestBody.content.application/json.schema.properties[?(@ =~ /Identifier|Arn/)].description
  name: arn-as-identifier-convention
  severity: info
rules_file: rules/amazon-control-tower-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-control-tower/refs/heads/main/rules/amazon-control-tower-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 4
  warn: 10
slug: amazon-control-tower-spectral-rules
source_filename: amazon-control-tower-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"AWS Control Tower\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^AWS Control Tower\"\n\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Info object should have a contact\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3x:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function:\
  \ pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers array must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS — POST-CENTRIC CONVENTION\n  paths-post-convention:\n    description: AWS Control Tower API paths use POST for all non-tag operations\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/(create|delete|get|list|update|reset|enable|disable)-|^/tags/\"\n\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"\
  ^(/[a-z0-9{}-]+)+$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-aws-prefix:\n    description: Operation summaries must start with \"AWS Control Tower\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^AWS Control Tower\"\n\n  operation-description-required:\n    description: All operations must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\
  \n  operation-id-camel-case:\n    description: OperationId must use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: All operations must have tags\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tags-defined:\n    description: Tags array should be defined globally\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  tag-description-required:\n    description: Each tag must have a description\n    severity: warn\n    given: \"$.tags[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-json-content:\n    description: POST request bodies should support application/json\n    severity: warn\n    given: \"$.paths[*].post.requestBody.content\"\
  \n    then:\n      field: application/json\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: All operations must have at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-error-has-message:\n    description: Error response schemas should include a message field\n    severity: warn\n    given: \"$.components.schemas.Error.properties\"\n    then:\n      field: message\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Top-level schemas\
  \ should have a description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # ASYNC OPERATIONS\n  async-operation-identifier-in-response:\n    description: Asynchronous operations (create, update, delete, reset, enable, disable) should return an operationIdentifier\n    severity: info\n    given: \"$.paths[?(@ =~ /create|update|delete|reset|enable|disable/)].post.responses.200.content.application/json.schema.properties\"\n    then:\n      field: operationIdentifier\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n\
  \        match: \".+\"\n\n  operation-examples-encouraged:\n    description: Operations should have examples in request bodies\n    severity: info\n    given: \"$.paths[*][*].requestBody.content[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"examples\"]\n            - required: [\"example\"]\n\n  arn-as-identifier-convention:\n    description: Control Tower uses ARNs as resource identifiers - document them consistently\n    severity: info\n    given: \"$.paths[*][*].requestBody.content.application/json.schema.properties[?(@ =~ /Identifier|Arn/)].description\"\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-control-tower/refs/heads/main/rules/amazon-control-tower-spectral-rules.yml
tags:
- Compliance
- Governance
- Landing Zone
- Multi-Account
- Security
- Controls
- Spectral
- Linting
- API Governance
---
