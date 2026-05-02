---
api_specs:
- filename: activision-blizzard-battle-net.json
  format: json
  label: Battle.net API
  slug: battle-net
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/activision-blizzard/refs/heads/main/openapi/activision-blizzard-battle-net.json
categories:
- http
- info
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for activision-blizzard.
layout: rules
name: activision-blizzard API Rules
provider_name: activision-blizzard
provider_slug: activision-blizzard
rule_count: 23
rules:
- description: API title should start with "Activision Blizzard" or "Battle.net"
  given: $.info.title
  name: info-title-format
  severity: warn
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must include a version
  given: $.info
  name: info-version-required
  severity: error
- description: Should use OpenAPI 3.x
  given: $.openapi
  name: openapi-version
  severity: warn
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: All servers should use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summary should start with "Activision Blizzard"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: OperationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationId-camelCase
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Battle.net data endpoints require namespace parameter
  given: $.paths[/data/**][get].parameters
  name: parameter-namespace-required
  severity: info
- description: Every operation must have a 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should document 401 Unauthorized
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-defined
  severity: warn
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Battle.net API should use OAuth2 authentication
  given: $.components.securitySchemes[*].type
  name: security-oauth2
  severity: warn
- description: GET operations should not have a request body
  given: $.paths[*].get
  name: http-get-no-request-body
  severity: error
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should have example values
  given: $.components.schemas[*].properties[*]
  name: schema-property-examples
  severity: info
rules_file: rules/activision-blizzard-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/activision-blizzard/refs/heads/main/rules/activision-blizzard-spectral-rules.yml
severity_counts:
  error: 9
  hint: 0
  info: 2
  warn: 12
slug: activision-blizzard-spectral-rules
source_filename: activision-blizzard-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-format:\n    description: API title should start with \"Activision Blizzard\" or \"Battle.net\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(Activision Blizzard|Battle\\\\.net)\"\n\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must include a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description: Should use OpenAPI 3.x\n    severity: warn\n    given: $.openapi\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined\n    severity: error\n\
  \    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: All servers should use HTTPS\n    severity: warn\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: warn\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"[^/]/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summary should start with \"Activision Blizzard\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match:\
  \ \"^Activision Blizzard \"\n\n  operation-description-required:\n    description: Every operation should have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-operationId-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationId-camelCase:\n    description: OperationId should use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: casing\n      functionOptions:\n        type: camel\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n\
  \    description: Every parameter must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-namespace-required:\n    description: Battle.net data endpoints require namespace parameter\n    severity: info\n    given: $.paths[/data/**][get].parameters\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            type: object\n            properties:\n              name:\n                enum: ['namespace']\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have a 2xx response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-401-defined:\n\
  \    description: Operations should document 401 Unauthorized\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: '401'\n      function: truthy\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-oauth2:\n    description: Battle.net API should use OAuth2 authentication\n    severity: warn\n    given: $.components.securitySchemes[*].type\n    then:\n      function: enumeration\n      functionOptions:\n        values: ['oauth2']\n\n  # HTTP METHODS\n  http-get-no-request-body:\n    description: GET operations should not have\
  \ a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Component schemas should have descriptions\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-property-examples:\n    description: Schema properties should have example values\n    severity: info\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: example\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/activision-blizzard/refs/heads/main/rules/activision-blizzard-spectral-rules.yml
tags:
- Spectral
- Linting
- API Governance
---
