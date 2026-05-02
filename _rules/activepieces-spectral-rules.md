---
api_specs:
- filename: activepieces.json
  format: json
  label: Activepieces API
  slug: activepieces-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/activepieces/refs/heads/main/openapi/activepieces.json
categories:
- http
- info
- openapi
- operation
- pagination
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Activepieces.
layout: rules
name: Activepieces API Rules
provider_name: Activepieces
provider_slug: activepieces
rule_count: 25
rules:
- description: API title should start with "Activepieces"
  given: $.info.title
  name: info-title-format
  severity: warn
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must include a version
  given: $.info
  name: info-version-required
  severity: error
- description: Should use OpenAPI 3.x
  given: $.openapi
  name: openapi-version
  severity: warn
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: All servers should use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: info
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summary should start with "Activepieces"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: OperationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationId-camelCase
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: List endpoints should support limit parameter
  given: $.paths[*].get.parameters[*]
  name: pagination-limit-param
  severity: info
- description: Every operation must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations should document 401 Unauthorized response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-defined
  severity: info
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: API should use Bearer authentication
  given: $.components.securitySchemes[*]
  name: security-bearer-auth
  severity: warn
- description: GET operations should not have a request body
  given: $.paths[*].get
  name: http-get-no-request-body
  severity: error
- description: DELETE operations should return 204
  given: $.paths[*].delete.responses
  name: http-delete-returns-204
  severity: info
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should define types
  given: $.components.schemas[*].properties[*]
  name: schema-properties-have-types
  severity: warn
rules_file: rules/activepieces-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/activepieces/refs/heads/main/rules/activepieces-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 4
  warn: 11
slug: activepieces-spectral-rules
source_filename: activepieces-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-format:\n    description: API title should start with \"Activepieces\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Activepieces\"\n\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must include a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description: Should use OpenAPI 3.x\n    severity: warn\n    given: $.openapi\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n\
  \      function: truthy\n\n  servers-https:\n    description: All servers should use HTTPS\n    severity: warn\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: error\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: info\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"_[a-z]\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summary should start with \"Activepieces\"\
  \n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Activepieces \"\n\n  operation-description-required:\n    description: Every operation should have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-operationId-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationId-camelCase:\n    description: OperationId should use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: casing\n      functionOptions:\n        type: camel\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given:\
  \ $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  # PAGINATION\n  pagination-limit-param:\n    description: List endpoints should support limit parameter\n    severity: info\n    given: $.paths[*].get.parameters[*]\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          properties:\n            name:\n              type: string\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have at least one 2xx response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n       \
  \     - required: ['201']\n            - required: ['204']\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-401-defined:\n    description: Operations should document 401 Unauthorized response\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: '401'\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-bearer-auth:\n    description: API should use Bearer authentication\n    severity: warn\n    given: $.components.securitySchemes[*]\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          properties:\n            scheme:\n\
  \              enum: ['bearer']\n\n  # HTTP METHOD CONVENTIONS\n  http-get-no-request-body:\n    description: GET operations should not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  http-delete-returns-204:\n    description: DELETE operations should return 204\n    severity: info\n    given: $.paths[*].delete.responses\n    then:\n      field: '204'\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Component schemas should have descriptions\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-properties-have-types:\n    description: Schema properties should define types\n    severity: warn\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: type\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/activepieces/refs/heads/main/rules/activepieces-spectral-rules.yml
tags:
- Automation
- No-Code
- Open Source
- Workflow
- AI Agents
- MCP
- Spectral
- Linting
- API Governance
---
