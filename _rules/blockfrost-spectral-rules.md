---
api_specs:
- filename: blockfrost-openapi.yaml
  format: yaml
  label: Blockfrost API
  slug: blockfrost
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/blockfrost/refs/heads/main/openapi/blockfrost-openapi.yaml
categories:
- external
- get
- info
- 'no'
- openapi
- operation
- pagination
- parameter
- paths
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Blockfrost.
layout: rules
name: Blockfrost API Rules
provider_name: Blockfrost
provider_slug: blockfrost
rule_count: 30
rules:
- description: API title must start with "Blockfrost"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Info object should have contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Info object should have license information
  given: $.info
  name: info-license-required
  severity: info
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Path segments must use lowercase with underscores or kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Blockfrost"
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
- description: operationId should use snake_case
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-snake-case
  severity: info
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must define a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: List endpoints should support count pagination parameter
  given: $.paths[*].get
  name: pagination-count-or-limit
  severity: info
- description: Every operation must define at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Operations should define a 400 Bad Request response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-400-defined
  severity: info
- description: Operations should define a 403 Forbidden response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-403-defined
  severity: info
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas must have a description
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: At least one security scheme must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Global tags array should be defined
  given: $
  name: tags-global-defined
  severity: info
- description: External documentation should be provided
  given: $
  name: external-docs-encouraged
  severity: info
rules_file: rules/blockfrost-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/blockfrost/refs/heads/main/rules/blockfrost-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 7
  warn: 10
slug: blockfrost-spectral-rules
source_filename: blockfrost-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Blockfrost Spectral Ruleset\n# Enforces conventions from the Blockfrost Cardano blockchain API OpenAPI specification.\n\nrules:\n\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title must start with \"Blockfrost\"\n    severity: warn\n    given: '$.info.title'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^Blockfrost'\n\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: '$.info'\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must have a version\n    severity: error\n    given: '$.info'\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Info object should have contact information\n    severity: warn\n    given: '$.info'\n    then:\n      field: contact\n      function: truthy\n\n  info-license-required:\n    description: Info object should\
  \ have license information\n    severity: info\n    given: '$.info'\n    then:\n      field: license\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: '$'\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: '^3\\.'\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined\n    severity: error\n    given: '$'\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: '$.servers[*].url'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments must use lowercase with underscores or kebab-case\n    severity: warn\n    given: '$.paths[*]~'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^(/[a-z0-9_{}.-]+)+$'\n\
  \n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: warn\n    given: '$.paths[*]~'\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: '/$'\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries must start with \"Blockfrost\"\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].summary'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^Blockfrost'\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation\
  \ must have an operationId\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-snake-case:\n    description: operationId should use snake_case\n    severity: info\n    given: '$.paths[*][get,post,put,patch,delete].operationId'\n    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-z0-9_]*$'\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete].parameters[*]'\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Every parameter must define a schema\n    severity:\
  \ error\n    given: '$.paths[*][get,post,put,patch,delete].parameters[*]'\n    then:\n      field: schema\n      function: truthy\n\n  pagination-count-or-limit:\n    description: List endpoints should support count pagination parameter\n    severity: info\n    given: '$.paths[*].get'\n    then:\n      field: parameters\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must define at least one 2xx response\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: responses\n      function: truthy\n\n  response-400-defined:\n    description: Operations should define a 400 Bad Request response\n    severity: info\n    given: '$.paths[*][get,post,put,patch,delete].responses'\n    then:\n      field: '400'\n      function: truthy\n\n  response-403-defined:\n    description: Operations should define a 403 Forbidden response\n    severity: info\n    given: '$.paths[*][get,post,put,patch,delete].responses'\n\
  \    then:\n      field: '403'\n      function: truthy\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].responses[*]'\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Top-level schemas must have a description\n    severity: warn\n    given: '$.components.schemas[*]'\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: At least one security scheme must be defined\n    severity: error\n    given: '$.components'\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: Global security must be defined\n    severity: warn\n    given: '$'\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations\
  \ must not have a request body\n    severity: error\n    given: '$.paths[*].get'\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: '$..description'\n    then:\n      function: pattern\n      functionOptions:\n        match: '.+'\n\n  tags-global-defined:\n    description: Global tags array should be defined\n    severity: info\n    given: '$'\n    then:\n      field: tags\n      function: truthy\n\n  external-docs-encouraged:\n    description: External documentation should be provided\n    severity: info\n    given: '$'\n    then:\n      field: externalDocs\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/blockfrost/refs/heads/main/rules/blockfrost-spectral-rules.yml
tags:
- Blockchain
- Cardano
- Cryptocurrency
- DApps
- NFT
- Web3
- Spectral
- Linting
- API Governance
---
