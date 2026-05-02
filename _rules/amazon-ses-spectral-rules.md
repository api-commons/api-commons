---
categories:
- delete
- get
- info
- openapi
- operation
- parameter
- response
- schema
- security
- server
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon SES.
layout: rules
name: Amazon SES API Rules
provider_name: Amazon SES
provider_slug: amazon-ses
rule_count: 19
rules:
- description: API must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: warn
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: API must use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS
  given: $.servers[*]
  name: server-https
  severity: warn
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-summary-required
  severity: error
- description: Operations must have a description
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-description-required
  severity: warn
- description: Operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-id-required
  severity: error
- description: OperationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-id-camel-case
  severity: warn
- description: Operations must have tags
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-tags-required
  severity: warn
- description: Parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Operations must have a success response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Responses must have descriptions
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: warn
- description: Schema properties should have types
  given: $.components.schemas[*].properties[*]
  name: schema-type-defined
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Security schemes should be defined
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations should not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
rules_file: rules/amazon-ses-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-ses/refs/heads/main/rules/amazon-ses-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 1
  warn: 10
slug: amazon-ses-spectral-rules
source_filename: amazon-ses-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: API must have a title\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: API must have a description\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: API must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  server-https:\n    description:\
  \ Server URLs should use HTTPS\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: Operations must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: OperationId should use camelCase\n    severity: warn\n\
  \    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Operations must have tags\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Parameters must have descriptions\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must have a success response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: ['200']\n     \
  \       - required: ['201']\n            - required: ['202']\n            - required: ['204']\n\n  response-description-required:\n    description: Responses must have descriptions\n    severity: warn\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-type-defined:\n    description: Schema properties should have types\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  schema-description-required:\n    description: Top-level schemas should have descriptions\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes should be defined\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n\
  \    description: GET operations should not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-ses/refs/heads/main/rules/amazon-ses-spectral-rules.yml
tags:
- Email
- Email Deliverability
- Email Service
- Marketing Email
- Notifications
- SMTP
- Transactional Email
- Spectral
- Linting
- API Governance
---
