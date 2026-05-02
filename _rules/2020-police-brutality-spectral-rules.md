---
api_specs:
- filename: 2020-police-brutality-openapi.yml
  format: yaml
  label: 2020 Police Brutality API
  slug: 2020-police-brutality
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/2020-police-brutality/refs/heads/main/openapi/2020-police-brutality-openapi.yml
categories:
- get
- info
- 'no'
- openapi
- operation
- response
- schema
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for 2020 Police Brutality.
layout: rules
name: 2020 Police Brutality API Rules
provider_name: 2020 Police Brutality
provider_slug: 2020-police-brutality
rule_count: 19
rules:
- description: API info title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: API info description must be present and meaningful.
  given: $.info
  name: info-description-required
  severity: warn
- description: API version must be defined.
  given: $.info
  name: info-version-required
  severity: error
- description: Open data APIs should include a license.
  given: $.info
  name: info-license-required
  severity: warn
- description: Must use OpenAPI 3.0.x.
  given: $
  name: openapi-version-3
  severity: error
- description: Servers array must be defined.
  given: $
  name: servers-must-be-defined
  severity: error
- description: Each server should have a description.
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Every operation must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Component schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schemas should define a type.
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Schema properties should have descriptions.
  given: $.components.schemas[*].properties[*]
  name: schema-properties-described
  severity: info
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Global tags array should be defined for documentation.
  given: $
  name: tags-defined
  severity: info
rules_file: rules/2020-police-brutality-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/2020-police-brutality/refs/heads/main/rules/2020-police-brutality-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 2
  warn: 7
slug: 2020-police-brutality-spectral-rules
source_filename: 2020-police-brutality-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: API info title must be present.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: API info description must be present and meaningful.\n    severity: warn\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API version must be defined.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-license-required:\n    description: Open data APIs should include a license.\n    severity: warn\n    given: $.info\n    then:\n      field: license\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.0.x.\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\
  \\.\"\n\n  # SERVERS\n  servers-must-be-defined:\n    description: Servers array must be defined.\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-description-required:\n    description: Each server should have a description.\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: Every operation should have a description.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n\
  \    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must define at least one 2xx response.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-description-required:\n    description: Every response must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-required:\n    description: Component schemas should have descriptions.\n    severity: warn\n    given: $.components.schemas[*]\n\
  \    then:\n      field: description\n      function: truthy\n\n  schema-type-required:\n    description: Schemas should define a type.\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  schema-properties-described:\n    description: Schema properties should have descriptions.\n    severity: info\n    given: $.components.schemas[*].properties[*]\n    then:\n      field: description\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: warn\n    given: $..description\n    then:\n      function: truthy\n\n  tags-defined:\n    description: Global tags array should be defined for documentation.\n    severity: info\n\
  \    given: $\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/2020-police-brutality/refs/heads/main/rules/2020-police-brutality-spectral-rules.yml
tags:
- Brutality
- Civil Rights
- Policing
- Public Data
- Spectral
- Linting
- API Governance
---
