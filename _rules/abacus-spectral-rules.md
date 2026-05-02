---
api_specs:
- filename: abacus-api-openapi.yaml
  format: yaml
  label: Abacus API
  slug: abacus-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/openapi/abacus-api-openapi.yaml
categories:
- delete
- examples
- get
- info
- microcks
- 'no'
- openapi
- operation
- pagination
- parameter
- paths
- request
- response
- schema
- security
- servers
- tag
description: Spectral linting rules defining API design standards and conventions for Abacus.
layout: rules
name: Abacus API Rules
provider_name: Abacus
provider_slug: abacus
rule_count: 39
rules:
- description: API info must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: API title should start with "Abacus"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: API info should have contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Should use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: warn
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Path segments should use kebab-case or snake_case with underscores
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths should not have trailing slashes
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Abacus"
  given: $.paths[*][get,post,put,patch,delete,options,head].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete,options,head].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-tags-required
  severity: error
- description: Tags used in operations should be defined at the global level
  given: $.tags
  name: tag-global-defined
  severity: warn
- description: Global tags should have descriptions
  given: $.tags[*]
  name: tag-description
  severity: info
- description: All parameters must have a description
  given: $..parameters[*]
  name: parameter-description-required
  severity: warn
- description: Parameter names should use snake_case
  given: $.paths[*][*].parameters[*].name
  name: parameter-snake-case
  severity: warn
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-content-json
  severity: info
- description: Operations must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Endpoints should document 401 Unauthorized responses
  given: $.paths[*][get,post,put,delete].responses
  name: response-401-for-auth
  severity: warn
- description: Endpoints with path parameters should document 404 responses
  given: $.paths[*][get,put,delete].responses
  name: response-404-for-resource-endpoints
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Schema property names should use snake_case
  given: $.components.schemas[*].properties
  name: schema-property-snake-case
  severity: warn
- description: Security schemes should be defined in components
  given: $.components.securitySchemes
  name: security-schemes-defined
  severity: error
- description: Security schemes should have descriptions
  given: $.components.securitySchemes[*]
  name: security-scheme-description
  severity: warn
- description: Global security should be defined
  given: $
  name: security-global-defined
  severity: warn
- description: OAuth2 scopes should be defined
  given: $.components.securitySchemes[?(@.type == 'oauth2')]
  name: security-oauth2-scopes
  severity: info
- description: GET operations should not have request bodies
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have request bodies
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions should not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should have examples for better DX
  given: $.components.schemas[*].properties[*]
  name: examples-on-schemas
  severity: info
- description: Operations should have x-microcks-operation for mock compatibility
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
- description: Paginated endpoints should use standard page/per_page parameters
  given: $.paths[*].get.parameters[*].name
  name: pagination-params-standard
  severity: info
rules_file: rules/abacus-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/rules/abacus-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 7
  warn: 19
slug: abacus-spectral-rules
source_filename: abacus-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: API info must have a title\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-title-prefix:\n    description: API title should start with \"Abacus\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Abacus\"\n\n  info-description-required:\n    description: API info must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API info must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API info should have contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n\
  \  openapi-version-3:\n    description: Should use OpenAPI 3.x\n    severity: warn\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description:\n    description: Each server should have a description\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case or snake_case with underscores\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function:\
  \ pattern\n      functionOptions:\n        match: \"^(\\\\/([a-z0-9_{}/-]+))*\\\\/?$\"\n\n  paths-no-trailing-slash:\n    description: Paths should not have trailing slashes\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"Abacus\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,options,head].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Abacus\"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\
  \n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,options,head].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tag-global-defined:\n    description: Tags used in operations should be defined at the global level\n    severity: warn\n    given: \"$.tags\"\n    then:\n      function: truthy\n\
  \n  tag-description:\n    description: Global tags should have descriptions\n    severity: info\n    given: \"$.tags[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description\n    severity: warn\n    given: \"$..parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-snake-case:\n    description: Parameter names should use snake_case\n    severity: warn\n    given: \"$.paths[*][*].parameters[*].name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_]*$\"\n\n  # REQUEST BODIES\n  request-body-content-json:\n    description: Request bodies should use application/json content type\n    severity: info\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  #\
  \ RESPONSES\n  response-success-required:\n    description: Operations must have at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses\n      function: truthy\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-401-for-auth:\n    description: Endpoints should document 401 Unauthorized responses\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete].responses\"\n    then:\n      function: truthy\n\n  response-404-for-resource-endpoints:\n    description: Endpoints with path parameters should document 404 responses\n    severity: warn\n    given: \"$.paths[*][get,put,delete].responses\"\n    then:\n      function: truthy\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-description-recommended:\n    description: Top-level schemas\
  \ should have descriptions\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-property-description:\n    description: Schema properties should have descriptions\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-property-snake-case:\n    description: Schema property names should use snake_case\n    severity: warn\n    given: \"$.components.schemas[*].properties\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes should be defined in components\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  security-scheme-description:\n    description: Security schemes should have descriptions\n    severity: warn\n    given: \"$.components.securitySchemes[*]\"\
  \n    then:\n      field: description\n      function: truthy\n\n  security-global-defined:\n    description: Global security should be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: security\n      function: truthy\n\n  security-oauth2-scopes:\n    description: OAuth2 scopes should be defined\n    severity: info\n    given: \"$.components.securitySchemes[?(@.type == 'oauth2')]\"\n    then:\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations should not have request bodies\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have request bodies\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions should not be empty strings\n    severity:\
  \ error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"^\\\\s*$\"\n\n  examples-on-schemas:\n    description: Schema properties should have examples for better DX\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: example\n      function: truthy\n\n  microcks-operation-extension:\n    description: Operations should have x-microcks-operation for mock compatibility\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n\n  pagination-params-standard:\n    description: Paginated endpoints should use standard page/per_page parameters\n    severity: info\n    given: \"$.paths[*].get.parameters[*].name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(page|per_page|cursor|limit|offset|sort|order|status|from_date|to_date|member_id|[a-z_]+)$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/rules/abacus-spectral-rules.yml
tags:
- Accounting
- Expense Management
- Finance
- Reimbursement
- Spectral
- Linting
- API Governance
---
