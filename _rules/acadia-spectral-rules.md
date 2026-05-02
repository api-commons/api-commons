---
api_specs:
- filename: acadia-platform.yaml
  format: yaml
  label: Acadia Platform API
  slug: acadia-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/acadia/refs/heads/main/openapi/acadia-platform.yaml
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
description: Spectral linting rules defining API design standards and conventions for Acadia.
layout: rules
name: Acadia API Rules
provider_name: Acadia
provider_slug: acadia
rule_count: 25
rules:
- description: Info title must start with "Acadia"
  given: $.info
  name: info-title-acadia-prefix
  severity: error
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: error
- description: Info version must be present
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.0.x
  given: $
  name: openapi-version-3
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https-required
  severity: error
- description: Path segments must use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: Operation summaries must start with "Acadia"
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: List endpoints should support page parameter
  given: $.paths[*].get.parameters[?(@.name == "page")]
  name: parameter-pagination-page
  severity: info
- description: List endpoints should support limit parameter
  given: $.paths[*].get.parameters[?(@.name == "limit")]
  name: parameter-pagination-limit
  severity: info
- description: Every operation must have a 2xx success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Protected operations should document 401 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: All responses must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Component schemas must have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Schema properties should have example values
  given: $.components.schemas[*].properties[*]
  name: schema-property-example
  severity: info
- description: Security schemes must be defined
  given: $
  name: security-schemes-required
  severity: error
- description: Acadia uses Bearer JWT authentication
  given: $.components.securitySchemes[*][?(@.type == "http")]
  name: security-bearer-jwt
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return 200 or 204
  given: $.paths[*].delete.responses
  name: delete-returns-200-or-204
  severity: warn
rules_file: rules/acadia-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/acadia/refs/heads/main/rules/acadia-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 4
  warn: 8
slug: acadia-spectral-rules
source_filename: acadia-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-acadia-prefix:\n    description: Info title must start with \"Acadia\"\n    severity: error\n    given: '$.info'\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: '^Acadia'\n\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: '$.info'\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info version must be present\n    severity: error\n    given: '$.info'\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.0.x\n    severity: error\n    given: '$'\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: '^3\\.0\\.'\n\n  # SERVERS\n  servers-https-required:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: '$.servers[*]'\n\
  \    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: '^https://'\n\n  # PATHS\n  paths-kebab-case:\n    description: Path segments must use kebab-case\n    severity: warn\n    given: '$.paths'\n    then:\n      field: '@key'\n      function: pattern\n      functionOptions:\n        match: '^(\\/[a-z0-9_\\-\\{\\}]*)*$'\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: warn\n    given: '$.paths'\n    then:\n      field: '@key'\n      function: pattern\n      functionOptions:\n        notMatch: '.+\\/$'\n\n  # OPERATIONS\n  operation-summary-prefix:\n    description: Operation summaries must start with \"Acadia\"\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: '^Acadia'\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n\
  \    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId must use camelCase\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]+$'\n\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Parameters must have descriptions\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].parameters[*]'\n\
  \    then:\n      field: description\n      function: truthy\n\n  parameter-pagination-page:\n    description: List endpoints should support page parameter\n    severity: info\n    given: '$.paths[*].get.parameters[?(@.name == \"page\")]'\n    then:\n      field: schema.type\n      function: enumeration\n      functionOptions:\n        values:\n          - integer\n\n  parameter-pagination-limit:\n    description: List endpoints should support limit parameter\n    severity: info\n    given: '$.paths[*].get.parameters[?(@.name == \"limit\")]'\n    then:\n      field: schema.type\n      function: enumeration\n      functionOptions:\n        values:\n          - integer\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have a 2xx success response\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].responses'\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n\
  \            - required: ['201']\n            - required: ['204']\n\n  response-401-required:\n    description: Protected operations should document 401 response\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].responses'\n    then:\n      field: '401'\n      function: truthy\n\n  response-description-required:\n    description: All responses must have descriptions\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].responses[*]'\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Component schemas must have descriptions\n    severity: warn\n    given: '$.components.schemas[*]'\n    then:\n      field: description\n      function: truthy\n\n  schema-property-description:\n    description: Schema properties should have descriptions\n    severity: info\n    given: '$.components.schemas[*].properties[*]'\n    then:\n      field: description\n      function: truthy\n\n  schema-property-example:\n\
  \    description: Schema properties should have example values\n    severity: info\n    given: '$.components.schemas[*].properties[*]'\n    then:\n      field: example\n      function: truthy\n\n  # SECURITY\n  security-schemes-required:\n    description: Security schemes must be defined\n    severity: error\n    given: '$'\n    then:\n      field: components.securitySchemes\n      function: truthy\n\n  security-bearer-jwt:\n    description: Acadia uses Bearer JWT authentication\n    severity: warn\n    given: '$.components.securitySchemes[*][?(@.type == \"http\")]'\n    then:\n      field: scheme\n      function: enumeration\n      functionOptions:\n        values:\n          - bearer\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: '$.paths[*].get'\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-returns-200-or-204:\n    description: DELETE operations should return\
  \ 200 or 204\n    severity: warn\n    given: '$.paths[*].delete.responses'\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['204']\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/acadia/refs/heads/main/rules/acadia-spectral-rules.yml
tags:
- Connected Worker
- Knowledge Management
- Manufacturing
- Skills Management
- Training
- Workforce Development
- Spectral
- Linting
- API Governance
---
