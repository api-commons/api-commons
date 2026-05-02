---
api_specs:
- filename: aerodatabox-openapi.yml
  format: yaml
  label: AeroDataBox Flight API
  slug: aerodatabox-flight-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/aerodatabox/refs/heads/main/openapi/aerodatabox-openapi.yml
- filename: aerodatabox-openapi.yml
  format: yaml
  label: AeroDataBox Aircraft API
  slug: aerodatabox-aircraft-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/aerodatabox/refs/heads/main/openapi/aerodatabox-openapi.yml
- filename: aerodatabox-openapi.yml
  format: yaml
  label: AeroDataBox Airport API
  slug: aerodatabox-airport-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/aerodatabox/refs/heads/main/openapi/aerodatabox-openapi.yml
- filename: aerodatabox-openapi.yml
  format: yaml
  label: AeroDataBox Statistical API
  slug: aerodatabox-statistical-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/aerodatabox/refs/heads/main/openapi/aerodatabox-openapi.yml
- filename: aerodatabox-openapi.yml
  format: yaml
  label: AeroDataBox Flight Alert API
  slug: aerodatabox-flight-alert-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/aerodatabox/refs/heads/main/openapi/aerodatabox-openapi.yml
categories:
- get
- info
- microcks
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for AeroDataBox.
layout: rules
name: AeroDataBox API Rules
provider_name: AeroDataBox
provider_slug: aerodatabox
rule_count: 22
rules:
- description: API info must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: API info must have a description.
  given: $.info
  name: info-description-required
  severity: warn
- description: API info must have a version.
  given: $.info
  name: info-version-required
  severity: error
- description: APIs should use OpenAPI 3.x specification.
  given: $
  name: openapi-version-3
  severity: warn
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*]
  name: servers-https-only
  severity: error
- description: Path must not have a trailing slash.
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Path must not contain a query string.
  given: $.paths[*]~
  name: paths-no-query-string
  severity: error
- description: Path segments should use kebab-case.
  given: $.paths[*]~
  name: paths-kebab-case
  severity: info
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "AeroDataBox".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-aerodatabox-prefix
  severity: warn
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Every operation must have at least one response.
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Security schemes should be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Each operation should have x-microcks-operation for mock server support.
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-present
  severity: info
rules_file: rules/aerodatabox-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/aerodatabox/refs/heads/main/rules/aerodatabox-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 3
  warn: 8
slug: aerodatabox-spectral-rules
source_filename: aerodatabox-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: API info must have a title.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: API info must have a description.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API info must have a version.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: APIs should use OpenAPI 3.x specification.\n    severity: warn\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function:\
  \ truthy\n\n  servers-https-only:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  # PATHS — NAMING CONVENTIONS\n  paths-no-trailing-slash:\n    description: Path must not have a trailing slash.\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  paths-no-query-string:\n    description: Path must not contain a query string.\n    severity: error\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\?\"\n\n  paths-kebab-case:\n    description: Path segments should use kebab-case.\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}-]+)+$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description:\
  \ Every operation must have a summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-aerodatabox-prefix:\n    description: Operation summaries should start with \"AeroDataBox\".\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^AeroDataBox \"\n\n  operation-description-required:\n    description: Every operation should have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have at least\
  \ one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Every parameter must have a schema.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: schema\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have at least one response.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: responses\n      function: truthy\n\n  response-description-required:\n    description: Every response must have a description.\n    severity: error\n    given:\
  \ \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Top-level schemas should have a description.\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes should be defined in components.\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  microcks-operation-present:\n    description: Each operation should have x-microcks-operation for mock server support.\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete]\"\
  \n    then:\n      field: x-microcks-operation\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/aerodatabox/refs/heads/main/rules/aerodatabox-spectral-rules.yml
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
- Spectral
- Linting
- API Governance
---
