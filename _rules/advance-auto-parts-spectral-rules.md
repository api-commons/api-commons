---
api_specs:
- filename: advance-auto-parts-catalog-api-openapi.yml
  format: yaml
  label: Advance Auto Parts Catalog API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/advance-auto-parts/refs/heads/main/openapi/advance-auto-parts-catalog-api-openapi.yml
- filename: advance-auto-parts-commerce-api-openapi.yml
  format: yaml
  label: Advance Auto Parts Commerce API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/advance-auto-parts/refs/heads/main/openapi/advance-auto-parts-commerce-api-openapi.yml
categories:
- delete
- examples
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
- vehicle
description: Spectral linting rules defining API design standards and conventions for Advance Auto Parts.
layout: rules
name: Advance Auto Parts API Rules
provider_name: Advance Auto Parts
provider_slug: advance-auto-parts
rule_count: 32
rules:
- description: API title must start with "Advance Auto Parts"
  given: $.info.title
  name: info-title-aap-prefix
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must declare a version
  given: $.info
  name: info-version-required
  severity: error
- description: API should include contact information
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
- description: Servers should have descriptions
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Path segments should use lowercase and hyphens
  given: $.paths[*]~
  name: paths-lowercase-kebab
  severity: info
- description: Operations must have summaries
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Summaries should start with "Advance Auto Parts"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-aap-prefix
  severity: warn
- description: Operations must have descriptions
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Operations must have operationIds
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camelcase
  severity: warn
- description: Operations must have tags
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
- description: Operations should define 401 Unauthorized response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-auth-defined
  severity: warn
- description: Responses must have descriptions
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description
  severity: warn
- description: Schemas should define a type
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Schema property names should use camelCase
  given: $.components.schemas[*].properties[*]~
  name: schema-properties-camelcase
  severity: info
- description: API must define security schemes
  given: $.components
  name: security-schemes-defined
  severity: error
- description: API should define global security
  given: $
  name: security-global-defined
  severity: warn
- description: GET operations must not have request bodies
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return 204 No Content
  given: $.paths[*].delete.responses
  name: delete-returns-204
  severity: info
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Responses should include examples
  given: $.paths[*][get,post,put,patch,delete].responses[*].content[*]
  name: examples-encouraged
  severity: info
- description: Fitment endpoints should document year/make/model parameters
  given: $.paths[/vehicles*][get].parameters[*].name
  name: vehicle-fitment-documented
  severity: info
rules_file: rules/advance-auto-parts-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/advance-auto-parts/refs/heads/main/rules/advance-auto-parts-spectral-rules.yml
severity_counts:
  error: 16
  hint: 0
  info: 5
  warn: 11
slug: advance-auto-parts-spectral-rules
source_filename: advance-auto-parts-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-aap-prefix:\n    description: API title must start with \"Advance Auto Parts\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Advance Auto Parts\"\n\n  info-description-required:\n    description: API must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must declare a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API should include contact information\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n\
  \        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: API must define servers\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description:\n    description: Servers should have descriptions\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # PATHS\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: warn\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  paths-lowercase-kebab:\n    description: Path segments should use lowercase and hyphens\n    severity: info\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n\
  \        match: \"^/[a-z0-9{}/_-]+$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Operations must have summaries\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-aap-prefix:\n    description: Summaries should start with \"Advance Auto Parts\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Advance Auto Parts\"\n\n  operation-description-required:\n    description: Operations must have descriptions\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Operations must have operationIds\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camelcase:\n\
  \    description: operationId should use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: Operations must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Parameters must have descriptions\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Parameters must have schemas\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-description:\n    description: Request bodies should have descriptions\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody\n\
  \    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must define 2xx responses\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: responses\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-auth-defined:\n    description: Operations should define 401 Unauthorized response\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"401\"]\n            - required: [\"400\"]\n\n  response-description-required:\n    description: Responses must have descriptions\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n\
  \n  # SCHEMAS\n  schema-description:\n    description: Component schemas should have descriptions\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-type-defined:\n    description: Schemas should define a type\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  schema-properties-camelcase:\n    description: Schema property names should use camelCase\n    severity: info\n    given: $.components.schemas[*].properties[*]~\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  # SECURITY\n  security-schemes-defined:\n    description: API must define security schemes\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: API should define global security\n    severity: warn\n    given: $\n    then:\n\
  \      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have request bodies\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-returns-204:\n    description: DELETE operations should return 204 No Content\n    severity: info\n    given: $.paths[*].delete.responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          required: [\"204\"]\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then:\n      function: truthy\n\n  examples-encouraged:\n    description: Responses should include examples\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].responses[*].content[*]\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required:\
  \ [\"example\"]\n            - required: [\"examples\"]\n\n  # AUTOMOTIVE DOMAIN\n  vehicle-fitment-documented:\n    description: Fitment endpoints should document year/make/model parameters\n    severity: info\n    given: $.paths[/vehicles*][get].parameters[*].name\n    then:\n      function: enumeration\n      functionOptions:\n        values: [year, makeId, modelId, engineId, trim]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/advance-auto-parts/refs/heads/main/rules/advance-auto-parts-spectral-rules.yml
tags:
- Automotive
- E-Commerce
- Parts Catalog
- Retail
- Supply Chain
- Spectral
- Linting
- API Governance
---
