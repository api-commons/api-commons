---
api_specs:
- filename: basiq-api-openapi.yml
  format: yaml
  label: Basiq API
  slug: basiq-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/basiq/refs/heads/main/openapi/basiq-api-openapi.yml
categories:
- basiq
description: Spectral linting rules defining API design standards and conventions for Basiq.
layout: rules
name: Basiq API Rules
provider_name: Basiq
provider_slug: basiq
rule_count: 15
rules:
- description: All protected operations must use BearerAuth security.
  given: $.paths[?(!@property.match('token'))].*.security
  name: basiq-bearer-auth-required
  severity: error
- description: All operations must have an operationId.
  given: $.paths.*.*
  name: basiq-operation-id-required
  severity: error
- description: Operation IDs must use camelCase.
  given: $.paths.*.*.operationId
  name: basiq-operation-id-camel-case
  severity: warn
- description: All operations must have a summary.
  given: $.paths.*.*
  name: basiq-summary-required
  severity: error
- description: Operation summaries must use Title Case.
  given: $.paths.*.*.summary
  name: basiq-summary-title-case
  severity: warn
- description: All operations must be tagged.
  given: $.paths.*.*
  name: basiq-tags-required
  severity: error
- description: All operations must have a description.
  given: $.paths.*.*
  name: basiq-description-required
  severity: warn
- description: All GET operations must define a 200 response.
  given: $.paths.*.get.responses
  name: basiq-200-response-required
  severity: error
- description: Parameterized path operations should define a 404 response.
  given: $.paths.*.get.responses
  name: basiq-404-response-required
  severity: warn
- description: User-scoped resource paths should be nested under /users/{userId}.
  given: $.paths[*]~
  name: basiq-user-path-prefix
  severity: warn
- description: Responses should reference schemas using $ref rather than inline definitions.
  given: $.paths.*.*.responses.*.content.application/json.schema
  name: basiq-response-schema-ref
  severity: warn
- description: All schema properties should have descriptions.
  given: $.components.schemas.*.properties.*
  name: basiq-schema-description-required
  severity: warn
- description: API info must include contact details.
  given: $.info
  name: basiq-info-contact-required
  severity: warn
- description: Server URLs must use HTTPS.
  given: $.servers.*.url
  name: basiq-server-url-https
  severity: error
- description: DELETE operations should return 204 No Content.
  given: $.paths.*.delete.responses
  name: basiq-204-delete-response
  severity: warn
rules_file: rules/basiq-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/basiq/refs/heads/main/rules/basiq-spectral-rules.yml
severity_counts:
  error: 6
  hint: 0
  info: 0
  warn: 9
slug: basiq-spectral-rules
source_filename: basiq-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  basiq-bearer-auth-required:\n    description: All protected operations must use BearerAuth security.\n    message: Operation must include BearerAuth security requirement.\n    severity: error\n    given: $.paths[?(!@property.match('token'))].*.security\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            type: object\n            required: [BearerAuth]\n\n  basiq-operation-id-required:\n    description: All operations must have an operationId.\n    message: Operation is missing operationId.\n    severity: error\n    given: $.paths.*.*\n    then:\n      field: operationId\n      function: truthy\n\n  basiq-operation-id-camel-case:\n    description: Operation IDs must use camelCase.\n    message: \"{{value}} must use camelCase.\"\n    severity: warn\n    given: $.paths.*.*.operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n\
  \  basiq-summary-required:\n    description: All operations must have a summary.\n    message: Operation is missing summary.\n    severity: error\n    given: $.paths.*.*\n    then:\n      field: summary\n      function: truthy\n\n  basiq-summary-title-case:\n    description: Operation summaries must use Title Case.\n    message: Summary must use Title Case.\n    severity: warn\n    given: $.paths.*.*.summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9 ]+$\"\n\n  basiq-tags-required:\n    description: All operations must be tagged.\n    message: Operation must include at least one tag.\n    severity: error\n    given: $.paths.*.*\n    then:\n      field: tags\n      function: truthy\n\n  basiq-description-required:\n    description: All operations must have a description.\n    message: Operation is missing description.\n    severity: warn\n    given: $.paths.*.*\n    then:\n      field: description\n      function: truthy\n\n  basiq-200-response-required:\n\
  \    description: All GET operations must define a 200 response.\n    message: GET operation is missing 200 success response.\n    severity: error\n    given: $.paths.*.get.responses\n    then:\n      field: \"200\"\n      function: truthy\n\n  basiq-404-response-required:\n    description: Parameterized path operations should define a 404 response.\n    message: Operation on parameterized path is missing 404 response.\n    severity: warn\n    given: $.paths.*.get.responses\n    then:\n      field: \"404\"\n      function: truthy\n\n  basiq-user-path-prefix:\n    description: User-scoped resource paths should be nested under /users/{userId}.\n    message: Resource path should be nested under /users/{userId}.\n    severity: warn\n    given: $.paths[*]~\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/(token|users)\"\n\n  basiq-response-schema-ref:\n    description: Responses should reference schemas using $ref rather than inline definitions.\n    message:\
  \ Response content should use $ref to reference schemas.\n    severity: warn\n    given: $.paths.*.*.responses.*.content.application/json.schema\n    then:\n      field: \"$ref\"\n      function: truthy\n\n  basiq-schema-description-required:\n    description: All schema properties should have descriptions.\n    message: Schema property is missing description.\n    severity: warn\n    given: $.components.schemas.*.properties.*\n    then:\n      field: description\n      function: truthy\n\n  basiq-info-contact-required:\n    description: API info must include contact details.\n    message: API info is missing contact information.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  basiq-server-url-https:\n    description: Server URLs must use HTTPS.\n    message: Server URL must use HTTPS.\n    severity: error\n    given: $.servers.*.url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  basiq-204-delete-response:\n\
  \    description: DELETE operations should return 204 No Content.\n    message: DELETE operation should define a 204 response.\n    severity: warn\n    given: $.paths.*.delete.responses\n    then:\n      field: \"204\"\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/basiq/refs/heads/main/rules/basiq-spectral-rules.yml
tags:
- Australia
- Banking
- CDR
- Financial Data
- Fintech
- Open Banking
- Transactions
- Spectral
- Linting
- API Governance
---
