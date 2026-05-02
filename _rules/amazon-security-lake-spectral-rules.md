---
api_specs:
- filename: amazon-security-lake-openapi.yml
  format: yaml
  label: Amazon Security Lake API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-security-lake/refs/heads/main/openapi/amazon-security-lake-openapi.yml
categories:
- global
- info
- microcks
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Security Lake.
layout: rules
name: Amazon Security Lake API Rules
provider_name: Amazon Security Lake
provider_slug: amazon-security-lake
rule_count: 21
rules:
- description: Info title must be present
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: warn
- description: Info version must be present
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https-only
  severity: error
- description: Paths should be versioned with /v1/ prefix
  given: $.paths
  name: paths-versioned
  severity: info
- description: Path segments must use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Amazon Security Lake"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId must use PascalCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-pascal-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must have a success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Top-level component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: info
- description: Security schemes should be defined in components
  given: $
  name: security-schemes-defined
  severity: warn
- description: Global security should be defined
  given: $
  name: global-security-defined
  severity: warn
- description: Operations should have x-microcks-operation for mock support
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-present
  severity: info
rules_file: rules/amazon-security-lake-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-security-lake/refs/heads/main/rules/amazon-security-lake-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 3
  warn: 10
slug: amazon-security-lake-spectral-rules
source_filename: amazon-security-lake-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: Info description must be present\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info version must be present\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: Servers must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n\
  \    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS\n  paths-versioned:\n    description: Paths should be versioned with /v1/ prefix\n    severity: info\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/v[0-9]/\"\n\n  paths-kebab-case:\n    description: Path segments must use kebab-case\n    severity: warn\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/v[0-9]/[a-z0-9-]+)*(/\\\\{[a-z][a-zA-Z0-9]*\\\\})*$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries must start\
  \ with \"Amazon Security Lake\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amazon Security Lake\"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-pascal-case:\n    description: operationId must use PascalCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation\
  \ must have at least one tag\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have a success response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-description-required:\n    description: Every response must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n  \
  \    field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-recommended:\n    description: Top-level component schemas should have descriptions\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes should be defined in components\n    severity: warn\n    given: \"$\"\n    then:\n      field: components.securitySchemes\n      function: truthy\n\n  global-security-defined:\n    description: Global security should be defined\n    severity: warn\n    given: \"$\"\n    then:\n      field: security\n      function: truthy\n\n  # GENERAL QUALITY\n  microcks-operation-present:\n    description: Operations should have x-microcks-operation for mock support\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-security-lake/refs/heads/main/rules/amazon-security-lake-spectral-rules.yml
tags:
- Data Lake
- Security
- SIEM
- Threat Detection
- Spectral
- Linting
- API Governance
---
