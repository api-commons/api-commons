---
api_specs:
- filename: 3m-partner-supplier-api-openapi.yml
  format: yaml
  label: 3M Partner and Supplier API
  slug: partner-supplier-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/3m/refs/heads/main/openapi/3m-partner-supplier-api-openapi.yml
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
description: Spectral linting rules defining API design standards and conventions for 3M.
layout: rules
name: 3M API Rules
provider_name: 3M
provider_slug: 3m
rule_count: 32
rules:
- description: API info title should follow "3M ..." pattern.
  given: $.info.title
  name: info-title-pattern
  severity: warn
- description: API info description must be present and at least 50 characters.
  given: $.info
  name: info-description-required
  severity: warn
- description: API version must be defined.
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x.
  given: $
  name: openapi-version-3
  severity: error
- description: Servers array must be defined and non-empty.
  given: $
  name: servers-must-be-defined
  severity: error
- description: Production server URLs must use HTTPS.
  given: $.servers[*]
  name: servers-https-required
  severity: error
- description: Each server must have a description.
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Path segments should use kebab-case or camelCase, not underscores.
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not end with a trailing slash.
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every summary should start with "3M".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: OperationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Global tags must have descriptions.
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Parameters should include example values.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-example-encouraged
  severity: info
- description: Request bodies should have a description.
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: warn
- description: Every operation must define at least one success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Authenticated APIs must define 401 Unauthorized response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: error
- description: Component schemas must have descriptions.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schemas should define a type.
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Schema properties should have descriptions.
  given: $.components.schemas[*].properties[*]
  name: schema-properties-described
  severity: info
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: schema-properties-examples
  severity: info
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security should be defined.
  given: $
  name: security-global-defined
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty.
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/3m-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/3m/refs/heads/main/rules/3m-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 3
  warn: 16
slug: 3m-spectral-rules
source_filename: 3m-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-pattern:\n    description: API info title should follow \"3M ...\" pattern.\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3M \"\n\n  info-description-required:\n    description: API info description must be present and at least 50 characters.\n    severity: warn\n    given: $.info\n    then:\n      field: description\n      function: minLength\n      functionOptions:\n        value: 50\n\n  info-version-required:\n    description: API version must be defined.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.x.\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-must-be-defined:\n    description: Servers array\
  \ must be defined and non-empty.\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-required:\n    description: Production server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*]\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description-required:\n    description: Each server must have a description.\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case or camelCase, not underscores.\n    severity: warn\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"_[a-z]\"\n\n  paths-no-trailing-slash:\n    description: Paths must not end with a trailing slash.\n    severity: warn\n    given: $.paths\n    then:\n      function: pattern\n \
  \     functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: Every operation should have a description.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-summary-prefix:\n    description: Every summary should start with \"3M\".\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3M \"\n\n  operation-operationid-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-camelcase:\n\
  \    description: OperationId should use camelCase.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tag-description-required:\n    description: Global tags must have descriptions.\n    severity: warn\n    given: $.tags[*]\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Every parameter must have a schema.\n    severity:\
  \ error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  parameter-example-encouraged:\n    description: Parameters should include example values.\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: example\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-description:\n    description: Request bodies should have a description.\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must define at least one success response.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-description-required:\n    description: Every\
  \ response must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-401-required:\n    description: Authenticated APIs must define 401 Unauthorized response.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            '401':\n              type: object\n\n  # SCHEMAS\n  schema-description-required:\n    description: Component schemas must have descriptions.\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-type-required:\n    description: Schemas should define a type.\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  schema-properties-described:\n    description: Schema\
  \ properties should have descriptions.\n    severity: info\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-properties-examples:\n    description: Schema properties should include example values.\n    severity: info\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: example\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: Global security should be defined.\n    severity: warn\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n \
  \     function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body.\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty.\n    severity: warn\n    given: $..description\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/3m/refs/heads/main/rules/3m-spectral-rules.yml
tags:
- Industrial
- Manufacturing
- Supply Chain
- Spectral
- Linting
- API Governance
---
