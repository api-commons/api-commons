---
api_specs:
- filename: microsoft-visio-graph-api.yaml
  format: yaml
  label: Microsoft Graph Visio API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/microsoft-visio/refs/heads/main/openapi/microsoft-visio-graph-api.yaml
categories:
- get
- info
- openapi
- operation
- parameter
- response
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Microsoft Visio.
layout: rules
name: Microsoft Visio API Rules
provider_name: Microsoft Visio
provider_slug: microsoft-visio
rule_count: 16
rules:
- description: Info title must contain 'Microsoft' or 'Visio'
  given: $.info.title
  name: info-title-must-contain-microsoft-visio
  severity: error
- description: Info description is required
  given: $.info
  name: info-description-required
  severity: error
- description: Info version is required
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: Servers array must be defined
  given: $
  name: servers-must-be-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with 'Microsoft Visio'
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Parameters must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must define a success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should define a 401 Unauthorized response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-recommended
  severity: warn
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
rules_file: rules/microsoft-visio-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/microsoft-visio/refs/heads/main/rules/microsoft-visio-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 0
  warn: 4
slug: microsoft-visio-spectral-rules
source_filename: microsoft-visio-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-must-contain-microsoft-visio:\n    description: Info title must contain 'Microsoft' or 'Visio'\n    given: $.info.title\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: (Microsoft|Visio)\n  info-description-required:\n    description: Info description is required\n    given: $.info\n    severity: error\n    then:\n      field: description\n      function: truthy\n  info-version-required:\n    description: Info version is required\n    given: $.info\n    severity: error\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.x\n    given: $.openapi\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-must-be-defined:\n    description: Servers array must be defined\n    given: $\n    severity: error\n    then:\n      field: servers\n\
  \      function: truthy\n  servers-https-required:\n    description: All server URLs must use HTTPS\n    given: $.servers[*].url\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # OPERATIONS\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n  operation-summary-required:\n    description: Every operation must have a summary\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n    then:\n      field: summary\n      function: truthy\n  operation-summary-prefix:\n    description: Operation summaries should start with 'Microsoft Visio'\n    given: $.paths[*][get,post,put,patch,delete].summary\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Microsoft Visio\"\n  operation-tags-required:\n\
  \    description: Every operation must have at least one tag\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n    then:\n      field: tags\n      function: truthy\n  operation-operationid-camel-case:\n    description: operationId should use camelCase\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Parameters must have a description\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    severity: warn\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must define a success response\n    given: $.paths[*][get,post,put,patch,delete].responses\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n    \
  \        - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n  response-401-recommended:\n    description: Operations should define a 401 Unauthorized response\n    given: $.paths[*][get,post,put,patch,delete].responses\n    severity: warn\n    then:\n      field: \"401\"\n      function: truthy\n\n  # SECURITY\n  security-global-defined:\n    description: Global security must be defined\n    given: $\n    severity: error\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    given: $.paths[*].get\n    severity: error\n    then:\n      field: requestBody\n      function: falsy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/microsoft-visio/refs/heads/main/rules/microsoft-visio-spectral-rules.yml
tags:
- Business Process
- Diagramming
- Flowcharts
- Microsoft 365
- Visualization
- Spectral
- Linting
- API Governance
---
