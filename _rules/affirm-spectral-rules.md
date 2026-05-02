---
api_specs:
- filename: affirm-direct-api-openapi.yml
  format: yaml
  label: Affirm Direct API
  slug: direct-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/affirm/refs/heads/main/openapi/affirm-direct-api-openapi.yml
- filename: affirm-checkout-openapi.yml
  format: yaml
  label: Affirm Checkout API
  slug: checkout-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/affirm/refs/heads/main/openapi/affirm-checkout-openapi.yml
- filename: affirm-transactions-openapi.yml
  format: yaml
  label: Affirm Transactions API
  slug: transactions-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/affirm/refs/heads/main/openapi/affirm-transactions-openapi.yml
- filename: affirm-promos-openapi.yml
  format: yaml
  label: Affirm Promos API
  slug: promos-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/affirm/refs/heads/main/openapi/affirm-promos-openapi.yml
- filename: affirm-disputes-openapi.yml
  format: yaml
  label: Affirm Disputes API
  slug: disputes-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/affirm/refs/heads/main/openapi/affirm-disputes-openapi.yml
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
- tag
description: Spectral linting rules defining API design standards and conventions for affirm.
layout: rules
name: affirm API Rules
provider_name: affirm
provider_slug: affirm
rule_count: 35
rules:
- description: API title must be present and start with "Affirm"
  given: $.info
  name: info-title-required
  severity: error
- description: API title must start with "Affirm"
  given: $.info.title
  name: info-title-affirm-prefix
  severity: warn
- description: API info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be present
  given: $.info
  name: info-version-required
  severity: error
- description: Contact information should be provided
  given: $.info
  name: info-contact-required
  severity: warn
- description: OpenAPI version must be 3.x
  given: $
  name: openapi-version
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Server entries should have descriptions
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Affirm"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-affirm-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: OperationIds should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined
  given: $
  name: tag-global-defined
  severity: warn
- description: Tags should have descriptions
  given: $.tags[*]
  name: tag-description
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Parameters must have a schema with a type
  given: $.paths[*][get,post,put,patch,delete].parameters[*].schema
  name: parameter-schema-type
  severity: error
- description: Request bodies should have descriptions
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: warn
- description: Request bodies should include application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must have a 2xx success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All response objects must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations using auth should document 401 responses
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-defined
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description
  severity: warn
- description: Schema property names should use snake_case
  given: $.components.schemas[*].properties[*]~
  name: schema-properties-snake-case
  severity: info
- description: Schema objects should have a type defined
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security should be defined
  given: $
  name: security-global-defined
  severity: warn
- description: GET operations must not have request bodies
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have request bodies
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have examples for better documentation
  given: $.paths[*][get,post,put,patch,delete].responses[*].content.application/json
  name: operation-examples-encouraged
  severity: info
rules_file: rules/affirm-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/affirm/refs/heads/main/rules/affirm-spectral-rules.yml
severity_counts:
  error: 16
  hint: 0
  info: 2
  warn: 17
slug: affirm-spectral-rules
source_filename: affirm-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: API title must be present and start with \"Affirm\"\n    severity: error\n    given: \"$.info\"\n    then:\n      - field: title\n        function: truthy\n  info-title-affirm-prefix:\n    description: API title must start with \"Affirm\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Affirm\"\n  info-description-required:\n    description: API info must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: API version must be present\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n  info-contact-required:\n    description: Contact information should be provided\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\
  \n  # OPENAPI VERSION\n  openapi-version:\n    description: OpenAPI version must be 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n  servers-https:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  servers-description:\n    description: Server entries should have descriptions\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n\
  \      functionOptions:\n        match: \"^(/[a-z0-9{}-]+)+$\"\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: error\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n  operation-summary-affirm-prefix:\n    description: Operation summaries must start with \"Affirm\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Affirm\"\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function:\
  \ truthy\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-operationid-camel-case:\n    description: OperationIds should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tag-global-defined:\n    description: Global tags array should be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n  tag-description:\n    description: Tags should have descriptions\n    severity: warn\n\
  \    given: \"$.tags[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have descriptions\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n  parameter-schema-type:\n    description: Parameters must have a schema with a type\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*].schema\"\n    then:\n      field: type\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-description:\n    description: Request bodies should have descriptions\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody\"\n    then:\n      field: description\n      function: truthy\n  request-body-json-content:\n    description: Request bodies should include application/json content type\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\
  \n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have a 2xx success response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n  response-description-required:\n    description: All response objects must have descriptions\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n  response-401-defined:\n    description: Operations using auth should document 401 responses\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function:\
  \ schema\n      functionOptions:\n        schema:\n          type: object\n          required: [\"401\"]\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-description:\n    description: Top-level schemas should have descriptions\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n  schema-properties-snake-case:\n    description: Schema property names should use snake_case\n    severity: info\n    given: \"$.components.schemas[*].properties[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_]*$\"\n  schema-type-defined:\n    description: Schema objects should have a type defined\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n\
  \      function: truthy\n  security-global-defined:\n    description: Global security should be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have request bodies\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n  delete-no-request-body:\n    description: DELETE operations should not have request bodies\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n  operation-examples-encouraged:\n    description: Operations should have examples for better documentation\n    severity:\
  \ info\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*].content.application/json\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"example\"]\n            - required: [\"examples\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/affirm/refs/heads/main/rules/affirm-spectral-rules.yml
tags:
- Spectral
- Linting
- API Governance
---
