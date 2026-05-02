---
api_specs:
- filename: amnic-openapi.yml
  format: yaml
  label: Amnic Cloud Cost Observability API
  slug: amnic-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amnic/refs/heads/main/openapi/amnic-openapi.yml
categories:
- examples
- get
- info
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
description: Spectral linting rules defining API design standards and conventions for Amnic.
layout: rules
name: Amnic API Rules
provider_name: Amnic
provider_slug: amnic
rule_count: 31
rules:
- description: API title should start with "Amnic".
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API info must have a description of at least 20 characters.
  given: $.info
  name: info-description-required
  severity: error
- description: API info must define a version.
  given: $.info
  name: info-version-required
  severity: error
- description: API info should include contact information.
  given: $.info
  name: info-contact-required
  severity: warn
- description: OpenAPI version must be 3.0.x.
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Each server should have a description.
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Path segments should use kebab-case (lowercase with hyphens).
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes.
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Amnic".
  given: $.paths[*][get,post,put,patch,delete,head,options].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete,head,options].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined.
  given: $
  name: tags-global-defined
  severity: warn
- description: Global tags should have descriptions.
  given: $.tags[*]
  name: tags-description
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: Query and path parameter names should use snake_case or kebab-case.
  given: $.paths[*][*].parameters[?(@.in == 'query')].name
  name: parameter-snake-case
  severity: warn
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-content-type
  severity: warn
- description: Every operation must have at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Operations with security should document a 401 response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema property names should use snake_case.
  given: $.components.schemas[*].properties[*]~
  name: schema-property-snake-case
  severity: warn
- description: Security schemes must be defined in components.
  given: $.components
  name: security-scheme-defined
  severity: error
- description: Global security should be defined.
  given: $
  name: security-global-defined
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should include examples for better documentation.
  given: $.paths[*][*].responses[*].content[*]
  name: examples-encouraged
  severity: info
rules_file: rules/amnic-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amnic/refs/heads/main/rules/amnic-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 1
  warn: 15
slug: amnic-spectral-rules
source_filename: amnic-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-prefix:\n    description: API title should start with \"Amnic\".\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: '^Amnic'\n\n  info-description-required:\n    description: API info must have a description of at least 20 characters.\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API info must define a version.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API info should include contact information.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: OpenAPI version must be 3.0.x.\n    severity: error\n    given: $.openapi\n    then:\n      function: pattern\n   \
  \   functionOptions:\n        match: '^3\\.0\\.'\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: '^https://'\n\n  servers-description:\n    description: Each server should have a description.\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # PATHS - NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case (lowercase with hyphens).\n    severity: warn\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        match: '^(/[a-z0-9{}-]+)+$'\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes.\n    severity:\
  \ error\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: '/$'\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"Amnic\".\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: '^Amnic'\n\n  operation-description-required:\n    description: Every operation should have a description.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n\
  \    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId should use camelCase.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-zA-Z0-9]*$'\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tags-global-defined:\n    description: Global tags array should be defined.\n    severity: warn\n    given: $\n    then:\n      field: tags\n      function: truthy\n\n  tags-description:\n    description: Global tags should have descriptions.\n    severity: warn\n    given: $.tags[*]\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every\
  \ parameter must have a description.\n    severity: error\n    given: $.paths[*][*].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-snake-case:\n    description: Query and path parameter names should use snake_case or kebab-case.\n    severity: warn\n    given: $.paths[*][*].parameters[?(@.in == 'query')].name\n    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-z0-9_]*$'\n\n  # REQUEST BODIES\n  request-body-content-type:\n    description: Request bodies should use application/json content type.\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      field: application/json\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have at least one 2xx response.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: responses\n      function: truthy\n\n  response-401-required:\n\
  \    description: Operations with security should document a 401 response.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: '401'\n      function: truthy\n\n  response-description-required:\n    description: Every response must have a description.\n    severity: error\n    given: $.paths[*][*].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS - PROPERTY NAMING\n  schema-description-required:\n    description: Top-level schemas should have a description.\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-property-snake-case:\n    description: Schema property names should use snake_case.\n    severity: warn\n    given: $.components.schemas[*].properties[*]~\n    then:\n      function: pattern\n      functionOptions:\n        match: '^[a-z][a-z0-9_]*$'\n\n  # SECURITY\n  security-scheme-defined:\n    description: Security\
  \ schemes must be defined in components.\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-global-defined:\n    description: Global security should be defined.\n    severity: warn\n    given: $\n    then:\n      field: security\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: error\n    given: $..description\n    then:\n      function: pattern\n      functionOptions:\n        match: '.+'\n\n  examples-encouraged:\n    description: Operations should include examples for better documentation.\n    severity: info\n    given: $.paths[*][*].responses[*].content[*]\n    then:\n      field: examples\n\
  \      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amnic/refs/heads/main/rules/amnic-spectral-rules.yml
tags:
- Cloud Cost Observability
- FinOps
- Cloud Cost Management
- Cost Optimization
- Kubernetes
- Azure
- Google Cloud
- Spectral
- Linting
- API Governance
---
