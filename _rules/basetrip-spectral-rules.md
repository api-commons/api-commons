---
api_specs:
- filename: basetrip-api-openapi.yml
  format: yaml
  label: Basetrip API
  slug: basetrip-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/basetrip/refs/heads/main/openapi/basetrip-api-openapi.yml
categories:
- basetrip
description: Spectral linting rules defining API design standards and conventions for Basetrip.
layout: rules
name: Basetrip API Rules
provider_name: Basetrip
provider_slug: basetrip
rule_count: 15
rules:
- description: All operations must require X-API-Key header authentication.
  given: $.paths.*.*.security
  name: basetrip-api-key-required
  severity: error
- description: All operations must have an operationId.
  given: $.paths.*.*
  name: basetrip-operation-id-required
  severity: error
- description: Operation IDs must use camelCase.
  given: $.paths.*.*.operationId
  name: basetrip-operation-id-camel-case
  severity: warn
- description: All operations must have a summary.
  given: $.paths.*.*
  name: basetrip-summary-required
  severity: error
- description: Operation summaries must use Title Case.
  given: $.paths.*.*.summary
  name: basetrip-summary-title-case
  severity: warn
- description: All operations must be tagged.
  given: $.paths.*.*
  name: basetrip-tags-required
  severity: error
- description: All operations must have a description.
  given: $.paths.*.*
  name: basetrip-description-required
  severity: warn
- description: All GET operations must have a 200 response.
  given: $.paths.*.get.responses
  name: basetrip-200-response-required
  severity: error
- description: Operations should document 401 Unauthorized responses.
  given: $.paths.*.get.responses
  name: basetrip-401-response-defined
  severity: warn
- description: Operations on parameterized paths should document 404 responses.
  given: $.paths[*~/*{id}*].*.responses
  name: basetrip-404-response-defined
  severity: warn
- description: Path segments must use kebab-case.
  given: $.paths[*]~
  name: basetrip-path-kebab-case
  severity: warn
- description: All schema properties should have descriptions.
  given: $.components.schemas.*.properties.*
  name: basetrip-schema-description-required
  severity: warn
- description: Responses should reference schemas using $ref rather than inline definitions.
  given: $.paths.*.*.responses.*.content.application/json.schema
  name: basetrip-response-schema-ref
  severity: warn
- description: API info must include contact details.
  given: $.info
  name: basetrip-info-contact-required
  severity: warn
- description: Server URLs must use HTTPS.
  given: $.servers.*.url
  name: basetrip-server-url-https
  severity: error
rules_file: rules/basetrip-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/basetrip/refs/heads/main/rules/basetrip-spectral-rules.yml
severity_counts:
  error: 6
  hint: 0
  info: 0
  warn: 9
slug: basetrip-spectral-rules
source_filename: basetrip-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  basetrip-api-key-required:\n    description: All operations must require X-API-Key header authentication.\n    message: Operation must include ApiKeyAuth security requirement.\n    severity: error\n    given: $.paths.*.*.security\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            type: object\n            required: [ApiKeyAuth]\n\n  basetrip-operation-id-required:\n    description: All operations must have an operationId.\n    message: Operation is missing operationId.\n    severity: error\n    given: $.paths.*.*\n    then:\n      field: operationId\n      function: truthy\n\n  basetrip-operation-id-camel-case:\n    description: Operation IDs must use camelCase.\n    message: \"{{value}} must use camelCase.\"\n    severity: warn\n    given: $.paths.*.*.operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  basetrip-summary-required:\n\
  \    description: All operations must have a summary.\n    message: Operation is missing summary.\n    severity: error\n    given: $.paths.*.*\n    then:\n      field: summary\n      function: truthy\n\n  basetrip-summary-title-case:\n    description: Operation summaries must use Title Case.\n    message: Summary must use Title Case.\n    severity: warn\n    given: $.paths.*.*.summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9 ]+$\"\n\n  basetrip-tags-required:\n    description: All operations must be tagged.\n    message: Operation must include at least one tag.\n    severity: error\n    given: $.paths.*.*\n    then:\n      field: tags\n      function: truthy\n\n  basetrip-description-required:\n    description: All operations must have a description.\n    message: Operation is missing description.\n    severity: warn\n    given: $.paths.*.*\n    then:\n      field: description\n      function: truthy\n\n  basetrip-200-response-required:\n\
  \    description: All GET operations must have a 200 response.\n    message: GET operation is missing 200 success response.\n    severity: error\n    given: $.paths.*.get.responses\n    then:\n      field: \"200\"\n      function: truthy\n\n  basetrip-401-response-defined:\n    description: Operations should document 401 Unauthorized responses.\n    message: Operation is missing 401 response definition.\n    severity: warn\n    given: $.paths.*.get.responses\n    then:\n      field: \"401\"\n      function: truthy\n\n  basetrip-404-response-defined:\n    description: Operations on parameterized paths should document 404 responses.\n    message: Parameterized path operation is missing 404 response.\n    severity: warn\n    given: \"$.paths[*~/*{id}*].*.responses\"\n    then:\n      field: \"404\"\n      function: truthy\n\n  basetrip-path-kebab-case:\n    description: Path segments must use kebab-case.\n    message: Path segment must use kebab-case.\n    severity: warn\n    given: $.paths[*]~\n\
  \    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z][a-z0-9-]*(/\\\\{[a-zA-Z]+\\\\})?)+$\"\n\n  basetrip-schema-description-required:\n    description: All schema properties should have descriptions.\n    message: Schema property is missing description.\n    severity: warn\n    given: $.components.schemas.*.properties.*\n    then:\n      field: description\n      function: truthy\n\n  basetrip-response-schema-ref:\n    description: Responses should reference schemas using $ref rather than inline definitions.\n    message: Response content should use $ref to reference schemas.\n    severity: warn\n    given: $.paths.*.*.responses.*.content.application/json.schema\n    then:\n      field: \"$ref\"\n      function: truthy\n\n  basetrip-info-contact-required:\n    description: API info must include contact details.\n    message: API info is missing contact information.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function:\
  \ truthy\n\n  basetrip-server-url-https:\n    description: Server URLs must use HTTPS.\n    message: Server URL must use HTTPS.\n    severity: error\n    given: $.servers.*.url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/basetrip/refs/heads/main/rules/basetrip-spectral-rules.yml
tags:
- Cities
- Countries
- Health
- Safety
- Travel
- Visa
- Spectral
- Linting
- API Governance
---
