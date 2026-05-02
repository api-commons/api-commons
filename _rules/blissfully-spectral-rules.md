---
api_specs:
- filename: blissfully-vendr-catalog-api-openapi.yaml
  format: yaml
  label: Vendr Catalog API
  slug: vendr-catalog-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/blissfully/refs/heads/main/openapi/blissfully-vendr-catalog-api-openapi.yaml
categories:
- get
- info
- list
- openapi
- operation
- parameter
- paths
- post
- request
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Blissfully.
layout: rules
name: Blissfully API Rules
provider_name: Blissfully
provider_slug: blissfully
rule_count: 27
rules:
- description: API title must start with "Vendr"
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
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Path segments must use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Vendr"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Pagination parameter names should use snake_case
  given: $.paths[*][get].parameters[*].name
  name: parameter-pagination-snake-case
  severity: info
- description: Request bodies must support application/json
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json
  severity: warn
- description: Every operation must define a 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Operations should define a 401 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-defined
  severity: warn
- description: Operations should define a 429 rate limit response
  given: $.paths[*][get,post].responses
  name: response-429-rate-limit
  severity: info
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Schema property names must use snake_case
  given: $.components.schemas[*].properties[*]~
  name: schema-property-snake-case
  severity: warn
- description: Top-level schemas must have a description
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: At least one security scheme must be defined
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
- description: POST operations should have a request body
  given: $.paths[*].post
  name: post-has-request-body
  severity: warn
- description: List operations should support limit and offset pagination
  given: $.paths[*].get
  name: list-operations-pagination
  severity: info
rules_file: rules/blissfully-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/blissfully/refs/heads/main/rules/blissfully-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 3
  warn: 13
slug: blissfully-spectral-rules
source_filename: blissfully-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Vendr/Blissfully API Spectral Ruleset\n# Enforces conventions observed in the Vendr Catalog API OpenAPI specification.\n\nrules:\n\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"Vendr\"\n    severity: warn\n    given: '$.info.title'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^Vendr'\n\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: '$.info'\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must have a version\n    severity: error\n    given: '$.info'\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: '$'\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: '^3\\.'\n\n  # SERVERS\n  servers-defined:\n\
  \    description: At least one server must be defined\n    severity: error\n    given: '$'\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: '$.servers[*].url'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments must use kebab-case\n    severity: warn\n    given: '$.paths[*]~'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^(/[a-z0-9-]+|\\{[a-z_]+\\})+$'\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries must start with \"Vendr\"\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].summary'\n\
  \    then:\n      function: pattern\n      functionOptions:\n        match: '^Vendr'\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId must use camelCase\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].operationId'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]+$'\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: tags\n      function:\
  \ truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].parameters[*]'\n    then:\n      field: description\n      function: truthy\n\n  parameter-pagination-snake-case:\n    description: Pagination parameter names should use snake_case\n    severity: info\n    given: '$.paths[*][get].parameters[*].name'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-z0-9_]*$'\n\n  # REQUEST BODIES\n  request-body-json:\n    description: Request bodies must support application/json\n    severity: warn\n    given: '$.paths[*][post,put,patch].requestBody.content'\n    then:\n      field: application/json\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must define a 2xx response\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: responses\n\
  \      function: truthy\n\n  response-401-defined:\n    description: Operations should define a 401 response\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].responses'\n    then:\n      field: '401'\n      function: truthy\n\n  response-429-rate-limit:\n    description: Operations should define a 429 rate limit response\n    severity: info\n    given: '$.paths[*][get,post].responses'\n    then:\n      field: '429'\n      function: truthy\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].responses[*]'\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-property-snake-case:\n    description: Schema property names must use snake_case\n    severity: warn\n    given: '$.components.schemas[*].properties[*]~'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-z0-9_]*$'\n\n  schema-description-required:\n\
  \    description: Top-level schemas must have a description\n    severity: warn\n    given: '$.components.schemas[*]'\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: At least one security scheme must be defined\n    severity: error\n    given: '$.components'\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: Global security must be defined\n    severity: warn\n    given: '$'\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: '$.paths[*].get'\n    then:\n      field: requestBody\n      function: falsy\n\n  post-has-request-body:\n    description: POST operations should have a request body\n    severity: warn\n    given: '$.paths[*].post'\n    then:\n      field: requestBody\n      function: truthy\n\
  \n  # PAGINATION\n  list-operations-pagination:\n    description: List operations should support limit and offset pagination\n    severity: info\n    given: '$.paths[*].get'\n    then:\n      field: parameters\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/blissfully/refs/heads/main/rules/blissfully-spectral-rules.yml
tags:
- Procurement
- SaaS Discovery
- SaaS Management
- Software Procurement
- Spend Optimization
- Vendor Management
- Spectral
- Linting
- API Governance
---
