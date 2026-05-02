---
api_specs:
- filename: aqua-security-api.yaml
  format: yaml
  label: Aqua Security
  slug: aqua-security
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/aqua-security/refs/heads/main/openapi/aqua-security-api.yaml
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
- tags
description: Spectral linting rules defining API design standards and conventions for Aqua Security.
layout: rules
name: Aqua Security API Rules
provider_name: Aqua Security
provider_slug: aqua-security
rule_count: 30
rules:
- description: Info object must have a title starting with "Aqua Security"
  given: $.info
  name: info-title-required
  severity: error
- description: Info object must have a description with at least 50 characters
  given: $.info
  name: info-description-required
  severity: warn
- description: Info object must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: API should have contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Use OpenAPI 3.0.x
  given: $
  name: openapi-version-3
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS
  given: $.servers[*]
  name: servers-https-only
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths should not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Aqua Security"
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-prefix
  severity: warn
- description: Every operation should have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: OperationId should use camelCase
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: error
- description: All parameters must have a description
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Parameter names should use snake_case or kebab-case
  given: $.paths[*][*].parameters[*]
  name: parameter-snake-case
  severity: info
- description: Request bodies should use application/json
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-content-type
  severity: warn
- description: Every operation must have a success (2xx) response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: Secured endpoints should document 401 responses
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-401-required
  severity: warn
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Schema properties should have a type defined
  given: $.components.schemas[*].properties[*]
  name: schema-type-defined
  severity: warn
- description: Top-level schemas should have a description
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: info
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Bearer auth security scheme should have a description
  given: $.components.securitySchemes[*]
  name: security-bearer-description
  severity: warn
- description: GET operations should not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: DELETE operations should return 204
  given: $.paths[*].delete.responses
  name: delete-returns-204
  severity: info
- description: Descriptions should not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Tags should be defined globally with descriptions
  given: $
  name: tags-global-defined
  severity: warn
rules_file: rules/aqua-security-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/aqua-security/refs/heads/main/rules/aqua-security-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 3
  warn: 15
slug: aqua-security-spectral-rules
source_filename: aqua-security-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: Info object must have a title starting with \"Aqua Security\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: \"^Aqua Security\"\n\n  info-description-required:\n    description: Info object must have a description with at least 50 characters\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API should have contact information\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Use OpenAPI 3.0.x\n    severity: error\n    given: \"\
  $\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: Server URLs should use HTTPS\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS - NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: \"$.paths\"\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^(\\\\/[a-z0-9][a-z0-9-]*[a-z0-9]?|\\\\{[a-z][a-zA-Z0-9_]*\\\\})*\\\\/?$\"\n\n  paths-no-trailing-slash:\n    description: Paths should not have trailing slashes\n    severity: warn\n    given: \"$.paths\"\n    then:\n     \
  \ field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"Aqua Security\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^Aqua Security\"\n\n  operation-description-required:\n    description: Every operation should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\
  \n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: OperationId should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-snake-case:\n    description: Parameter names should use snake_case or kebab-case\n    severity: info\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: name\n      function:\
  \ pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_-]*$\"\n\n  # REQUEST BODIES\n  request-body-content-type:\n    description: Request bodies should use application/json\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      field: \"@key\"\n      function: enumeration\n      functionOptions:\n        values:\n          - application/json\n          - multipart/form-data\n          - application/x-www-form-urlencoded\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have a success (2xx) response\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-401-required:\n    description: Secured endpoints should document 401 responses\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].responses\"\n    then:\n\
  \      field: \"401\"\n      function: truthy\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-type-defined:\n    description: Schema properties should have a type defined\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [type]\n            - required: [$ref]\n\n  schema-description-recommended:\n    description: Top-level schemas should have a description\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components\n    severity: error\n    given: \"$.components\"\
  \n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-bearer-description:\n    description: Bearer auth security scheme should have a description\n    severity: warn\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations should not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-returns-204:\n    description: DELETE operations should return 204\n    severity: info\n    given: \"$.paths[*].delete.responses\"\n    then:\n      field: \"204\"\n      function: truthy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description:\
  \ Descriptions should not be empty strings\n    severity: error\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  tags-global-defined:\n    description: Tags should be defined globally with descriptions\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/aqua-security/refs/heads/main/rules/aqua-security-spectral-rules.yml
tags:
- Cloud Native
- Containers
- Kubernetes
- Runtime Protection
- Security
- Vulnerability Scanning
- Spectral
- Linting
- API Governance
---
