---
api_specs:
- filename: amazon-appflow-openapi.yml
  format: yaml
  label: Amazon AppFlow API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-appflow/refs/heads/main/openapi/amazon-appflow-openapi.yml
categories:
- delete
- get
- info
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
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon AppFlow.
layout: rules
name: Amazon AppFlow API Rules
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
rule_count: 34
rules:
- description: API title must start with "Amazon AppFlow"
  given: $.info
  name: info-title-prefix
  severity: warn
- description: API info must have a description with at least 50 characters
  given: $.info
  name: info-description-required
  severity: error
- description: API info must have a version field
  given: $.info
  name: info-version-required
  severity: error
- description: API info should include contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Must use OpenAPI 3.x specification
  given: $
  name: openapi-version-3x
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https
  severity: error
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Path segments must use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Amazon AppFlow"
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: OperationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined
  given: $
  name: tags-defined
  severity: warn
- description: Each global tag should have a description
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Every parameter must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-content-json
  severity: warn
- description: Every operation must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: POST operations should define a 400 error response
  given: $.paths[*][post].responses
  name: response-400-defined
  severity: warn
- description: Operations should define a 500 error response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-500-defined
  severity: warn
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should have a type defined
  given: $.components.schemas[*].properties[*]
  name: schema-properties-type-defined
  severity: warn
- description: Global security must be defined
  given: $
  name: security-defined
  severity: error
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Each security scheme should have a description
  given: $.components.securitySchemes[*]
  name: security-scheme-description
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Operations should provide request/response examples for mock server compatibility
  given: $.paths[*][post,put,patch].requestBody.content.application/json
  name: operation-examples-encouraged
  severity: info
- description: Operations should have x-microcks-operation extension for mock server compatibility
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-microcks-extension
  severity: info
rules_file: rules/amazon-appflow-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-appflow/refs/heads/main/rules/amazon-appflow-spectral-rules.yml
severity_counts:
  error: 17
  hint: 0
  info: 2
  warn: 15
slug: amazon-appflow-spectral-rules
source_filename: amazon-appflow-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"Amazon AppFlow\"\n    severity: warn\n    given: $.info\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: '^Amazon AppFlow'\n\n  info-description-required:\n    description: API info must have a description with at least 50 characters\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API info must have a version field\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API info should include contact information\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3x:\n    description: Must use OpenAPI 3.x specification\n    severity: error\n    given: $\n    then:\n\
  \      field: openapi\n      function: pattern\n      functionOptions:\n        match: '^3\\.'\n\n  # SERVERS\n  servers-defined:\n    description: Servers must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: $.servers[*]\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: '^https://'\n\n  servers-description:\n    description: Each server should have a description\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments must use kebab-case\n    severity: warn\n    given: $.paths\n    then:\n      field: '@key'\n      function: pattern\n      functionOptions:\n        match: '^(/[a-z0-9-{}#]+)+$'\n\n  paths-no-trailing-slash:\n    description: Paths must not\
  \ have trailing slashes\n    severity: error\n    given: $.paths\n    then:\n      field: '@key'\n      function: pattern\n      functionOptions:\n        notMatch: '/$'\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries must start with \"Amazon AppFlow\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: '^Amazon AppFlow'\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n\
  \    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: OperationId must use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]+$'\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tags-defined:\n    description: Global tags array should be defined\n    severity: warn\n    given: $\n    then:\n      field: tags\n      function: truthy\n\n  tag-description-required:\n    description: Each global tag should have a description\n    severity: warn\n    given: $.tags[*]\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n\
  \  parameter-description-required:\n    description: Every parameter must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Every parameter must have a schema\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-content-json:\n    description: Request bodies should use application/json content type\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      field: application/json\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have at least one 2xx response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: '200'\n      function: truthy\n\n  response-400-defined:\n\
  \    description: POST operations should define a 400 error response\n    severity: warn\n    given: $.paths[*][post].responses\n    then:\n      field: '400'\n      function: truthy\n\n  response-500-defined:\n    description: Operations should define a 500 error response\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: '500'\n      function: truthy\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-description-required:\n    description: Top-level component schemas should have descriptions\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-properties-type-defined:\n    description: Schema properties should have a type defined\n\
  \    severity: warn\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-defined:\n    description: Global security must be defined\n    severity: error\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes must be defined in components\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-scheme-description:\n    description: Each security scheme should have a description\n    severity: warn\n    given: $.components.securitySchemes[*]\n    then:\n      field: description\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description:\
  \ DELETE operations should not have a request body\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  operation-examples-encouraged:\n    description: Operations should provide request/response examples for mock server compatibility\n    severity: info\n    given: $.paths[*][post,put,patch].requestBody.content.application/json\n    then:\n      field: examples\n      function: truthy\n\n  operation-microcks-extension:\n    description: Operations should have x-microcks-operation extension for mock server compatibility\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-appflow/refs/heads/main/rules/amazon-appflow-spectral-rules.yml
tags:
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
- Spectral
- Linting
- API Governance
---
