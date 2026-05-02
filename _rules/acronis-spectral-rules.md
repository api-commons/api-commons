---
api_specs:
- filename: acronis-account-management-openapi.yaml
  format: yaml
  label: Acronis Account Management API
  slug: account-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/openapi/acronis-account-management-openapi.yaml
- filename: acronis-agent-management-openapi.yaml
  format: yaml
  label: Acronis Agent Management REST API
  slug: agent-management-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/openapi/acronis-agent-management-openapi.yaml
- filename: acronis-task-manager-openapi.yaml
  format: yaml
  label: Acronis Task Manager API
  slug: task-manager-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/openapi/acronis-task-manager-openapi.yaml
categories:
- delete
- get
- info
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
- tags
- tenant
description: Spectral linting rules defining API design standards and conventions for Acronis.
layout: rules
name: Acronis API Rules
provider_name: Acronis
provider_slug: acronis
rule_count: 33
rules:
- description: OpenAPI info.title must be present
  given: $.info
  name: info-title-required
  severity: error
- description: OpenAPI info.description must be present
  given: $.info
  name: info-description-required
  severity: warn
- description: OpenAPI info.version must be defined
  given: $.info
  name: info-version-required
  severity: error
- description: API info should include contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Acronis APIs must use OpenAPI 3.x
  given: $
  name: openapi-version-3x
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https
  severity: error
- description: Acronis API servers should use acronis.com domain
  given: $.servers[*]
  name: servers-acronis-domain
  severity: info
- description: Paths must not end with a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: All operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Operation summaries should start with 'Acronis'
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-acronis-prefix
  severity: info
- description: Operations should have x-microcks-operation for mock testing
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-microcks-extension
  severity: info
- description: Global tags array should be defined
  given: $
  name: tags-global-defined
  severity: warn
- description: All global tags should have descriptions
  given: $.tags[*]
  name: tags-description-required
  severity: warn
- description: All parameters should have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: All operations must define at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Protected endpoints should define 401 responses
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should define types
  given: $.components.schemas[*].properties[*]
  name: schema-type-required
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Schema properties should have examples
  given: $.components.schemas[*].properties[*]
  name: schema-property-example
  severity: info
- description: Security schemes must be defined
  given: $
  name: security-schemes-defined
  severity: error
- description: Acronis APIs use bearer token authentication
  given: $.components.securitySchemes[*]
  name: security-bearer-scheme
  severity: info
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return 204 No Content
  given: $.paths[*].delete.responses
  name: delete-returns-204
  severity: warn
- description: Endpoints that scope to a tenant should include tenant_id parameter
  given: $.paths[*][get]
  name: tenant-id-parameter
  severity: info
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/acronis-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/rules/acronis-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 7
  warn: 11
slug: acronis-spectral-rules
source_filename: acronis-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: OpenAPI info.title must be present\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: OpenAPI info.description must be present\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: OpenAPI info.version must be defined\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API info should include contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3x:\n    description: Acronis APIs must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n\
  \        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: At least one server must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-acronis-domain:\n    description: Acronis API servers should use acronis.com domain\n    severity: info\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"acronis\\\\.com\"\n\n  # PATHS\n  paths-no-trailing-slash:\n    description: Paths must not end with a trailing slash\n    severity: error\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description:\
  \ All operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: All operations should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: All operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: All operations must have at least one tag\n    severity: error\n\
  \    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  operation-summary-acronis-prefix:\n    description: Operation summaries should start with 'Acronis'\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Acronis \"\n\n  operation-microcks-extension:\n    description: Operations should have x-microcks-operation for mock testing\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n\n  # TAGS\n  tags-global-defined:\n    description: Global tags array should be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  tags-description-required:\n    description: All global tags should have descriptions\n    severity: warn\n    given: \"$.tags[*]\"\n    then:\n      field: description\n\
  \      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: All parameters must have a schema\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: All operations must define at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: All responses\
  \ must have a description\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-401-required:\n    description: Protected endpoints should define 401 responses\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [\"401\"]\n\n  # SCHEMAS\n  schema-description-required:\n    description: Top-level schemas should have descriptions\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-type-required:\n    description: Schema properties should define types\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  schema-property-description:\n    description: Schema properties should\
  \ have descriptions\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-property-example:\n    description: Schema properties should have examples\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: example\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: components.securitySchemes\n      function: truthy\n\n  security-bearer-scheme:\n    description: Acronis APIs use bearer token authentication\n    severity: info\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      field: type\n      function: pattern\n      functionOptions:\n        match: \"http|oauth2\"\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given:\
  \ \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-returns-204:\n    description: DELETE operations should return 204 No Content\n    severity: warn\n    given: \"$.paths[*].delete.responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: [\"204\"]\n\n  # ACRONIS-SPECIFIC\n  tenant-id-parameter:\n    description: Endpoints that scope to a tenant should include tenant_id parameter\n    severity: info\n    given: \"$.paths[*][get]\"\n    then:\n      field: parameters\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/rules/acronis-spectral-rules.yml
tags:
- Cybersecurity
- Data Protection
- Endpoint Management
- Spectral
- Linting
- API Governance
---
