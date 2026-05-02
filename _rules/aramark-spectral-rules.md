---
api_specs:
- filename: marko-api.yml
  format: yaml
  label: Aramark Marko API
  slug: marko-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/aramark/refs/heads/main/openapi/marko-api.yml
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
description: Spectral linting rules defining API design standards and conventions for Aramark.
layout: rules
name: Aramark API Rules
provider_name: Aramark
provider_slug: aramark
rule_count: 21
rules:
- description: API title must start with "Aramark"
  given: $.info
  name: info-title-aramark-prefix
  severity: error
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: warn
- description: API must have a version
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
- description: Operation summaries should start with "Aramark"
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-aramark-prefix
  severity: warn
- description: All operations should have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
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
- description: All secured operations should document 401 responses
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-401-required
  severity: warn
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-properties-described
  severity: info
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: API key should be passed in the header (not query)
  given: $.components.securitySchemes[*][?(@.type=='apiKey')]
  name: security-api-key-header
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return 204
  given: $.paths[*].delete.responses
  name: delete-returns-204
  severity: info
rules_file: rules/aramark-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/aramark/refs/heads/main/rules/aramark-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 2
  warn: 6
slug: aramark-spectral-rules
source_filename: aramark-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-aramark-prefix:\n    description: API title must start with \"Aramark\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: \"^Aramark\"\n\n  info-description-required:\n    description: API must have a description\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Use OpenAPI 3.0.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Server URLs must be defined\n    severity: error\n    given: \"$\"\n    then:\n\
  \      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # OPERATIONS\n  operation-id-required:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: OperationIds should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function:\
  \ truthy\n\n  operation-summary-aramark-prefix:\n    description: Operation summaries should start with \"Aramark\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^Aramark\"\n\n  operation-description-required:\n    description: All operations should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-tags-required:\n    description: All operations must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n\
  \  response-success-required:\n    description: All operations must define a success response\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].responses\"\n    then:\n      function: truthy\n\n  response-401-required:\n    description: All secured operations should document 401 responses\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].responses\"\n    then:\n      field: \"401\"\n      function: truthy\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-properties-described:\n    description: Schema properties should have descriptions\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be\
  \ defined\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-api-key-header:\n    description: API key should be passed in the header (not query)\n    severity: error\n    given: \"$.components.securitySchemes[*][?(@.type=='apiKey')]\"\n    then:\n      field: in\n      function: enumeration\n      functionOptions:\n        values: [header]\n\n  # HTTP METHODS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-returns-204:\n    description: DELETE operations should return 204\n    severity: info\n    given: \"$.paths[*].delete.responses\"\n    then:\n      field: \"204\"\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/aramark/refs/heads/main/rules/aramark-spectral-rules.yml
tags:
- Food Services
- Facilities Management
- Uniform Services
- Data Platform
- Fortune 500
- Spectral
- Linting
- API Governance
---
