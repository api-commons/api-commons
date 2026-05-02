---
api_specs:
- filename: akamai-edgekv-openapi.json
  format: json
  label: Akamai EdgeKV API
  slug: akamai-edgekv-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/akamai/refs/heads/main/openapi/akamai-edgekv-openapi.json
- filename: akamai-edgeworkers-openapi.json
  format: json
  label: Akamai EdgeWorkers API
  slug: akamai-edgeworkers-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/akamai/refs/heads/main/openapi/akamai-edgeworkers-openapi.json
- filename: akamai-network-lists-openapi.json
  format: json
  label: Akamai Network Lists API
  slug: akamai-network-lists-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/akamai/refs/heads/main/openapi/akamai-network-lists-openapi.json
- filename: akamai-papi-openapi.json
  format: json
  label: Akamai Property Manager API
  slug: akamai-property-manager-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/akamai/refs/heads/main/openapi/akamai-papi-openapi.json
categories:
- delete
- get
- info
- openapi
- operation
- parameter
- paths
- response
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Akamai.
layout: rules
name: Akamai API Rules
provider_name: Akamai
provider_slug: akamai
rule_count: 21
rules:
- description: ''
  given: $.info.title
  name: info-title-akamai-prefix
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
  severity: error
- description: ''
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: ''
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-akamai-prefix
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-external-docs
  severity: info
- description: ''
  given: $.paths[*][get,post,put,patch,delete][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: ''
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: ''
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: ''
  given: $.paths[*].delete.responses
  name: delete-returns-no-content
  severity: info
- description: ''
  given: $.components
  name: security-schemes-defined
  severity: info
- description: ''
  given: $
  name: tags-global-defined
  severity: info
rules_file: rules/akamai-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/akamai/refs/heads/main/rules/akamai-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 4
  warn: 6
slug: akamai-spectral-rules
source_filename: akamai-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Akamai API Spectral Ruleset\n# Enforces conventions found across Akamai's API suite\n\nrules:\n\n  # INFO / METADATA\n  info-title-akamai-prefix:\n    message: \"API title should start with 'Akamai:'\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Akamai:\"\n\n  info-description-required:\n    message: \"API info must have a description\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    message: \"API info must have a version\"\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    message: \"Must use OpenAPI 3.x\"\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    message:\
  \ \"Servers must be defined\"\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    message: \"Server URLs must use HTTPS\"\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS\n  paths-kebab-case:\n    message: \"Path segments should use kebab-case\"\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(\\\\/([a-z0-9][a-z0-9\\\\-]*|\\\\{[a-zA-Z][a-zA-Z0-9_]*\\\\}))*$\"\n\n  paths-no-trailing-slash:\n    message: \"Paths must not have trailing slashes\"\n    severity: error\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    message: \"Every operation must have a summary\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\
  \n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-akamai-prefix:\n    message: \"Operation summaries should start with 'Akamai'\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Akamai\"\n\n  operation-description-required:\n    message: \"Every operation must have a description\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    message: \"Every operation must have an operationId\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    message: \"operationId should use camelCase\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n\
  \        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    message: \"Every operation must have at least one tag\"\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  operation-external-docs:\n    message: \"Operations should have externalDocs linking to Akamai's documentation\"\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: externalDocs\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    message: \"All parameters must have a description\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-description-required:\n    message: \"All responses must have a description\"\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function:\
  \ truthy\n\n  # HTTP METHODS\n  get-no-request-body:\n    message: \"GET operations must not have a request body\"\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-returns-no-content:\n    message: \"DELETE operations should return 204 No Content\"\n    severity: info\n    given: \"$.paths[*].delete.responses\"\n    then:\n      field: \"204\"\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    message: \"Security schemes should be defined\"\n    severity: info\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # TAGS\n  tags-global-defined:\n    message: \"Global tags array should be defined\"\n    severity: info\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/akamai/refs/heads/main/rules/akamai-spectral-rules.yml
tags:
- CDN
- Cloud
- Edge Computing
- Networks
- Platform
- Security
- Spectral
- Linting
- API Governance
---
