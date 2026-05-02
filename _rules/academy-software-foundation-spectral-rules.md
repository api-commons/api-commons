---
api_specs:
- filename: academy-software-foundation-opencue.yaml
  format: yaml
  label: OpenCue
  slug: opencue
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/academy-software-foundation/refs/heads/main/openapi/academy-software-foundation-opencue.yaml
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
- servers
description: Spectral linting rules defining API design standards and conventions for Academy Software Foundation.
layout: rules
name: Academy Software Foundation API Rules
provider_name: Academy Software Foundation
provider_slug: academy-software-foundation
rule_count: 21
rules:
- description: Info title must be present and start with "Academy Software Foundation"
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present and be descriptive
  given: $.info
  name: info-description-required
  severity: error
- description: Info version must be present
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.0.x
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-required
  severity: error
- description: Servers should have descriptions
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Path segments should use kebab-case or snake_case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with the provider name
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Path and query parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Parameters should have example values
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-example-recommended
  severity: info
- description: Every operation must have a 2xx success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description-recommended
  severity: info
- description: GET operations must not have request bodies
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have request bodies
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/academy-software-foundation-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/academy-software-foundation/refs/heads/main/rules/academy-software-foundation-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 2
  warn: 5
slug: academy-software-foundation-spectral-rules
source_filename: academy-software-foundation-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: Info title must be present and start with \"Academy Software Foundation\"\n    severity: error\n    given: '$.info'\n    then:\n      field: title\n      function: pattern\n      functionOptions:\n        match: '^Academy Software Foundation'\n\n  info-description-required:\n    description: Info description must be present and be descriptive\n    severity: error\n    given: '$.info'\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info version must be present\n    severity: error\n    given: '$.info'\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.0.x\n    severity: error\n    given: '$'\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: '^3\\.0\\.'\n\n  # SERVERS\n  servers-required:\n    description: At least\
  \ one server must be defined\n    severity: error\n    given: '$'\n    then:\n      field: servers\n      function: truthy\n\n  servers-description-required:\n    description: Servers should have descriptions\n    severity: warn\n    given: '$.servers[*]'\n    then:\n      field: description\n      function: truthy\n\n  # PATHS\n  paths-kebab-case:\n    description: Path segments should use kebab-case or snake_case\n    severity: warn\n    given: '$.paths'\n    then:\n      field: '@key'\n      function: pattern\n      functionOptions:\n        match: '^(\\/[a-z0-9_\\-\\{\\}]*)*$'\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with the provider name\n    severity: warn\n    given: '$.paths[*][get,post,put,patch,delete]'\n\
  \    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: '^Academy Software Foundation'\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete]'\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Path and query parameters must have descriptions\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].parameters[*]'\n\
  \    then:\n      field: description\n      function: truthy\n\n  parameter-example-recommended:\n    description: Parameters should have example values\n    severity: info\n    given: '$.paths[*][get,post,put,patch,delete].parameters[*]'\n    then:\n      field: example\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have a 2xx success response\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].responses'\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: '$.paths[*][get,post,put,patch,delete].responses[*]'\n    then:\n      field: description\n      function: truthy\n\n  # SCHEMAS\n  schema-description-recommended:\n    description: Component\
  \ schemas should have descriptions\n    severity: warn\n    given: '$.components.schemas[*]'\n    then:\n      field: description\n      function: truthy\n\n  schema-property-description-recommended:\n    description: Schema properties should have descriptions\n    severity: info\n    given: '$.components.schemas[*].properties[*]'\n    then:\n      field: description\n      function: truthy\n\n  # HTTP CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have request bodies\n    severity: error\n    given: '$.paths[*].get'\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have request bodies\n    severity: warn\n    given: '$.paths[*].delete'\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: '$..description'\n    then:\n      function: pattern\n\
  \      functionOptions:\n        match: '.+'\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/academy-software-foundation/refs/heads/main/rules/academy-software-foundation-spectral-rules.yml
tags:
- Animation
- Color Management
- Film
- Linux Foundation
- Open Source
- Rendering
- Standards
- Visual Effects
- VFX
- Spectral
- Linting
- API Governance
---
