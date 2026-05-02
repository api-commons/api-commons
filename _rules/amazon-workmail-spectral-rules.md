---
api_specs:
- filename: amazon-workmail-openapi-original.yaml
  format: yaml
  label: Amazon WorkMail API
  slug: amazon-workmail-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-workmail/refs/heads/main/openapi/amazon-workmail-openapi-original.yaml
categories:
- components
- get
- info
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
description: Spectral linting rules defining API design standards and conventions for Amazon WorkMail.
layout: rules
name: Amazon WorkMail API Rules
provider_name: Amazon WorkMail
provider_slug: amazon-workmail
rule_count: 19
rules:
- description: API title should reference Amazon WorkMail
  given: $.info
  name: info-title-format
  severity: warn
- description: API info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.0.x
  given: $
  name: openapi-version
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https
  severity: error
- description: Paths must not have a trailing slash
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: warn
- description: Operation summary should start with Amazon WorkMail
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-prefix
  severity: info
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: All parameters must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Request bodies should support application/json
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have a description
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: info
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Security schemes should be defined in components
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: Components schemas should be defined for reuse
  given: $.components
  name: components-schemas-exist
  severity: info
rules_file: rules/amazon-workmail-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-workmail/refs/heads/main/rules/amazon-workmail-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 3
  warn: 8
slug: amazon-workmail-spectral-rules
source_filename: amazon-workmail-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Amazon WorkMail API Spectral Ruleset\n\nrules:\n\n  info-title-format:\n    description: API title should reference Amazon WorkMail\n    severity: warn\n    given: $.info\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: \"^Amazon WorkMail\"\n\n  info-description-required:\n    description: API info must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API info must have a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  openapi-version:\n    description: Must use OpenAPI 3.0.x\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  servers-defined:\n    description: At least one server must be defined\n    severity: error\n    given: $\n    then:\n    \
  \  field: servers\n      function: truthy\n\n  servers-https:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: $.servers[*]\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have a trailing slash\n    severity: warn\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation\
  \ summary should start with Amazon WorkMail\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^Amazon WorkMail\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  parameter-description-required:\n    description: All parameters must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  request-body-json-content:\n    description: Request bodies should support application/json\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      field: application/json\n      function: truthy\n\n  response-description-required:\n    description: All responses must\
  \ have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-description-recommended:\n    description: Top-level schemas should have a description\n    severity: info\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: warn\n    given: $..description\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  security-schemes-defined:\n    description: Security schemes should be defined in components\n    severity: warn\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\
  \n  components-schemas-exist:\n    description: Components schemas should be defined for reuse\n    severity: info\n    given: $.components\n    then:\n      field: schemas\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-workmail/refs/heads/main/rules/amazon-workmail-spectral-rules.yml
tags:
- Business Communication
- Calendar
- Email
- Exchange
- Enterprise
- Spectral
- Linting
- API Governance
---
