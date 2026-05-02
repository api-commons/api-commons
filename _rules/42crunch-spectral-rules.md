---
api_specs:
- filename: 42crunch-scand-manager.yaml
  format: yaml
  label: 42Crunch API Conformance Scan Jobs Manager
  slug: 42crunch-scand-manager
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/42crunch/refs/heads/main/openapi/42crunch-scand-manager.yaml
categories:
- delete
- examples
- get
- info
- 'no'
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
- tags
description: Spectral linting rules defining API design standards and conventions for 42Crunch.
layout: rules
name: 42Crunch API Rules
provider_name: 42Crunch
provider_slug: 42crunch
rule_count: 43
rules:
- description: The info object must have a non-empty title.
  given: $.info
  name: info-title-required
  severity: error
- description: API title must start with "42Crunch" to identify the provider.
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: The info object must have a description with at least 30 characters.
  given: $.info
  name: info-description-required
  severity: warn
- description: The info object must specify a version.
  given: $.info
  name: info-version-required
  severity: error
- description: The info object should include contact information.
  given: $.info
  name: info-contact-required
  severity: info
- description: All specs must use OpenAPI 3.0.x.
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: warn
- description: Every server must have a description.
  given: $.servers[*]
  name: servers-description
  severity: info
- description: Path segments must use kebab-case (lowercase letters, numbers, hyphens).
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not end with a trailing slash.
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Paths must not contain query strings; use parameters instead.
  given: $.paths[*]~
  name: paths-no-query-string
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "42Crunch" for consistency.
  given: $.paths[*][get,post,put,patch,delete,options,head].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-id-required
  severity: error
- description: operationId must use camelCase format.
  given: $.paths[*][get,post,put,patch,delete,options,head].operationId
  name: operation-id-camel-case
  severity: warn
- description: operationId should start with a standard verb (list, get, create, update, delete, check, run, search).
  given: $.paths[*][get,post,put,patch,delete,options,head].operationId
  name: operation-id-verb-prefix
  severity: info
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-tags-required
  severity: error
- description: Operations should include x-microcks-operation for mock server compatibility.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-microcks-extension
  severity: info
- description: Global tags array should be defined with descriptions.
  given: $
  name: tags-global-defined
  severity: warn
- description: Tag names must use Title Case (e.g., "Jobs", "Health", "Logs").
  given: $.tags[*].name
  name: tags-title-case
  severity: warn
- description: Each global tag should have a description.
  given: $.tags[*]
  name: tags-description-required
  severity: info
- description: Every parameter must have a description.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema.
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Query parameter names should use snake_case or kebab-case.
  given: $.paths[*][*].parameters[?(@.in == 'query')].name
  name: parameter-name-kebab-case
  severity: info
- description: Request bodies should specify application/json as content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Request body schemas should include examples for documentation and mocking.
  given: $.paths[*][post,put,patch].requestBody.content.application/json
  name: request-body-examples
  severity: info
- description: Every operation must have at least one 2xx success response.
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Every operation should have a 400 Bad Request response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-400-required
  severity: warn
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Success responses should return application/json content.
  given: $.paths[*][get,post,put,patch].responses[?(@property.match(/^2/))]
  name: response-json-content
  severity: warn
- description: Error responses (4xx) should use the Error schema with an 'error' field.
  given: $.paths[*][*].responses[?(@property.match(/^4/))]
  name: response-error-schema
  severity: warn
- description: All schemas in components must have a type defined.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: All component schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should have descriptions.
  given: $.components.schemas[*].properties[*]
  name: schema-properties-description
  severity: info
- description: Schemas should set additionalProperties to false for strict validation.
  given: $.components.schemas[*]
  name: schema-additional-properties-false
  severity: info
- description: Schema properties must not be empty objects without type or $ref.
  given: $.components.schemas[*].properties[*]
  name: schema-no-empty-properties
  severity: warn
- description: All security schemes must have descriptions.
  given: $.components.securitySchemes[*]
  name: security-schemes-described
  severity: warn
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
  name: post-has-request-body
  severity: warn
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/42crunch-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/42crunch/refs/heads/main/rules/42crunch-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 10
  warn: 21
slug: 42crunch-spectral-rules
source_filename: 42crunch-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # ─── INFO / METADATA ────────────────────────────────────────────────────────\n\n  info-title-required:\n    description: The info object must have a non-empty title.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-title-prefix:\n    description: API title must start with \"42Crunch\" to identify the provider.\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^42Crunch\"\n\n  info-description-required:\n    description: The info object must have a description with at least 30 characters.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: minLength\n      functionOptions:\n        value: 30\n\n  info-version-required:\n    description: The info object must specify a version.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n\
  \    description: The info object should include contact information.\n    severity: info\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # ─── OPENAPI VERSION ────────────────────────────────────────────────────────\n\n  openapi-version-3:\n    description: All specs must use OpenAPI 3.0.x.\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # ─── SERVERS ────────────────────────────────────────────────────────────────\n\n  servers-defined:\n    description: At least one server must be defined.\n    severity: warn\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-description:\n    description: Every server must have a description.\n    severity: info\n    given: \"$.servers[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # ─── PATHS — NAMING CONVENTIONS ─────────────────────────────────────────────\n\
  \n  paths-kebab-case:\n    description: Path segments must use kebab-case (lowercase letters, numbers, hyphens).\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}-]+)+$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not end with a trailing slash.\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  paths-no-query-string:\n    description: Paths must not contain query strings; use parameters instead.\n    severity: error\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\?\"\n\n  # ─── OPERATIONS ─────────────────────────────────────────────────────────────\n\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n\
  \      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries must start with \"42Crunch\" for consistency.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,options,head].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^42Crunch\"\n\n  operation-description-required:\n    description: Every operation must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId must use camelCase format.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,options,head].operationId\"\
  \n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-id-verb-prefix:\n    description: operationId should start with a standard verb (list, get, create, update, delete, check, run, search).\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete,options,head].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(list|get|create|update|delete|check|run|search|health)[A-Z]\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: tags\n      function: truthy\n\n  operation-microcks-extension:\n    description: Operations should include x-microcks-operation for mock server compatibility.\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: x-microcks-operation\n      function: truthy\n\
  \n  # ─── TAGS ───────────────────────────────────────────────────────────────────\n\n  tags-global-defined:\n    description: Global tags array should be defined with descriptions.\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  tags-title-case:\n    description: Tag names must use Title Case (e.g., \"Jobs\", \"Health\", \"Logs\").\n    severity: warn\n    given: \"$.tags[*].name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z ]*$\"\n\n  tags-description-required:\n    description: Each global tag should have a description.\n    severity: info\n    given: \"$.tags[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # ─── PARAMETERS ─────────────────────────────────────────────────────────────\n\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field:\
  \ description\n      function: truthy\n\n  parameter-schema-required:\n    description: Every parameter must have a schema.\n    severity: error\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  parameter-name-kebab-case:\n    description: Query parameter names should use snake_case or kebab-case.\n    severity: info\n    given: \"$.paths[*][*].parameters[?(@.in == 'query')].name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_-]*$\"\n\n  # ─── REQUEST BODIES ─────────────────────────────────────────────────────────\n\n  request-body-json-content:\n    description: Request bodies should specify application/json as content type.\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      function: truthy\n\n  request-body-examples:\n    description: Request body schemas should include examples for documentation and mocking.\n    severity: info\n \
  \   given: \"$.paths[*][post,put,patch].requestBody.content.application/json\"\n    then:\n      field: examples\n      function: truthy\n\n  # ─── RESPONSES ──────────────────────────────────────────────────────────────\n\n  response-success-required:\n    description: Every operation must have at least one 2xx success response.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-400-required:\n    description: Every operation should have a 400 Bad Request response.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      field: \"400\"\n      function: truthy\n\n  response-description-required:\n    description: Every response must have a description.\n    severity: error\n    given: \"$.paths[*][*].responses[*]\"\n    then:\n      field: description\n \
  \     function: truthy\n\n  response-json-content:\n    description: Success responses should return application/json content.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch].responses[?(@property.match(/^2/))]\"\n    then:\n      field: content\n      function: truthy\n\n  response-error-schema:\n    description: Error responses (4xx) should use the Error schema with an 'error' field.\n    severity: warn\n    given: \"$.paths[*][*].responses[?(@property.match(/^4/))]\"\n    then:\n      field: content\n      function: truthy\n\n  # ─── SCHEMAS — PROPERTY NAMING ──────────────────────────────────────────────\n\n  schema-type-defined:\n    description: All schemas in components must have a type defined.\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  schema-description-required:\n    description: All component schemas should have a description.\n    severity: warn\n    given: \"$.components.schemas[*]\"\
  \n    then:\n      field: description\n      function: truthy\n\n  schema-properties-description:\n    description: Schema properties should have descriptions.\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-additional-properties-false:\n    description: Schemas should set additionalProperties to false for strict validation.\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: additionalProperties\n      function: defined\n\n  schema-no-empty-properties:\n    description: Schema properties must not be empty objects without type or $ref.\n    severity: warn\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      function: truthy\n\n  # ─── SECURITY ────────────────────────────────────────────────────────────────\n\n  security-schemes-described:\n    description: All security schemes must have descriptions.\n    severity: warn\n    given: \"$.components.securitySchemes[*]\"\
  \n    then:\n      field: description\n      function: truthy\n\n  # ─── HTTP METHOD CONVENTIONS ─────────────────────────────────────────────────\n\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body.\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  post-has-request-body:\n    description: POST operations should have a request body.\n    severity: warn\n    given: \"$.paths[*].post\"\n    then:\n      field: requestBody\n      function: truthy\n\n  # ─── GENERAL QUALITY ─────────────────────────────────────────────────────────\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: error\n    given: \"$..description\"\n    then:\n  \
  \    function: truthy\n\n  examples-encouraged:\n    description: Schema properties should include example values.\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: example\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/42crunch/refs/heads/main/rules/42crunch-spectral-rules.yml
tags:
- API Security
- Platform
- Scanning
- Security
- OpenAPI
- DevSecOps
- Spectral
- Linting
- API Governance
---
