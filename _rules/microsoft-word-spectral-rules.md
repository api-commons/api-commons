---
api_specs:
- filename: microsoft-word-graph-api.yaml
  format: yaml
  label: Microsoft Graph Word API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/microsoft-word/refs/heads/main/openapi/microsoft-word-graph-api.yaml
- filename: microsoft-word-javascript-api.yaml
  format: yaml
  label: Office JavaScript API for Word
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/microsoft-word/refs/heads/main/openapi/microsoft-word-javascript-api.yaml
- filename: microsoft-word-open-xml-sdk.yaml
  format: yaml
  label: Open XML SDK for Word
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/microsoft-word/refs/heads/main/openapi/microsoft-word-open-xml-sdk.yaml
categories:
- delete
- examples
- get
- info
- microcks
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
description: Spectral linting rules defining API design standards and conventions for Microsoft Word.
layout: rules
name: Microsoft Word API Rules
provider_name: Microsoft Word
provider_slug: microsoft-word
rule_count: 39
rules:
- description: Info title must be present and non-empty.
  given: $.info
  name: info-title-required
  severity: error
- description: Info title should start with 'Microsoft Word'.
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info description must be present.
  given: $.info
  name: info-description-required
  severity: error
- description: Info description should be at least 50 characters.
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: Info version must be present.
  given: $.info
  name: info-version-required
  severity: error
- description: Info should include contact information.
  given: $.info
  name: info-contact-required
  severity: warn
- description: Info should include license information.
  given: $.info
  name: info-license-required
  severity: info
- description: OpenAPI version must be 3.0.x.
  given: $
  name: openapi-version
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS.
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: Each server should have a description.
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Path segments should use kebab-case.
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with 'Microsoft Word'.
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: OperationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined.
  given: $
  name: tags-defined
  severity: warn
- description: Each tag should have a description.
  given: $.tags[*]
  name: tags-description
  severity: info
- description: Every parameter must have a description.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema with a type.
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should specify application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must have at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Operations should include a 401 Unauthorized response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: GET operations should include a 404 Not Found response.
  given: $.paths[*].get.responses
  name: response-404-for-get
  severity: warn
- description: All schemas must have a type defined.
  given: $.components.schemas[*]
  name: schema-type-required
  severity: error
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should use camelCase naming.
  given: $.components.schemas[*].properties
  name: schema-properties-camelcase
  severity: warn
- description: Global security must be defined.
  given: $
  name: security-defined
  severity: error
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: OAuth2 security scheme should be defined for Microsoft Graph APIs.
  given: $.components.securitySchemes
  name: security-schemes-oauth2
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
- description: Operations should include x-microcks-operation extension.
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/microsoft-word-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/microsoft-word/refs/heads/main/rules/microsoft-word-spectral-rules.yml
severity_counts:
  error: 18
  hint: 0
  info: 4
  warn: 17
slug: microsoft-word-spectral-rules
source_filename: microsoft-word-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # ─── INFO / METADATA ───────────────────────────────────────────────\n  info-title-required:\n    description: Info title must be present and non-empty.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-title-prefix:\n    description: Info title should start with 'Microsoft Word'.\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Microsoft Word\"\n\n  info-description-required:\n    description: Info description must be present.\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-description-min-length:\n    description: Info description should be at least 50 characters.\n    severity: warn\n    given: $.info.description\n    then:\n      function: length\n      functionOptions:\n        min: 50\n\n  info-version-required:\n    description: Info version must be present.\n    severity:\
  \ error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Info should include contact information.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  info-license-required:\n    description: Info should include license information.\n    severity: info\n    given: $.info\n    then:\n      field: license\n      function: truthy\n\n  # ─── OPENAPI VERSION ───────────────────────────────────────────────\n  openapi-version:\n    description: OpenAPI version must be 3.0.x.\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # ─── SERVERS ────────────────────────────────────────────────────────\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n\
  \    description: Server URLs should use HTTPS.\n    severity: warn\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description:\n    description: Each server should have a description.\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # ─── PATHS — NAMING CONVENTIONS ────────────────────────────────────\n  paths-kebab-case:\n    description: Path segments should use kebab-case.\n    severity: warn\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}()'=-]+)+$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes.\n    severity: error\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # ─── OPERATIONS ─────────────────────────────────────────────────────\n\
  \  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with 'Microsoft Word'.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Microsoft Word\"\n\n  operation-description-required:\n    description: Every operation must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-camelcase:\n    description:\
  \ OperationId should use camelCase.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # ─── TAGS ───────────────────────────────────────────────────────────\n  tags-defined:\n    description: Global tags array should be defined.\n    severity: warn\n    given: $\n    then:\n      field: tags\n      function: truthy\n\n  tags-description:\n    description: Each tag should have a description.\n    severity: info\n    given: $.tags[*]\n    then:\n      field: description\n      function: truthy\n\n  # ─── PARAMETERS ─────────────────────────────────────────────────────\n  parameter-description-required:\n    description: Every parameter must\
  \ have a description.\n    severity: warn\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Every parameter must have a schema with a type.\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: schema\n      function: truthy\n\n  # ─── REQUEST BODIES ─────────────────────────────────────────────────\n  request-body-json-content:\n    description: Request bodies should specify application/json content type.\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      field: application/json\n      function: truthy\n\n  # ─── RESPONSES ──────────────────────────────────────────────────────\n  response-success-required:\n    description: Every operation must have at least one 2xx response.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n\
  \        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['202']\n            - required: ['204']\n\n  response-description-required:\n    description: Every response must have a description.\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-401-required:\n    description: Operations should include a 401 Unauthorized response.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: '401'\n      function: truthy\n\n  response-404-for-get:\n    description: GET operations should include a 404 Not Found response.\n    severity: warn\n    given: $.paths[*].get.responses\n    then:\n      field: '404'\n      function: truthy\n\n  # ─── SCHEMAS — PROPERTY NAMING ──────────────────────────────────────\n  schema-type-required:\n    description: All schemas must have a type defined.\n    severity:\
  \ error\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  schema-description-required:\n    description: Top-level schemas should have descriptions.\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-properties-camelcase:\n    description: Schema properties should use camelCase naming.\n    severity: warn\n    given: $.components.schemas[*].properties\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^[a-z@$][a-zA-Z0-9.@]*$\"\n\n  # ─── SECURITY ───────────────────────────────────────────────────────\n  security-defined:\n    description: Global security must be defined.\n    severity: error\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    severity: error\n    given: $.components\n    then:\n\
  \      field: securitySchemes\n      function: truthy\n\n  security-schemes-oauth2:\n    description: OAuth2 security scheme should be defined for Microsoft Graph APIs.\n    severity: warn\n    given: $.components.securitySchemes\n    then:\n      field: oauth2\n      function: truthy\n\n  # ─── HTTP METHOD CONVENTIONS ────────────────────────────────────────\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body.\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  # ─── GENERAL QUALITY ────────────────────────────────────────────────\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: error\n    given: $..description\n    then:\n      function:\
  \ truthy\n\n  examples-encouraged:\n    description: Schema properties should include example values.\n    severity: info\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: example\n      function: truthy\n\n  microcks-operation-extension:\n    description: Operations should include x-microcks-operation extension.\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/microsoft-word/refs/heads/main/rules/microsoft-word-spectral-rules.yml
tags:
- Documents
- Microsoft 365
- Office
- Productivity
- Word Processing
- Spectral
- Linting
- API Governance
---
