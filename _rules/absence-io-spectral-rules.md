---
api_specs:
- filename: absence-io-openapi.yml
  format: yaml
  label: Absence.io API
  slug: absence-io
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/absence-io/refs/heads/main/openapi/absence-io-openapi.yml
categories:
- examples
- id
- info
- list
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- server
- servers
- tag
- tags
description: Spectral linting rules defining API design standards and conventions for Absence.io.
layout: rules
name: Absence.io API Rules
provider_name: Absence.io
provider_slug: absence-io
rule_count: 30
rules:
- description: API info must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: API title should follow the "Absence.io ..." naming pattern.
  given: $.info.title
  name: info-title-format
  severity: warn
- description: API info must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: API info must have a version.
  given: $.info
  name: info-version-required
  severity: error
- description: API must use OpenAPI 3.x.
  given: $
  name: openapi-version
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-required
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: server-https-required
  severity: error
- description: Path segments should use lowercase with optional underscores.
  given: $.paths
  name: paths-lowercase
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Absence.io".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: OperationIds must use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined.
  given: $
  name: tags-array-defined
  severity: warn
- description: Each global tag should have a description.
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Every operation must have at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every authenticated operation should have a 401 response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: All schemas should have a type defined.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Schema property names should use snake_case or camelCase.
  given: $.components.schemas[*].properties
  name: schema-properties-snake-case
  severity: info
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Every operation should have security defined.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-security-defined
  severity: warn
- description: Absence.io uses POST for list operations (not GET). This is a provider-specific pattern.
  given: $.paths
  name: list-operations-use-post
  severity: info
- description: List request bodies should include skip and limit for pagination.
  given: $.paths[*].post.requestBody.content.application/json.schema.properties
  name: list-request-skip-limit
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have examples for better developer experience.
  given: $.paths[*][get,post,put,patch,delete].responses[*].content[*]
  name: examples-encouraged
  severity: info
- description: Absence.io uses MongoDB-style _id fields (not id). Ensure IDs follow this convention.
  given: $.components.schemas[*].properties
  name: id-field-naming
  severity: info
rules_file: rules/absence-io-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/absence-io/refs/heads/main/rules/absence-io-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 5
  warn: 11
slug: absence-io-spectral-rules
source_filename: absence-io-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: API info must have a title.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-title-format:\n    description: API title should follow the \"Absence.io ...\" naming pattern.\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Absence\\\\.io\"\n\n  info-description-required:\n    description: API info must have a description.\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API info must have a version.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version:\n    description: API must use OpenAPI 3.x.\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n\
  \        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-required:\n    description: At least one server must be defined.\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  server-https-required:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS — NAMING CONVENTIONS\n  paths-lowercase:\n    description: Path segments should use lowercase with optional underscores.\n    severity: warn\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9_/-]+(\\\\{[a-zA-Z0-9_]+\\\\})?)*$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description:\
  \ Operation summaries should start with \"Absence.io\".\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Absence\\\\.io\"\n\n  operation-description-required:\n    description: Every operation should have a description.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-camelcase:\n    description: OperationIds must use camelCase.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description:\
  \ Every operation must have at least one tag.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tags-array-defined:\n    description: Global tags array should be defined.\n    severity: warn\n    given: $\n    then:\n      field: tags\n      function: truthy\n\n  tag-description-required:\n    description: Each global tag should have a description.\n    severity: warn\n    given: $.tags[*]\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have at least one 2xx response.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n\
  \    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-401-required:\n    description: Every authenticated operation should have a 401 response.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          required: ['401']\n\n  response-description-required:\n    description: All responses must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Top-level schemas should have descriptions.\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-type-defined:\n    description: All schemas\
  \ should have a type defined.\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  schema-properties-snake-case:\n    description: Schema property names should use snake_case or camelCase.\n    severity: info\n    given: $.components.schemas[*].properties\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  operation-security-defined:\n    description: Every operation should have security defined.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: security\n      function: truthy\n\n  # ABSENCE.IO SPECIFIC — POST for listing\n  list-operations-use-post:\n    description: Absence.io uses POST for list operations (not\
  \ GET). This is a provider-specific pattern.\n    severity: info\n    given: $.paths\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n\n  # PAGINATION\n  list-request-skip-limit:\n    description: List request bodies should include skip and limit for pagination.\n    severity: info\n    given: $.paths[*].post.requestBody.content.application/json.schema.properties\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: error\n    given: $..description\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n\n  examples-encouraged:\n    description: Operations should have examples for better developer experience.\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].responses[*].content[*]\n    then:\n      function: schema\n    \
  \  functionOptions:\n        schema:\n          anyOf:\n            - required: ['example']\n            - required: ['examples']\n\n  # MONGOOSE IDS\n  id-field-naming:\n    description: Absence.io uses MongoDB-style _id fields (not id). Ensure IDs follow this convention.\n    severity: info\n    given: $.components.schemas[*].properties\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/absence-io/refs/heads/main/rules/absence-io-spectral-rules.yml
tags:
- Absences
- Employees
- Leave Management
- HR
- Spectral
- Linting
- API Governance
---
