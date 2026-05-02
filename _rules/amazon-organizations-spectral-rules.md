---
api_specs:
- filename: Welcome.html
  format: yaml
  label: AWS Organizations API
  slug: ''
  spec_type: OpenAPI
  url: https://docs.aws.amazon.com/organizations/latest/APIReference/Welcome.html
categories:
- get
- info
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- server
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Organizations.
layout: rules
name: Amazon Organizations API Rules
provider_name: Amazon Organizations
provider_slug: amazon-organizations
rule_count: 21
rules:
- description: API title should start with "Amazon Organizations"
  given: $.info.title
  name: info-title-format
  severity: warn
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: OpenAPI version should be 3.x
  given: $.openapi
  name: openapi-version-3
  severity: warn
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: server-https-required
  severity: error
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths should not have a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Amazon Organizations"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-company-prefix
  severity: warn
- description: Operations must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: Operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: OperationIds should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: warn
- description: Parameters must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Operations must have a success response (2xx)
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Response objects must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Schemas should define a type
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Security schemes must be defined in components
  given: $.components
  name: security-scheme-defined
  severity: error
- description: GET operations should not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Operations should include examples
  given: $.paths[*][get,post,put,patch,delete].responses[*].content[*]
  name: operation-examples-encouraged
  severity: info
rules_file: rules/amazon-organizations-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-organizations/refs/heads/main/rules/amazon-organizations-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 1
  warn: 10
slug: amazon-organizations-spectral-rules
source_filename: amazon-organizations-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [[spectral:oas, recommended]]\n\nrules:\n  # INFO / METADATA\n  info-title-format:\n    description: API title should start with \"Amazon Organizations\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Organizations\"\n\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: OpenAPI version should be 3.x\n    severity: warn\n    given: \"$.openapi\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: Servers must be defined\n\
  \    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  server-https-required:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9][a-z0-9-]*|/\\\\{[a-zA-Z][a-zA-Z0-9_]*\\\\})*$\"\n\n  paths-no-trailing-slash:\n    description: Paths should not have a trailing slash\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n\
  \      field: summary\n      function: truthy\n\n  operation-summary-company-prefix:\n    description: Operation summaries should start with \"Amazon Organizations\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Organizations\"\n\n  operation-description-required:\n    description: Operations must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: OperationIds should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n\
  \      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Operations must have at least one tag\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Parameters must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must have a success response (2xx)\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"202\"]\n            - required: [\"204\"\
  ]\n\n  response-description-required:\n    description: Response objects must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-type-required:\n    description: Schemas should define a type\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-scheme-defined:\n    description: Security schemes must be defined in components\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations should not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  operation-examples-encouraged:\n    description: Operations should include\
  \ examples\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*].content[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"example\"]\n            - required: [\"examples\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-organizations/refs/heads/main/rules/amazon-organizations-spectral-rules.yml
tags:
- Account Management
- Consolidated Billing
- Governance
- Multi-Account
- Organizations
- Policies
- Spectral
- Linting
- API Governance
---
