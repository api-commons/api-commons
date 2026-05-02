---
api_specs:
- filename: microsoft-power-automate-management-api.yaml
  format: yaml
  label: Power Automate Management API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/microsoft-power-automate/refs/heads/main/openapi/microsoft-power-automate-management-api.yaml
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
description: Spectral linting rules defining API design standards and conventions for Microsoft Power Automate.
layout: rules
name: Microsoft Power Automate API Rules
provider_name: Microsoft Power Automate
provider_slug: microsoft-power-automate
rule_count: 23
rules:
- description: Info object must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: Info title should start with Microsoft Power Automate
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
- description: OpenAPI version must be 3.0.x
  given: $
  name: openapi-version
  severity: error
- description: Servers array must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: operationId should be camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Operation summaries should start with Microsoft Power Automate
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: info
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Parameters must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Operations must define a success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should define a 401 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: Schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: error
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
rules_file: rules/microsoft-power-automate-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/microsoft-power-automate/refs/heads/main/rules/microsoft-power-automate-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 1
  warn: 7
slug: microsoft-power-automate-spectral-rules
source_filename: microsoft-power-automate-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: Info object must have a title\n    given: $.info\n    severity: error\n    then:\n      field: title\n      function: truthy\n\n  info-title-prefix:\n    description: Info title should start with Microsoft Power Automate\n    given: $.info.title\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Microsoft Power Automate\"\n\n  info-description-required:\n    description: Info object must have a description\n    given: $.info\n    severity: error\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must have a version\n    given: $.info\n    severity: error\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description: OpenAPI version must be 3.0.x\n    given: $\n    severity: error\n    then:\n      field: openapi\n      function: pattern\n\
  \      functionOptions:\n        match: \"^3\\\\.0\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers array must be defined\n    given: $\n    severity: error\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    given: $.servers[*].url\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    given: $.paths\n    severity: error\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Operations must have a summary\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: Operations must have a description\n   \
  \ given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n    description: Operations must have an operationId\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-camel-case:\n    description: operationId should be camelCase\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Operations must have at least one tag\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with Microsoft Power Automate\n    given: $.paths[*][get,post,put,patch,delete].summary\n\
  \    severity: info\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Microsoft Power Automate \"\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Parameters must have descriptions\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    severity: warn\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Parameters must have a schema\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    severity: error\n    then:\n      field: schema\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must define a success response\n    given: $.paths[*][get,post,put,patch,delete].responses\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"202\"]\n            -\
  \ required: [\"204\"]\n\n  response-401-required:\n    description: Operations should define a 401 response\n    given: $.paths[*][get,post,put,patch,delete].responses\n    severity: warn\n    then:\n      field: \"401\"\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Schemas should have descriptions\n    given: $.components.schemas[*]\n    severity: warn\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-global-defined:\n    description: Global security must be defined\n    given: $\n    severity: error\n    then:\n      field: security\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes must be defined\n    given: $.components\n    severity: error\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    given: $.paths[*].get\n    severity: error\n\
  \    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body\n    given: $.paths[*].delete\n    severity: warn\n    then:\n      field: requestBody\n      function: falsy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/microsoft-power-automate/refs/heads/main/rules/microsoft-power-automate-spectral-rules.yml
tags:
- Automation
- Business Process
- Integration
- Low-Code
- Microsoft
- Power Platform
- RPA
- Workflow
- Spectral
- Linting
- API Governance
---
