---
api_specs:
- filename: adobe-premiere-creative-cloud-libraries-openapi.yml
  format: yaml
  label: Adobe Creative Cloud Libraries API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/adobe-premiere/refs/heads/main/openapi/adobe-premiere-creative-cloud-libraries-openapi.yml
categories:
- delete
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
description: Spectral linting rules defining API design standards and conventions for Adobe Premiere Pro.
layout: rules
name: Adobe Premiere Pro API Rules
provider_name: Adobe Premiere Pro
provider_slug: adobe-premiere
rule_count: 27
rules:
- description: API title must start with "Adobe"
  given: $.info.title
  name: info-title-adobe-prefix
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must declare a version
  given: $.info
  name: info-version-required
  severity: error
- description: API info should include contact details
  given: $.info
  name: info-contact-required
  severity: warn
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: API must define servers
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Paths must not end with trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Summaries should start with "Adobe Premiere"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-adobe-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camelcase
  severity: warn
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: Parameters must have schemas
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should have descriptions
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: warn
- description: Operations must define 2xx responses
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Responses must have descriptions
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Operations should define 401 error response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-error-401
  severity: warn
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description
  severity: warn
- description: Schemas should define a type
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: API must define security schemes
  given: $.components
  name: security-schemes-defined
  severity: error
- description: API should define global security
  given: $
  name: security-global-defined
  severity: warn
- description: GET must not have request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE should not have request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/adobe-premiere-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/adobe-premiere/refs/heads/main/rules/adobe-premiere-spectral-rules.yml
severity_counts:
  error: 16
  hint: 0
  info: 0
  warn: 11
slug: adobe-premiere-spectral-rules
source_filename: adobe-premiere-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-adobe-prefix:\n    description: API title must start with \"Adobe\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Adobe\"\n\n  info-description-required:\n    description: API must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must declare a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API info should include contact details\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match:\
  \ \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: API must define servers\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS\n  paths-no-trailing-slash:\n    description: Paths must not end with trailing slash\n    severity: warn\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-adobe-prefix:\n    description: Summaries should start with \"Adobe Premiere\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n\
  \    then:\n      function: pattern\n      functionOptions:\n        match: \"^Adobe Premiere\"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camelcase:\n    description: operationId should use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function:\
  \ truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Parameters must have descriptions\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Parameters must have schemas\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-description:\n    description: Request bodies should have descriptions\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must define 2xx responses\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: responses\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n\
  \            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: Responses must have descriptions\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-error-401:\n    description: Operations should define 401 error response\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"401\"]\n            - required: [\"400\"]\n\n  # SCHEMAS\n  schema-description:\n    description: Component schemas should have descriptions\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-type-defined:\n    description: Schemas should define a type\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function:\
  \ truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: API must define security schemes\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: API should define global security\n    severity: warn\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET must not have request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE should not have request body\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/adobe-premiere/refs/heads/main/rules/adobe-premiere-spectral-rules.yml
tags:
- Adobe
- Automation
- Creative Cloud
- Media
- Premiere Pro
- Video Editing
- Video Production
- Spectral
- Linting
- API Governance
---
