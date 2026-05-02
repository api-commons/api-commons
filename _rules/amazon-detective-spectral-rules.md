---
api_specs:
- filename: amazon-detective-openapi.yml
  format: yaml
  label: Amazon Detective API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-detective/refs/heads/main/openapi/amazon-detective-openapi.yml
categories:
- delete
- external
- get
- info
- 'no'
- openapi
- operation
- operations
- parameter
- paths
- post
- request
- response
- schema
- security
- servers
- tag
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon Detective.
layout: rules
name: Amazon Detective API Rules
provider_name: Amazon Detective
provider_slug: amazon-detective
rule_count: 39
rules:
- description: API title should start with "Amazon Detective"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API must have a description of at least 50 characters
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: API info should include contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: API info should include license information
  given: $.info
  name: info-license-required
  severity: warn
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Path segments should use kebab-case or camelCase (AWS Detective uses camelCase in some paths)
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Paths must not end with a trailing slash
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Amazon Detective"
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-prefix
  severity: warn
- description: All operations must have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: OperationIds should use camelCase
  given: $.paths[*][get,post,put,delete,patch].operationId
  name: operation-id-camel-case
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined
  given: $
  name: tags-global-defined
  severity: warn
- description: Global tags should have descriptions
  given: $.tags[*]
  name: tag-description-required
  severity: info
- description: All parameters must have a description
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-description-required
  severity: error
- description: All parameters must have a schema
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should have a description
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: info
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Operations must have at least one 2xx response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: error
- description: Operations should include a 400 error response
  given: $.paths[*][post,put,patch].responses
  name: response-error-400
  severity: info
- description: Operations should include a 500 error response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-error-500
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schemas should have a type defined
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Amazon Detective schema properties use PascalCase naming
  given: $.components.schemas[*].properties
  name: schema-property-pascal-case
  severity: info
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: error
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Security schemes should have descriptions
  given: $.components.securitySchemes[*]
  name: security-scheme-description
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations typically should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body-unless-needed
  severity: info
- description: POST operations should have a request body
  given: $.paths[*].post
  name: post-should-have-request-body
  severity: info
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have x-microcks-operation for mock support
  given: $.paths[*][get,post,put,delete,patch]
  name: operations-microcks-extension
  severity: info
- description: API should reference external documentation
  given: $
  name: external-docs-encouraged
  severity: info
rules_file: rules/amazon-detective-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-detective/refs/heads/main/rules/amazon-detective-spectral-rules.yml
severity_counts:
  error: 18
  hint: 0
  info: 9
  warn: 12
slug: amazon-detective-spectral-rules
source_filename: amazon-detective-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title should start with \"Amazon Detective\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Detective\"\n\n  info-description-required:\n    description: API must have a description of at least 50 characters\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API must have a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API info should include contact information\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  info-license-required:\n    description: API info should include license information\n    severity: warn\n    given: $.info\n    then:\n      field: license\n      function:\
  \ truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description-required:\n    description: Each server should have a description\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case or camelCase (AWS Detective uses camelCase in some paths)\n \
  \   severity: info\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z][a-zA-Z0-9/-]*)+$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not end with a trailing slash\n    severity: error\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"Amazon Detective\"\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Detective\"\n\n  operation-description-required:\n    description: All operations must have a description\n    severity: error\n    given:\
  \ $.paths[*][get,post,put,delete,patch]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: All operations must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: OperationIds should use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: All operations must have at least one tag\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tags-global-defined:\n    description: Global tags array should be defined\n    severity: warn\n    given: $\n    then:\n      field: tags\n      function: truthy\n\n  tag-description-required:\n\
  \    description: Global tags should have descriptions\n    severity: info\n    given: $.tags[*]\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: All parameters must have a schema\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-description:\n    description: Request bodies should have a description\n    severity: info\n    given: $.paths[*][post,put,patch].requestBody\n    then:\n      field: description\n      function: truthy\n\n  request-body-json-content:\n    description: Request bodies should use application/json content type\n    severity:\
  \ warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must have at least one 2xx response\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: $.paths[*][get,post,put,delete,patch].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-error-400:\n    description: Operations should include a 400 error response\n    severity: info\n    given: $.paths[*][post,put,patch].responses\n\
  \    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: ['400']\n\n  response-error-500:\n    description: Operations should include a 500 error response\n    severity: warn\n    given: $.paths[*][get,post,put,delete,patch].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required: ['500']\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-description-required:\n    description: Top-level schemas should have descriptions\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-type-required:\n    description: Schemas should have a type defined\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  schema-property-pascal-case:\n    description: Amazon Detective schema properties use PascalCase naming\n    severity: info\n    given:\
  \ $.components.schemas[*].properties\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n\n  # SECURITY\n  security-global-defined:\n    description: Global security must be defined\n    severity: error\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes must be defined in components\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-scheme-description:\n    description: Security schemes should have descriptions\n    severity: warn\n    given: $.components.securitySchemes[*]\n    then:\n      field: description\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body-unless-needed:\n\
  \    description: DELETE operations typically should not have a request body\n    severity: info\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  post-should-have-request-body:\n    description: POST operations should have a request body\n    severity: info\n    given: $.paths[*].post\n    then:\n      field: requestBody\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: $..description\n    then:\n      function: truthy\n\n  operations-microcks-extension:\n    description: Operations should have x-microcks-operation for mock support\n    severity: info\n    given: $.paths[*][get,post,put,delete,patch]\n    then:\n      field: x-microcks-operation\n      function: truthy\n\n  external-docs-encouraged:\n    description: API should reference external documentation\n    severity: info\n    given: $\n    then:\n      field: externalDocs\n\
  \      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-detective/refs/heads/main/rules/amazon-detective-spectral-rules.yml
tags:
- Forensics
- Investigation
- Security
- Spectral
- Linting
- API Governance
---
