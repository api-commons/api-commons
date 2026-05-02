---
api_specs:
- filename: arcbest-api.yaml
  format: yaml
  label: ArcBest API
  slug: arcbest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/arcbest/refs/heads/main/openapi/arcbest-api.yaml
categories:
- delete
- get
- info
- openapi
- operation
- parameter
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for ArcBest.
layout: rules
name: ArcBest API Rules
provider_name: ArcBest
provider_slug: arcbest
rule_count: 18
rules:
- description: API title must start with "ArcBest"
  given: $.info
  name: info-title-arcbest-prefix
  severity: error
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: warn
- description: API must specify a version
  given: $.info
  name: info-version-required
  severity: error
- description: Use OpenAPI 3.0.x
  given: $
  name: openapi-version-3
  severity: error
- description: Server URLs must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: OperationIds should use camelCase
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-camel-case
  severity: warn
- description: All operations must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "ArcBest"
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-prefix
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: error
- description: All parameters must have a description
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All operations must define a success response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: All secured endpoints should document 401 responses
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-401-secured
  severity: warn
- description: Schema properties should define a type
  given: $.components.schemas[*].properties[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return 204
  given: $.paths[*].delete.responses
  name: delete-returns-204
  severity: info
rules_file: rules/arcbest-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/arcbest/refs/heads/main/rules/arcbest-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 1
  warn: 6
slug: arcbest-spectral-rules
source_filename: arcbest-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-arcbest-prefix:\n    description: API title must start with \"ArcBest\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: \"^ArcBest\"\n  info-description-required:\n    description: API must have a description\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: API must specify a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n  openapi-version-3:\n    description: Use OpenAPI 3.0.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n  servers-defined:\n    description: Server URLs must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n  servers-https:\n\
  \    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  operation-id-required:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-id-camel-case:\n    description: OperationIds should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n  operation-summary-prefix:\n    description: Operation summaries should start with\
  \ \"ArcBest\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^ArcBest\"\n  operation-tags-required:\n    description: All operations must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n  parameter-description-required:\n    description: All parameters must have a description\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n  response-success-required:\n    description: All operations must define a success response\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].responses\"\n    then:\n      function: truthy\n  response-401-secured:\n    description: All secured endpoints should document 401 responses\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].responses\"\
  \n    then:\n      field: \"401\"\n      function: truthy\n  schema-type-defined:\n    description: Schema properties should define a type\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [type]\n            - required: [$ref]\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n  delete-returns-204:\n    description: DELETE operations should return 204\n    severity: info\n    given: \"$.paths[*].delete.responses\"\n    then:\n      field: \"204\"\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/arcbest/refs/heads/main/rules/arcbest-spectral-rules.yml
tags:
- Logistics
- Freight
- LTL
- Supply Chain
- Shipping
- Transportation
- Spectral
- Linting
- API Governance
---
