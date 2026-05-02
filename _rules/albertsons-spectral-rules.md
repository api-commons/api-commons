---
api_specs:
- filename: albertsons-retail-media-api-openapi.yml
  format: yaml
  label: Albertsons Media Collective API
  slug: retail-media-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/albertsons/refs/heads/main/openapi/albertsons-retail-media-api-openapi.yml
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
- tags
description: Spectral linting rules defining API design standards and conventions for albertsons.
layout: rules
name: albertsons API Rules
provider_name: albertsons
provider_slug: albertsons
rule_count: 35
rules:
- description: Info title must be defined and start with "Albertsons".
  given: $.info.title
  name: info-title-required
  severity: error
- description: Info description must be defined with meaningful content.
  given: $.info.description
  name: info-description-required
  severity: error
- description: API version must be specified.
  given: $.info.version
  name: info-version-required
  severity: error
- description: Contact information should be provided.
  given: $.info.contact
  name: info-contact-required
  severity: warn
- description: All specs must use OpenAPI 3.x.
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $.servers
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Path segments must use kebab-case (lowercase with hyphens).
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not end with a trailing slash.
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Resource path segments should use plural nouns.
  given: $.paths[*]~
  name: paths-plural-resource-nouns
  severity: info
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Albertsons".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-albertsons-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete].description
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-required
  severity: error
- description: operationId must use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete].tags
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined.
  given: $.tags
  name: tags-global-defined
  severity: warn
- description: All global tags must have descriptions.
  given: $.tags[*].description
  name: tags-description-required
  severity: warn
- description: All parameters must have descriptions.
  given: $.paths[*][get,post,put,patch,delete].parameters[*].description
  name: parameter-description-required
  severity: error
- description: Query and path parameter names should use camelCase or snake_case.
  given: $.paths[*][get,post,put,patch,delete].parameters[*].name
  name: parameter-snake-case
  severity: info
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-content-json
  severity: warn
- description: Request body content should have a schema with description.
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: info
- description: Every operation must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Secured endpoints should define a 401 response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: All responses must have descriptions.
  given: $.paths[*][get,post,put,patch,delete].responses[*].description
  name: response-description-required
  severity: error
- description: Top-level schemas must have descriptions.
  given: $.components.schemas[*].description
  name: schema-description-required
  severity: warn
- description: All schemas must define a type.
  given: $.components.schemas[*].type
  name: schema-type-required
  severity: warn
- description: Schema property names should use camelCase.
  given: $.components.schemas[*].properties[*]~
  name: schema-property-camel-case
  severity: info
- description: Security schemes must be defined in components.
  given: $.components.securitySchemes
  name: security-schemes-defined
  severity: error
- description: Bearer authentication scheme should be defined.
  given: $.components.securitySchemes.bearerAuth
  name: security-bearer-auth
  severity: warn
- description: Each operation should define security requirements.
  given: $.paths[*][get,post,put,patch,delete].security
  name: security-operation-defined
  severity: warn
- description: GET operations must not have request bodies.
  given: $.paths[*].get.requestBody
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have request bodies.
  given: $.paths[*].delete.requestBody
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/albertsons-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/albertsons/refs/heads/main/rules/albertsons-spectral-rules.yml
severity_counts:
  error: 16
  hint: 0
  info: 5
  warn: 14
slug: albertsons-spectral-rules
source_filename: albertsons-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: Info title must be defined and start with \"Albertsons\".\n    severity: error\n    given: \"$.info.title\"\n    then:\n      function: truthy\n\n  info-description-required:\n    description: Info description must be defined with meaningful content.\n    severity: error\n    given: \"$.info.description\"\n    then:\n      function: truthy\n\n  info-version-required:\n    description: API version must be specified.\n    severity: error\n    given: \"$.info.version\"\n    then:\n      function: truthy\n\n  info-contact-required:\n    description: Contact information should be provided.\n    severity: warn\n    given: \"$.info.contact\"\n    then:\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: All specs must use OpenAPI 3.x.\n    severity: error\n    given: \"$.openapi\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n\
  \  servers-required:\n    description: At least one server must be defined.\n    severity: error\n    given: \"$.servers\"\n    then:\n      function: truthy\n\n  servers-https-only:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments must use kebab-case (lowercase with hyphens).\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9-{}]+)+$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not end with a trailing slash.\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  paths-plural-resource-nouns:\n    description: Resource path segments should use plural nouns.\n    severity: info\n \
  \   given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9-{}]*s[a-z0-9-{}]*|/[a-z0-9-{}]*)+$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: truthy\n\n  operation-summary-albertsons-prefix:\n    description: Operation summaries must start with \"Albertsons\".\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Albertsons\"\n\n  operation-description-required:\n    description: Every operation must have a description.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].description\"\n    then:\n      function: truthy\n\n  operation-operationid-required:\n    description: Every operation must have an operationId.\n    severity: error\n \
  \   given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: truthy\n\n  operation-operationid-camel-case:\n    description: operationId must use camelCase.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].tags\"\n    then:\n      function: truthy\n\n  # TAGS\n  tags-global-defined:\n    description: Global tags array should be defined.\n    severity: warn\n    given: \"$.tags\"\n    then:\n      function: truthy\n\n  tags-description-required:\n    description: All global tags must have descriptions.\n    severity: warn\n    given: \"$.tags[*].description\"\n    then:\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description:\
  \ All parameters must have descriptions.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*].description\"\n    then:\n      function: truthy\n\n  parameter-snake-case:\n    description: Query and path parameter names should use camelCase or snake_case.\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*].name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9_]*$\"\n\n  # REQUEST BODIES\n  request-body-content-json:\n    description: Request bodies should use application/json content type.\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      function: truthy\n\n  request-body-description:\n    description: Request body content should have a schema with description.\n    severity: info\n    given: \"$.paths[*][post,put,patch].requestBody\"\n    then:\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description:\
  \ Every operation must define at least one 2xx response.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-401-required:\n    description: Secured endpoints should define a 401 response.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: truthy\n\n  response-description-required:\n    description: All responses must have descriptions.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*].description\"\n    then:\n      function: truthy\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-description-required:\n    description: Top-level schemas must have descriptions.\n    severity: warn\n    given: \"$.components.schemas[*].description\"\n    then:\n      function: truthy\n\n  schema-type-required:\n    description: All schemas must\
  \ define a type.\n    severity: warn\n    given: \"$.components.schemas[*].type\"\n    then:\n      function: truthy\n\n  schema-property-camel-case:\n    description: Schema property names should use camelCase.\n    severity: info\n    given: \"$.components.schemas[*].properties[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  security-bearer-auth:\n    description: Bearer authentication scheme should be defined.\n    severity: warn\n    given: \"$.components.securitySchemes.bearerAuth\"\n    then:\n      function: truthy\n\n  security-operation-defined:\n    description: Each operation should define security requirements.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].security\"\n    then:\n\
  \      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have request bodies.\n    severity: error\n    given: \"$.paths[*].get.requestBody\"\n    then:\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have request bodies.\n    severity: warn\n    given: \"$.paths[*].delete.requestBody\"\n    then:\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  examples-encouraged:\n    description: Schema properties should include example values.\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/albertsons/refs/heads/main/rules/albertsons-spectral-rules.yml
tags:
- Grocery
- Retail
- Retail Media
- Advertising
- Campaigns
- Analytics
- Consumer Goods
- Food
- Pharmacy
- Spectral
- Linting
- API Governance
---
