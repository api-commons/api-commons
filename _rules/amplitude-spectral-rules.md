---
api_specs:
- filename: amplitude-http-v2-api-openapi.yml
  format: yaml
  label: Amplitude HTTP V2 API
  slug: http-v2-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/openapi/amplitude-http-v2-api-openapi.yml
- filename: amplitude-identify-api-openapi.yml
  format: yaml
  label: Amplitude Identify API
  slug: identify-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/openapi/amplitude-identify-api-openapi.yml
- filename: amplitude-dashboard-rest-api-openapi.yml
  format: yaml
  label: Amplitude Dashboard REST API
  slug: dashboard-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/openapi/amplitude-dashboard-rest-api-openapi.yml
- filename: amplitude-export-api-openapi.yml
  format: yaml
  label: Amplitude Export API
  slug: export-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/openapi/amplitude-export-api-openapi.yml
- filename: amplitude-behavioral-cohorts-api-openapi.yml
  format: yaml
  label: Amplitude Behavioral Cohorts API
  slug: behavioral-cohorts-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/openapi/amplitude-behavioral-cohorts-api-openapi.yml
- filename: amplitude-taxonomy-api-openapi.yml
  format: yaml
  label: Amplitude Taxonomy API
  slug: taxonomy-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/openapi/amplitude-taxonomy-api-openapi.yml
- filename: amplitude-attribution-api-openapi.yml
  format: yaml
  label: Amplitude Attribution API
  slug: attribution-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/openapi/amplitude-attribution-api-openapi.yml
- filename: amplitude-chart-annotations-api-openapi.yml
  format: yaml
  label: Amplitude Chart Annotations API
  slug: chart-annotations-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/openapi/amplitude-chart-annotations-api-openapi.yml
- filename: amplitude-user-profile-api-openapi.yml
  format: yaml
  label: Amplitude User Profile API
  slug: user-profile-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/openapi/amplitude-user-profile-api-openapi.yml
- filename: amplitude-user-mapping-api-openapi.yml
  format: yaml
  label: Amplitude User Mapping API
  slug: user-mapping-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/openapi/amplitude-user-mapping-api-openapi.yml
- filename: amplitude-scim-api-openapi.yml
  format: yaml
  label: Amplitude SCIM API
  slug: scim-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/openapi/amplitude-scim-api-openapi.yml
- filename: amplitude-dsar-api-openapi.yml
  format: yaml
  label: Amplitude Data Subject Access Request API
  slug: dsar-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/openapi/amplitude-dsar-api-openapi.yml
- filename: amplitude-experiment-evaluation-api-openapi.yml
  format: yaml
  label: Amplitude Experiment Evaluation API
  slug: experiment-evaluation-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/openapi/amplitude-experiment-evaluation-api-openapi.yml
- filename: amplitude-experiment-management-api-openapi.yml
  format: yaml
  label: Amplitude Experiment Management API
  slug: experiment-management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/openapi/amplitude-experiment-management-api-openapi.yml
categories:
- delete
- get
- info
- 'no'
- openapi
- operation
- parameter
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amplitude.
layout: rules
name: Amplitude API Rules
provider_name: Amplitude
provider_slug: amplitude
rule_count: 23
rules:
- description: API title must start with "Amplitude"
  given: $.info.title
  name: info-title-has-provider
  severity: warn
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: Servers array must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Amplitude"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-amplitude-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
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
- description: Every parameter must have a description
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Query and path parameter names should use snake_case
  given: $.paths[*][*].parameters[?(@.in=='query' || @.in=='path')].name
  name: parameter-snake-case
  severity: info
- description: Every operation must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should document a 401 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-error-401
  severity: warn
- description: Every response must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Schemas should have an explicit type
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Security schemes must be defined if security is used
  given: $.components
  name: security-schemes-defined
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/amplitude-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/rules/amplitude-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 2
  warn: 9
slug: amplitude-spectral-rules
source_filename: amplitude-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: \"spectral:oas\"\nrules:\n\n  # INFO / METADATA\n  info-title-has-provider:\n    description: API title must start with \"Amplitude\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amplitude\"\n\n  info-description-required:\n    description: Info object must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info object must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.x\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers array must be defined\n    severity: error\n\
  \    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: All server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-amplitude-prefix:\n    description: Operation summaries should start with \"Amplitude\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Amplitude\"\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field:\
  \ description\n      function: truthy\n\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-camel-case:\n    description: operationId should use camelCase\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\
  \n  parameter-snake-case:\n    description: Query and path parameter names should use snake_case\n    severity: info\n    given: \"$.paths[*][*].parameters[?(@.in=='query' || @.in=='path')].name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_]*$\"\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have at least one 2xx response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-error-401:\n    description: Operations should document a 401 response\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          required: ['401']\n\n  response-description-required:\n\
  \    description: Every response must have a description\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-property-description:\n    description: Schema properties should have descriptions\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-type-required:\n    description: Schemas should have an explicit type\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined if security is used\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given:\
  \ \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/rules/amplitude-spectral-rules.yml
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
- Spectral
- Linting
- API Governance
---
