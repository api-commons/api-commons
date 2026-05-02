---
api_specs:
- filename: google-forms-api.yaml
  format: yaml
  label: Google Forms API v1
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/google-forms/refs/heads/main/openapi/google-forms-api.yaml
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
- tag
description: Spectral linting rules defining API design standards and conventions for Google Forms.
layout: rules
name: Google Forms API Rules
provider_name: Google Forms
provider_slug: google-forms
rule_count: 27
rules:
- description: Info object must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: Info title should start with Google Forms
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
- description: OpenAPI version must be 3.0.x
  given: $
  name: openapi-version
  severity: error
- description: Servers array must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: operationId should be camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Operation summaries should start with Google Forms
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-title-case
  severity: info
- description: Tag names should use Title Case
  given: $.tags[*].name
  name: tag-title-case
  severity: warn
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Parameters must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Operations must define a success response (2xx)
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should define a 401 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schemas should have a type defined
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: error
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations must not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $.paths[*][get,post,put,patch,delete].description
  name: no-empty-descriptions
  severity: error
rules_file: rules/google-forms-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/google-forms/refs/heads/main/rules/google-forms-spectral-rules.yml
severity_counts:
  error: 16
  hint: 0
  info: 1
  warn: 10
slug: google-forms-spectral-rules
source_filename: google-forms-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-required:\n    description: Info object must have a title\n    given: $.info\n    severity: error\n    then:\n      field: title\n      function: truthy\n\n  info-title-prefix:\n    description: Info title should start with Google Forms\n    given: $.info.title\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Google Forms\"\n\n  info-description-required:\n    description: Info object must have a description\n    given: $.info\n    severity: error\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must have a version\n    given: $.info\n    severity: error\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description: OpenAPI version must be 3.0.x\n    given: $\n    severity: error\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n\
  \        match: \"^3\\\\.0\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers array must be defined\n    given: $\n    severity: error\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    given: $.servers[*].url\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS - NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    given: $.paths\n    severity: warn\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^(/v[0-9]+)?(/[a-z][a-z0-9-]*(/{[a-zA-Z]+})?)*(:?[a-zA-Z]+)?$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    given: $.paths\n    severity: error\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n\
  \    description: Operations must have a summary\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: Operations must have a description\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n    description: Operations must have an operationId\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-camel-case:\n    description: operationId should be camelCase\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Operations must have at least one tag\n    given: $.paths[*][get,post,put,patch,delete]\n\
  \    severity: warn\n    then:\n      field: tags\n      function: truthy\n\n  operation-summary-title-case:\n    description: Operation summaries should start with Google Forms\n    given: $.paths[*][get,post,put,patch,delete].summary\n    severity: info\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Google Forms \"\n\n  # TAGS\n  tag-title-case:\n    description: Tag names should use Title Case\n    given: $.tags[*].name\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z]+\"\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Parameters must have descriptions\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    severity: warn\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Parameters must have a schema\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    severity: error\n    then:\n\
  \      field: schema\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must define a success response (2xx)\n    given: $.paths[*][get,post,put,patch,delete].responses\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"202\"]\n            - required: [\"204\"]\n\n  response-401-required:\n    description: Operations should define a 401 response\n    given: $.paths[*][get,post,put,patch,delete].responses\n    severity: warn\n    then:\n      field: \"401\"\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Top-level schemas should have descriptions\n    given: $.components.schemas[*]\n    severity: warn\n    then:\n      field: description\n      function: truthy\n\n  schema-type-required:\n    description: Schemas should have a type defined\n\
  \    given: $.components.schemas[*]\n    severity: warn\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-global-defined:\n    description: Global security must be defined\n    given: $\n    severity: error\n    then:\n      field: security\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes must be defined\n    given: $.components\n    severity: error\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    given: $.paths[*].get\n    severity: error\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations must not have a request body\n    given: $.paths[*].delete\n    severity: warn\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must\
  \ not be empty strings\n    given: $.paths[*][get,post,put,patch,delete].description\n    severity: error\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/google-forms/refs/heads/main/rules/google-forms-spectral-rules.yml
tags:
- Data Collection
- Forms
- Google
- Google Workspace
- Questionnaires
- Responses
- Surveys
- Spectral
- Linting
- API Governance
---
