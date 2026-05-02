---
api_specs:
- filename: airtable-airtable-api-openapi.yml
  format: yaml
  label: Airtable API
  slug: airtable-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/openapi/airtable-airtable-api-openapi.yml
- filename: airtable-metadata-api-openapi.yml
  format: yaml
  label: Airtable Metadata API
  slug: airtable-metadata-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/openapi/airtable-metadata-api-openapi.yml
- filename: airtable-enterprise-api-openapi.yml
  format: yaml
  label: Airtable Enterprise API
  slug: airtable-enterprise-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/openapi/airtable-enterprise-api-openapi.yml
- filename: airtable-scim-api-openapi.yml
  format: yaml
  label: Airtable SCIM API
  slug: airtable-scim-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/openapi/airtable-scim-api-openapi.yml
- filename: airtable-audit-logs-api-openapi.yml
  format: yaml
  label: Airtable Audit Logs API
  slug: airtable-audit-logs-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/openapi/airtable-audit-logs-api-openapi.yml
- filename: airtable-shares-api-openapi.yml
  format: yaml
  label: Airtable Shares API
  slug: airtable-shares-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/openapi/airtable-shares-api-openapi.yml
categories:
- airtable
- get
- info
- microcks
- 'no'
- openapi
- operation
- parameter
- paths
- post
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Airtable.
layout: rules
name: Airtable API Rules
provider_name: Airtable
provider_slug: airtable
rule_count: 29
rules:
- description: Info title must be defined.
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be defined.
  given: $.info
  name: info-description-required
  severity: warn
- description: Info version must be defined.
  given: $.info
  name: info-version-required
  severity: error
- description: OpenAPI version must be 3.x.
  given: $
  name: openapi-version-3
  severity: error
- description: Servers must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*]
  name: servers-https
  severity: warn
- description: Airtable API servers should use api.airtable.com.
  given: $.servers[*]
  name: servers-api-airtable-base
  severity: info
- description: Airtable API paths typically start with /v0/.
  given: $.paths[*]~
  name: paths-v0-prefix
  severity: info
- description: Path segments should use kebab-case or base IDs.
  given: $.paths[*]~
  name: paths-kebab-or-base-id
  severity: info
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: operationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationId-camelCase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Operation summaries should start with "Airtable".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-starts-with-airtable
  severity: info
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Authorization should use Bearer token scheme.
  given: $.components.securitySchemes[*]
  name: parameter-authorization-header
  severity: info
- description: Every operation must have a success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Operations with request bodies should document 422 validation errors.
  given: $.paths[*][post,put,patch].responses
  name: response-422-for-validation
  severity: info
- description: Schema properties in Airtable APIs use camelCase.
  given: $.components.schemas[*].properties[*]~
  name: schema-property-camelCase
  severity: info
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Security schemes must be defined.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Airtable APIs use Bearer token authentication.
  given: $.components.securitySchemes[*]
  name: security-bearer-required
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: List operations should support cursor or offset pagination.
  given: $.paths[*].get
  name: post-list-uses-offset
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Operations should include x-microcks-operation for mock compatibility.
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
- description: Rate limits should be documented in the API info.
  given: $.info
  name: airtable-rate-limit-documented
  severity: info
rules_file: rules/airtable-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/rules/airtable-spectral-rules.yml
severity_counts:
  error: 9
  hint: 0
  info: 11
  warn: 9
slug: airtable-spectral-rules
source_filename: airtable-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: Info title must be defined.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: Info description must be defined.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info version must be defined.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: OpenAPI version must be 3.x.\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers must be defined.\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n\
  \    description: Server URLs must use HTTPS.\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-api-airtable-base:\n    description: Airtable API servers should use api.airtable.com.\n    severity: info\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"api\\\\.airtable\\\\.com\"\n\n  # PATHS — NAMING CONVENTIONS\n  paths-v0-prefix:\n    description: Airtable API paths typically start with /v0/.\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/v0/|/scim/)\"\n\n  paths-kebab-or-base-id:\n    description: Path segments should use kebab-case or base IDs.\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-zA-Z0-9{}_/-]+)+$\"\n\n  # OPERATIONS\n\
  \  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: Every operation should have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-operationId-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationId-camelCase:\n    description: operationId should use camelCase.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description:\
  \ Every operation must have at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  operation-summary-starts-with-airtable:\n    description: Operation summaries should start with \"Airtable\".\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Airtable \"\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-authorization-header:\n    description: Authorization should use Bearer token scheme.\n    severity: info\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      field: scheme\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description:\
  \ Every operation must have a success response.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: truthy\n\n  response-description-required:\n    description: All responses must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-422-for-validation:\n    description: Operations with request bodies should document 422 validation errors.\n    severity: info\n    given: \"$.paths[*][post,put,patch].responses\"\n    then:\n      function: truthy\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-property-camelCase:\n    description: Schema properties in Airtable APIs use camelCase.\n    severity: info\n    given: \"$.components.schemas[*].properties[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  schema-description-required:\n    description: Top-level\
  \ schemas should have a description.\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined.\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-bearer-required:\n    description: Airtable APIs use Bearer token authentication.\n    severity: warn\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  post-list-uses-offset:\n    description: List operations should support cursor or offset pagination.\n    severity: info\n    given: \"$.paths[*].get\"\n    then:\n      field:\
  \ parameters\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: truthy\n\n  microcks-operation-extension:\n    description: Operations should include x-microcks-operation for mock compatibility.\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n\n  airtable-rate-limit-documented:\n    description: Rate limits should be documented in the API info.\n    severity: info\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/rules/airtable-spectral-rules.yml
tags:
- Applications
- Collaboration
- Data
- Databases
- Low-Code
- Productivity
- Spreadsheets
- Spectral
- Linting
- API Governance
---
