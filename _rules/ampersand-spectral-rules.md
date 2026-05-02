---
api_specs:
- filename: ampersand-api-openapi-original.yml
  format: yaml
  label: Ampersand API
  slug: ampersand-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/ampersand/refs/heads/main/openapi/ampersand-api-openapi-original.yml
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
description: Spectral linting rules defining API design standards and conventions for Ampersand.
layout: rules
name: Ampersand API Rules
provider_name: Ampersand
provider_slug: ampersand
rule_count: 26
rules:
- description: API title should reference "Ampersand".
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API info must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: API info must define a version.
  given: $.info
  name: info-version-required
  severity: error
- description: OpenAPI version must be 3.0.x or 3.1.x.
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Path segments should use kebab-case or camelCase with braces for params.
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes.
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Ampersand".
  given: $.paths[*][get,post,put,patch,delete,head,options].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete,head,options].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined.
  given: $
  name: tags-global-defined
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content-type
  severity: warn
- description: Every operation must define responses.
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Operations should document a 401 unauthorized response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Security schemes must be defined in components.
  given: $.components
  name: security-scheme-defined
  severity: error
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return 204 No Content when successful.
  given: $.paths[*].delete.responses
  name: delete-returns-204
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should include examples for documentation.
  given: $.paths[*][*].responses[*].content[*]
  name: examples-encouraged
  severity: info
rules_file: rules/ampersand-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/ampersand/refs/heads/main/rules/ampersand-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 2
  warn: 9
slug: ampersand-spectral-rules
source_filename: ampersand-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title should reference \"Ampersand\".\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: '^Ampersand'\n\n  info-description-required:\n    description: API info must have a description.\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API info must define a version.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: OpenAPI version must be 3.0.x or 3.1.x.\n    severity: error\n    given: $.openapi\n    then:\n      function: pattern\n      functionOptions:\n        match: '^3\\.'\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: $\n    then:\n      field: servers\n\
  \      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n\n  # PATHS - NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case or camelCase with braces for params.\n    severity: warn\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        match: '^(/[a-z0-9A-Z{}_-]+)+$'\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes.\n    severity: error\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: '/$'\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n\
  \    description: Operation summaries should start with \"Ampersand\".\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: '^Ampersand'\n\n  operation-description-required:\n    description: Every operation should have a description.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId should use camelCase.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]*$'\n\
  \n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tags-global-defined:\n    description: Global tags array should be defined.\n    severity: warn\n    given: $\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-json-content-type:\n    description: Request bodies should use application/json content type.\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      field: application/json\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation\
  \ must define responses.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: responses\n      function: truthy\n\n  response-401-required:\n    description: Operations should document a 401 unauthorized response.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: '401'\n      function: truthy\n\n  response-description-required:\n    description: Every response must have a description.\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Top-level schemas should have a description.\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-scheme-defined:\n    description: Security schemes must be defined in components.\n    severity: error\n    given: $.components\n    then:\n\
  \      field: securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-returns-204:\n    description: DELETE operations should return 204 No Content when successful.\n    severity: info\n    given: $.paths[*].delete.responses\n    then:\n      field: '204'\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: error\n    given: $..description\n    then:\n      function: pattern\n      functionOptions:\n        match: '.+'\n\n  examples-encouraged:\n    description: Operations should include examples for documentation.\n    severity: info\n    given: $.paths[*][*].responses[*].content[*]\n    then:\n      field: examples\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/ampersand/refs/heads/main/rules/ampersand-spectral-rules.yml
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
- Spectral
- Linting
- API Governance
---
