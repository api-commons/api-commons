---
api_specs:
- filename: akamai-api-security-openapi.json
  format: json
  label: Akamai API Security
  slug: api-security
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/akamai-api-security/refs/heads/main/openapi/akamai-api-security-openapi.json
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
description: Spectral linting rules defining API design standards and conventions for Akamai API Security.
layout: rules
name: Akamai API Security API Rules
provider_name: Akamai API Security
provider_slug: akamai-api-security
rule_count: 23
rules:
- description: ''
  given: $.info.title
  name: info-title-format
  severity: warn
- description: ''
  given: $.info
  name: info-description-required
  severity: error
- description: ''
  given: $.info
  name: info-version-required
  severity: error
- description: ''
  given: $
  name: openapi-version-3
  severity: error
- description: ''
  given: $
  name: servers-defined
  severity: error
- description: ''
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: ''
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: ''
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete,head,options].summary
  name: operation-summary-akamai-prefix
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete,head,options].operationId
  name: operation-id-camel-case
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-success-response
  severity: error
- description: ''
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: ''
  given: $.components.schemas[*].properties[*]
  name: schema-type-defined
  severity: warn
- description: ''
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: ''
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: ''
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: ''
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: ''
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/akamai-api-security-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/akamai-api-security/refs/heads/main/rules/akamai-api-security-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 0
  warn: 11
slug: akamai-api-security-spectral-rules
source_filename: akamai-api-security-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Akamai API Security Spectral Ruleset\n# Enforces conventions found in the Akamai Application Security API specification\n\nrules:\n\n  # INFO / METADATA\n  info-title-format:\n    message: \"API title should start with 'Akamai'\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Akamai\"\n\n  info-description-required:\n    message: \"API info must have a description\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    message: \"API info must have a version\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    message: \"Must use OpenAPI 3.x\"\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n\
  \    message: \"Servers must be defined\"\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    message: \"Server URLs should use HTTPS\"\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS\n  paths-kebab-case:\n    message: \"Path segments should use kebab-case\"\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(\\\\/([a-z0-9][a-z0-9\\\\-]*|\\\\{[a-zA-Z][a-zA-Z0-9_]*\\\\}))*$\"\n\n  paths-no-trailing-slash:\n    message: \"Paths must not have trailing slashes\"\n    severity: error\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    message: \"Every operation must have a summary\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\
  \n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-akamai-prefix:\n    message: \"Operation summaries should start with 'Akamai'\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Akamai\"\n\n  operation-description-required:\n    message: \"Every operation must have a description\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    message: \"Every operation must have an operationId\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    message: \"operationId should use camelCase\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,head,options].operationId\"\
  \n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    message: \"Every operation must have at least one tag\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,head,options]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    message: \"All parameters must have a description\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  operation-success-response:\n    message: \"Operations must have at least one 2xx response\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses\n      function: truthy\n\n  response-description-required:\n    message: \"All responses must have a description\"\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n\
  \    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-type-defined:\n    message: \"Schema properties should have a type defined\"\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  schema-description-required:\n    message: \"Top-level schemas should have a description\"\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    message: \"Security schemes should be defined\"\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHODS\n  get-no-request-body:\n    message: \"GET operations must not have a request body\"\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    message: \"DELETE operations\
  \ should not have a request body\"\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    message: \"Descriptions must not be empty\"\n    severity: error\n    given: \"$..description\"\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/akamai-api-security/refs/heads/main/rules/akamai-api-security-spectral-rules.yml
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
- Spectral
- Linting
- API Governance
---
