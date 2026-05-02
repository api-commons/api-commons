---
api_specs:
- filename: amazon-well-architected-tool-openapi-original.yaml
  format: yaml
  label: AWS Well-Architected Tool API
  slug: aws-well-architected-tool-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-well-architected-tool/refs/heads/main/openapi/amazon-well-architected-tool-openapi-original.yaml
categories:
- components
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
description: Spectral linting rules defining API design standards and conventions for Amazon Well-Architected Tool.
layout: rules
name: Amazon Well-Architected Tool API Rules
provider_name: Amazon Well-Architected Tool
provider_slug: amazon-well-architected-tool
rule_count: 25
rules:
- description: API title should reference AWS Well-Architected Tool
  given: $.info
  name: info-title-format
  severity: warn
- description: API info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.0.x
  given: $
  name: openapi-version
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https
  severity: error
- description: Path segments should use kebab-case or camelCase (AWS uses mixed)
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Paths must not have a trailing slash
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: operationId should use PascalCase (AWS convention)
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-pascal-case
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: warn
- description: Operation summary should start with Amazon Well-Architected Tool
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-prefix
  severity: info
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: All parameters must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Request bodies should have a description
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: info
- description: Request bodies should support application/json
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Operations must define at least one success (2xx) response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have a description
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: info
- description: Schema properties should define a type
  given: $.components.schemas[*].properties[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes should be defined in components
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Components schemas should be defined for reuse
  given: $.components
  name: components-schemas-exist
  severity: info
rules_file: rules/amazon-well-architected-tool-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-well-architected-tool/refs/heads/main/rules/amazon-well-architected-tool-spectral-rules.yml
severity_counts:
  error: 9
  hint: 0
  info: 5
  warn: 11
slug: amazon-well-architected-tool-spectral-rules
source_filename: amazon-well-architected-tool-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Amazon Well-Architected Tool API Spectral Ruleset\n# Enforces conventions observed across the Well-Architected Tool OpenAPI specification\n\nrules:\n\n  # INFO / METADATA\n  info-title-format:\n    description: API title should reference AWS Well-Architected Tool\n    severity: warn\n    given: $.info\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: \"^AWS Well-Architected Tool\"\n\n  info-description-required:\n    description: API info must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API info must have a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description: Must use OpenAPI 3.0.x\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n\
  \        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: $.servers[*]\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case or camelCase (AWS uses mixed)\n    severity: info\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^/[a-zA-Z0-9/_{}.-]+$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have a trailing slash\n    severity: warn\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-operationid-required:\n\
  \    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-pascal-case:\n    description: operationId should use PascalCase (AWS convention)\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]+$\"\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summary should start with Amazon Well-Architected Tool\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^Amazon\
  \ Well-Architected Tool\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-description:\n    description: Request bodies should have a description\n    severity: info\n    given: $.paths[*][post,put,patch].requestBody\n    then:\n      field: description\n      function: truthy\n\n  request-body-json-content:\n    description: Request bodies should support application/json\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      field: application/json\n      function: truthy\n\n  # RESPONSES\n \
  \ response-success-required:\n    description: Operations must define at least one success (2xx) response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          minProperties: 1\n\n  response-description-required:\n    description: All responses must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-description-recommended:\n    description: Top-level schemas should have a description\n    severity: info\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-type-defined:\n    description: Schema properties should define a type\n    severity: warn\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n\
  \  security-schemes-defined:\n    description: Security schemes should be defined in components\n    severity: warn\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: warn\n    given: $..description\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  components-schemas-exist:\n    description: Components schemas should be defined for reuse\n    severity: info\n    given:\
  \ $.components\n    then:\n      field: schemas\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-well-architected-tool/refs/heads/main/rules/amazon-well-architected-tool-spectral-rules.yml
tags:
- Architecture
- Best Practices
- Cloud Governance
- Well-Architected
- Workloads
- Spectral
- Linting
- API Governance
---
