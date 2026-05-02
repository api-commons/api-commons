---
api_specs:
- filename: amazon-iot-twinmaker-openapi-original.yml
  format: yaml
  label: AWS IoT TwinMaker API
  slug: aws-iot-twinmaker-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-twinmaker/refs/heads/main/openapi/amazon-iot-twinmaker-openapi-original.yml
categories:
- get
- info
- 'no'
- openapi
- operation
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon IoT TwinMaker.
layout: rules
name: Amazon IoT TwinMaker API Rules
provider_name: Amazon IoT TwinMaker
provider_slug: amazon-iot-twinmaker
rule_count: 14
rules:
- description: Info title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: API version must be specified.
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x.
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*]
  name: servers-https-only
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with 'Amazon IoT TwinMaker'.
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: Every response must have a description.
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: warn
- description: Schemas should define an explicit type.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: info
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Security schemes should be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: warn
rules_file: rules/amazon-iot-twinmaker-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-twinmaker/refs/heads/main/rules/amazon-iot-twinmaker-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 1
  warn: 5
slug: amazon-iot-twinmaker-spectral-rules
source_filename: amazon-iot-twinmaker-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n  info-version-required:\n    description: API version must be specified.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n  openapi-version-3:\n    description: Must use OpenAPI 3.x.\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n  servers-https-only:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*]\"\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  operation-summary-required:\n\
  \    description: Every operation must have a summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n  operation-summary-prefix:\n    description: Operation summaries must start with 'Amazon IoT TwinMaker'.\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: pattern\n      functionOptions:\n        match: \"^Amazon IoT TwinMaker\"\n  operation-id-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: tags\n      function: truthy\n  response-description-required:\n    description: Every response must\
  \ have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].responses[*]\"\n    then:\n      field: description\n      function: truthy\n  schema-type-defined:\n    description: Schemas should define an explicit type.\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: truthy\n  security-schemes-defined:\n    description: Security schemes should be defined in components.\n    severity: warn\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-twinmaker/refs/heads/main/rules/amazon-iot-twinmaker-spectral-rules.yml
tags:
- 3D Visualization
- Digital Twin
- Industrial IoT
- IoT
- Spectral
- Linting
- API Governance
---
