---
api_specs:
- filename: microsoft-edge-addons-api.yaml
  format: yaml
  label: Microsoft Edge Add-ons API
  slug: edge-addons-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/microsoft-edge/refs/heads/main/openapi/microsoft-edge-addons-api.yaml
- filename: microsoft-edge-devtools-api.yaml
  format: yaml
  label: Microsoft Edge DevTools Protocol HTTP API
  slug: edge-devtools-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/microsoft-edge/refs/heads/main/openapi/microsoft-edge-devtools-api.yaml
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
- tags
description: Spectral linting rules defining API design standards and conventions for Microsoft Edge.
layout: rules
name: Microsoft Edge API Rules
provider_name: Microsoft Edge
provider_slug: microsoft-edge
rule_count: 27
rules:
- description: Info title must start with "Microsoft Edge"
  given: $.info.title
  name: info-title-prefix
  severity: error
- description: Info description is required
  given: $.info
  name: info-description-required
  severity: error
- description: Info description should be at least 50 characters
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: Info version is required
  given: $.info
  name: info-version-required
  severity: error
- description: Info contact is required
  given: $.info
  name: info-contact-required
  severity: warn
- description: OpenAPI version should be 3.0.x
  given: $.openapi
  name: openapi-version
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Path segments should use kebab-case
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
- description: Operation summary should start with "Microsoft Edge"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Tags should use Title Case
  given: $.paths[*][get,post,put,patch,delete].tags[*]
  name: tags-title-case
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Every operation must have a success response (2xx)
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schemas should have a type defined
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Security schemes should be defined when security is used
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations should not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions should not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/microsoft-edge-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/microsoft-edge/refs/heads/main/rules/microsoft-edge-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 0
  warn: 12
slug: microsoft-edge-spectral-rules
source_filename: microsoft-edge-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-prefix:\n    description: Info title must start with \"Microsoft Edge\"\n    severity: error\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: ^Microsoft Edge\n  info-description-required:\n    description: Info description is required\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n  info-description-min-length:\n    description: Info description should be at least 50 characters\n    severity: warn\n    given: $.info.description\n    then:\n      function: length\n      functionOptions:\n        min: 50\n  info-version-required:\n    description: Info version is required\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n  info-contact-required:\n    description: Info contact is required\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\
  \n  # OPENAPI VERSION\n  openapi-version:\n    description: OpenAPI version should be 3.0.x\n    severity: error\n    given: $.openapi\n    then:\n      function: pattern\n      functionOptions:\n        match: ^3\\.0\\.\\d+$\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n  servers-description:\n    description: Each server should have a description\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # PATHS - NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: warn\n    given: $.paths\n    then:\n      field: '@key'\n      function: pattern\n      functionOptions:\n        match: ^(/[a-z0-9\\-\\{\\}\\.]+)+$\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: error\n    given: $.paths\n    then:\n\
  \      field: '@key'\n      function: pattern\n      functionOptions:\n        notMatch: .+\\/$\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n  operation-summary-prefix:\n    description: Operation summary should start with \"Microsoft Edge\"\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: ^Microsoft Edge\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n\
  \      field: operationId\n      function: truthy\n  operation-operationid-camel-case:\n    description: operationId should use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: ^[a-z][a-zA-Z0-9]*$\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tags-title-case:\n    description: Tags should use Title Case\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].tags[*]\n    then:\n      function: pattern\n      functionOptions:\n        match: ^[A-Z]\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n\
  \      function: truthy\n  parameter-schema-required:\n    description: Every parameter must have a schema\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have a success response (2xx)\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['202']\n            - required: ['204']\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Top-level schemas should have\
  \ descriptions\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n  schema-type-required:\n    description: Schemas should have a type defined\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes should be defined when security is used\n    severity: warn\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations should not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n  delete-no-request-body:\n    description: DELETE operations should not have a request body\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n\
  \  no-empty-descriptions:\n    description: Descriptions should not be empty strings\n    severity: error\n    given: $..description\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/microsoft-edge/refs/heads/main/rules/microsoft-edge-spectral-rules.yml
tags:
- Browser
- Chromium
- Developer Tools
- Edge
- Extensions
- Microsoft
- Progressive Web Apps
- Web Development
- WebView
- Spectral
- Linting
- API Governance
---
