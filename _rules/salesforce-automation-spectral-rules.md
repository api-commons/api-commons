---
api_specs:
- filename: salesforce-rest-api-openapi.json
  format: json
  label: Salesforce REST API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce-automation/refs/heads/main/openapi/salesforce-rest-api-openapi.json
- filename: salesforce-bulk-api-openapi.json
  format: json
  label: Salesforce Bulk API 2.0
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce-automation/refs/heads/main/openapi/salesforce-bulk-api-openapi.json
- filename: salesforce-streaming-api-openapi.json
  format: json
  label: Salesforce Streaming API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce-automation/refs/heads/main/openapi/salesforce-streaming-api-openapi.json
- filename: salesforce-platform-events-api-openapi.json
  format: json
  label: Salesforce Platform Events API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce-automation/refs/heads/main/openapi/salesforce-platform-events-api-openapi.json
- filename: salesforce-analytics-api-openapi.json
  format: json
  label: Salesforce Analytics API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce-automation/refs/heads/main/openapi/salesforce-analytics-api-openapi.json
- filename: salesforce-tooling-api-openapi.json
  format: json
  label: Salesforce Tooling API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce-automation/refs/heads/main/openapi/salesforce-tooling-api-openapi.json
- filename: salesforce-connect-rest-api-openapi.json
  format: json
  label: Salesforce Connect REST API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce-automation/refs/heads/main/openapi/salesforce-connect-rest-api-openapi.json
- filename: salesforce-change-data-capture-api-openapi.json
  format: json
  label: Salesforce Change Data Capture API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce-automation/refs/heads/main/openapi/salesforce-change-data-capture-api-openapi.json
- filename: salesforce-invocable-actions-api-openapi.json
  format: json
  label: Salesforce Invocable Actions API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce-automation/refs/heads/main/openapi/salesforce-invocable-actions-api-openapi.json
- filename: salesforce-composite-api-openapi.json
  format: json
  label: Salesforce Composite API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce-automation/refs/heads/main/openapi/salesforce-composite-api-openapi.json
- filename: salesforce-apex-rest-api-openapi.json
  format: json
  label: Salesforce Apex REST API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/salesforce-automation/refs/heads/main/openapi/salesforce-apex-rest-api-openapi.json
categories:
- delete
- examples
- get
- info
- 'no'
- oauth2
- openapi
- operation
- parameter
- paths
- post
- request
- response
- schema
- security
- servers
- tag
description: Spectral linting rules defining API design standards and conventions for Salesforce Automation.
layout: rules
name: Salesforce Automation API Rules
provider_name: Salesforce Automation
provider_slug: salesforce-automation
rule_count: 37
rules:
- description: Info object must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: Info title should start with "Salesforce".
  given: $.info.title
  name: info-title-salesforce-prefix
  severity: warn
- description: Info object must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: Info description should be at least 50 characters.
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: Info object must have a version.
  given: $.info
  name: info-version-required
  severity: error
- description: Info object should have contact information.
  given: $.info
  name: info-contact-required
  severity: warn
- description: Info object should include license information.
  given: $.info
  name: info-license-required
  severity: info
- description: OpenAPI version should be 3.1.0.
  given: $
  name: openapi-version
  severity: warn
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS.
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Each server should have a description.
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Paths must not include query strings.
  given: $.paths
  name: paths-no-query-strings
  severity: error
- description: Path segments should use kebab-case or camelCase (no underscores).
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: operationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Salesforce".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-salesforce-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Tags should have descriptions.
  given: $.tags[*]
  name: tag-description
  severity: info
- description: Every parameter must have a description.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema.
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must have at least one success response (2xx).
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Authenticated endpoints should define a 401 response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: info
- description: Schemas must define a type.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description
  severity: info
- description: Global security must be defined.
  given: $
  name: security-defined
  severity: error
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: POST operations should have a request body.
  given: $.paths[*].post
  name: post-request-body-required
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
- description: Salesforce APIs should use OAuth 2.0 authentication.
  given: $.components.securitySchemes
  name: oauth2-security
  severity: warn
rules_file: rules/salesforce-automation-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/salesforce-automation/refs/heads/main/rules/salesforce-automation-spectral-rules.yml
severity_counts:
  error: 18
  hint: 0
  info: 7
  warn: 12
slug: salesforce-automation-spectral-rules
source_filename: salesforce-automation-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # ============================================================\n  # INFO / METADATA\n  # ============================================================\n  info-title-required:\n    description: Info object must have a title.\n    given: $.info\n    severity: error\n    then:\n      field: title\n      function: truthy\n\n  info-title-salesforce-prefix:\n    description: Info title should start with \"Salesforce\".\n    given: $.info.title\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Salesforce\"\n\n  info-description-required:\n    description: Info object must have a description.\n    given: $.info\n    severity: error\n    then:\n      field: description\n      function: truthy\n\n  info-description-min-length:\n    description: Info description should be at least 50 characters.\n    given: $.info.description\n    severity: warn\n    then:\n      function: length\n      functionOptions:\n        min: 50\n\n  info-version-required:\n\
  \    description: Info object must have a version.\n    given: $.info\n    severity: error\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Info object should have contact information.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n\n  info-license-required:\n    description: Info object should include license information.\n    given: $.info\n    severity: info\n    then:\n      field: license\n      function: truthy\n\n  # ============================================================\n  # OPENAPI VERSION\n  # ============================================================\n  openapi-version:\n    description: OpenAPI version should be 3.1.0.\n    given: $\n    severity: warn\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # ============================================================\n  # SERVERS\n  # ============================================================\n\
  \  servers-defined:\n    description: At least one server must be defined.\n    given: $\n    severity: error\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs should use HTTPS.\n    given: $.servers[*].url\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description:\n    description: Each server should have a description.\n    given: $.servers[*]\n    severity: warn\n    then:\n      field: description\n      function: truthy\n\n  # ============================================================\n  # PATHS - NAMING CONVENTIONS\n  # ============================================================\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes.\n    given: $.paths\n    severity: error\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n\n  paths-no-query-strings:\n \
  \   description: Paths must not include query strings.\n    given: $.paths\n    severity: error\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\?\"\n\n  paths-kebab-case:\n    description: Path segments should use kebab-case or camelCase (no underscores).\n    given: $.paths\n    severity: info\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"_\"\n\n  # ============================================================\n  # OPERATIONS\n  # ============================================================\n  operation-operationid-required:\n    description: Every operation must have an operationId.\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-camel-case:\n    description: operationId should use camelCase.\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    severity:\
  \ warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-summary-required:\n    description: Every operation must have a summary.\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-salesforce-prefix:\n    description: Operation summaries should start with \"Salesforce\".\n    given: $.paths[*][get,post,put,patch,delete].summary\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Salesforce\"\n\n  operation-description-required:\n    description: Every operation must have a description.\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n    then:\n      field: description\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    given: $.paths[*][get,post,put,patch,delete]\n    severity: error\n\
  \    then:\n      field: tags\n      function: truthy\n\n  # ============================================================\n  # TAGS\n  # ============================================================\n  tag-description:\n    description: Tags should have descriptions.\n    given: $.tags[*]\n    severity: info\n    then:\n      field: description\n      function: truthy\n\n  # ============================================================\n  # PARAMETERS\n  # ============================================================\n  parameter-description-required:\n    description: Every parameter must have a description.\n    given: $.paths[*][*].parameters[*]\n    severity: warn\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Every parameter must have a schema.\n    given: $.paths[*][*].parameters[*]\n    severity: error\n    then:\n      field: schema\n      function: truthy\n\n  # ============================================================\n\
  \  # REQUEST BODIES\n  # ============================================================\n  request-body-json-content:\n    description: Request bodies should use application/json content type.\n    given: $.paths[*][post,put,patch].requestBody.content\n    severity: warn\n    then:\n      field: application/json\n      function: truthy\n\n  # ============================================================\n  # RESPONSES\n  # ============================================================\n  response-success-required:\n    description: Every operation must have at least one success response (2xx).\n    given: $.paths[*][get,post,put,patch,delete].responses\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"202\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: Every response must have a description.\n\
  \    given: $.paths[*][*].responses[*]\n    severity: error\n    then:\n      field: description\n      function: truthy\n\n  response-401-required:\n    description: Authenticated endpoints should define a 401 response.\n    given: $.paths[*][get,post,put,patch,delete].responses\n    severity: info\n    then:\n      field: \"401\"\n      function: truthy\n\n  # ============================================================\n  # SCHEMAS - PROPERTY NAMING\n  # ============================================================\n  schema-type-defined:\n    description: Schemas must define a type.\n    given: $.components.schemas[*]\n    severity: warn\n    then:\n      field: type\n      function: truthy\n\n  schema-description:\n    description: Top-level schemas should have descriptions.\n    given: $.components.schemas[*]\n    severity: info\n    then:\n      field: description\n      function: truthy\n\n  # ============================================================\n  # SECURITY\n  # ============================================================\n\
  \  security-defined:\n    description: Global security must be defined.\n    given: $\n    severity: error\n    then:\n      field: security\n      function: truthy\n\n  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    given: $.components\n    severity: error\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # ============================================================\n  # HTTP METHOD CONVENTIONS\n  # ============================================================\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    given: $.paths[*].get\n    severity: error\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body.\n    given: $.paths[*].delete\n    severity: warn\n    then:\n      field: requestBody\n      function: falsy\n\n  post-request-body-required:\n    description: POST operations\
  \ should have a request body.\n    given: $.paths[*].post\n    severity: info\n    then:\n      field: requestBody\n      function: truthy\n\n  # ============================================================\n  # GENERAL QUALITY\n  # ============================================================\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    given: $..description\n    severity: error\n    then:\n      function: truthy\n\n  examples-encouraged:\n    description: Schema properties should include example values.\n    given: $.components.schemas[*].properties[*]\n    severity: info\n    then:\n      field: example\n      function: truthy\n\n  oauth2-security:\n    description: Salesforce APIs should use OAuth 2.0 authentication.\n    given: $.components.securitySchemes\n    severity: warn\n    then:\n      field: oauth2\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/salesforce-automation/refs/heads/main/rules/salesforce-automation-spectral-rules.yml
tags:
- Automation
- Cloud
- CRM
- Enterprise
- Sales
- Spectral
- Linting
- API Governance
---
