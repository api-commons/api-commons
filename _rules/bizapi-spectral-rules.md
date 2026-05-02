---
api_specs:
- filename: bizapi-business-intelligence-api-openapi.yml
  format: yaml
  label: BizAPI Business Intelligence API
  slug: bizapi
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/bizapi/refs/heads/main/openapi/bizapi-business-intelligence-api-openapi.yml
categories:
- examples
- get
- info
- 'no'
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
- tags
description: Spectral linting rules defining API design standards and conventions for BizAPI.
layout: rules
name: BizAPI API Rules
provider_name: BizAPI
provider_slug: bizapi
rule_count: 33
rules:
- description: API title must start with "BizAPI"
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
- description: Info object should have contact information
  given: $.info
  name: info-contact-required
  severity: warn
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
- description: Path segments must use kebab-case or lowercase
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "BizAPI"
  given: $.paths[*][get,post,put,patch,delete].summary
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
- description: operationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must define a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should have a description
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: info
- description: Request bodies must support application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json
  severity: warn
- description: Every operation must define at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Operations using authentication should define a 401 response
  given: $.paths[*][post]
  name: response-401-defined
  severity: warn
- description: Operations should define a 429 rate-limit response
  given: $.paths[*][post]
  name: response-429-defined
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
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-properties-description
  severity: info
- description: At least one security scheme must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: warn
- description: POST operations should have a request body
  given: $.paths[*].post
  name: post-has-request-body
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should have examples
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
- description: Global tags array should be defined
  given: $
  name: tags-global-defined
  severity: info
rules_file: rules/bizapi-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/bizapi/refs/heads/main/rules/bizapi-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 5
  warn: 15
slug: bizapi-spectral-rules
source_filename: bizapi-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# BizAPI Spectral Ruleset\n# Enforces conventions observed in the BizAPI Business Intelligence API OpenAPI specification.\n\nrules:\n\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"BizAPI\"\n    message: 'Info title must start with \"BizAPI\" — got \"{{value}}\"'\n    severity: warn\n    given: '$.info.title'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^BizAPI'\n\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: '$.info'\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must have a version\n    severity: error\n    given: '$.info'\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Info object should have contact information\n    severity: warn\n    given: '$.info'\n    then:\n      field: contact\n      function: truthy\n\
  \n  # OPENAPI VERSION\n  openapi-version:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: '$'\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: '^3\\.'\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined\n    severity: error\n    given: '$'\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: '$.servers[*].url'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments must use kebab-case or lowercase\n    severity: warn\n    given: '$.paths[*]~'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^(/[a-z0-9-]+)+$'\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: warn\n    given: '$.paths[*]~'\n\
  \    then:\n      function: pattern\n      functionOptions:\n        notMatch: '/$'\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete,options,head]'\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries must start with \"BizAPI\"\n    message: 'Operation summary must start with \"BizAPI\" — got \"{{value}}\"'\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].summary'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^BizAPI'\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete,options,head]'\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n\
  \    severity: error\n    given: '$.paths[*][get,post,put,patch,delete,options,head]'\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId must use camelCase\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].operationId'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]+$'\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete,options,head]'\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].parameters[*]'\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Every parameter must define a schema\n    severity: error\n\
  \    given: '$.paths[*][get,post,put,patch,delete].parameters[*]'\n    then:\n      field: schema\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-description:\n    description: Request bodies should have a description\n    severity: info\n    given: '$.paths[*][post,put,patch].requestBody'\n    then:\n      field: description\n      function: truthy\n\n  request-body-json:\n    description: Request bodies must support application/json content type\n    severity: warn\n    given: '$.paths[*][post,put,patch].requestBody.content'\n    then:\n      field: application/json\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must define at least one 2xx response\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: responses\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          patternProperties:\n            '^2[0-9]{2}$': {}\n        \
  \  minProperties: 1\n\n  response-401-defined:\n    description: Operations using authentication should define a 401 response\n    severity: warn\n    given: '$.paths[*][post]'\n    then:\n      field: responses\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: ['401']\n\n  response-429-defined:\n    description: Operations should define a 429 rate-limit response\n    severity: info\n    given: '$.paths[*][post]'\n    then:\n      field: responses\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: ['429']\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].responses[*]'\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-property-snake-case:\n    description: Schema property names must use snake_case\n    severity:\
  \ warn\n    given: '$.components.schemas[*].properties[*]~'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-z0-9_]*$'\n\n  schema-description-required:\n    description: Top-level schemas must have a description\n    severity: warn\n    given: '$.components.schemas[*]'\n    then:\n      field: description\n      function: truthy\n\n  schema-properties-description:\n    description: Schema properties should have descriptions\n    severity: info\n    given: '$.components.schemas[*].properties[*]'\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: At least one security scheme must be defined in components\n    severity: error\n    given: '$.components'\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: Global security must be defined\n    severity: warn\n    given: '$'\n    then:\n      field: security\n      function:\
  \ truthy\n\n  # HTTP METHOD CONVENTIONS\n  post-has-request-body:\n    description: POST operations should have a request body\n    severity: warn\n    given: '$.paths[*].post'\n    then:\n      field: requestBody\n      function: truthy\n\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: '$.paths[*].get'\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: '$..description'\n    then:\n      function: pattern\n      functionOptions:\n        match: '.+'\n\n  examples-encouraged:\n    description: Schema properties should have examples\n    severity: info\n    given: '$.components.schemas[*].properties[*]'\n    then:\n      field: example\n      function: truthy\n\n  tags-global-defined:\n    description: Global tags array should be defined\n    severity: info\n    given: '$'\n\
  \    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/bizapi/refs/heads/main/rules/bizapi-spectral-rules.yml
tags:
- Business Intelligence
- Company Data
- CRM
- Firmographic Data
- NAICS
- SIC
- Spectral
- Linting
- API Governance
---
