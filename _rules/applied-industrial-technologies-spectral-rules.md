---
api_specs:
- filename: applied-industrial-technologies-openapi.yaml
  format: yaml
  label: Applied Industrial Technologies API
  slug: applied-industrial-technologies-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/applied-industrial-technologies/refs/heads/main/openapi/applied-industrial-technologies-openapi.yaml
categories:
- http
- info
- 'no'
- operation
- parameter
- paths
- response
- schema
- servers
description: Spectral linting rules defining API design standards and conventions for Applied Industrial Technologies.
layout: rules
name: Applied Industrial Technologies API Rules
provider_name: Applied Industrial Technologies
provider_slug: applied-industrial-technologies
rule_count: 16
rules:
- description: API title must be present
  given: $.info
  name: info-title-required
  severity: error
- description: API version must be specified
  given: $.info
  name: info-version-required
  severity: error
- description: API description should be present
  given: $.info
  name: info-description-required
  severity: warn
- description: At least one server must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https
  severity: warn
- description: Path segments must use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must have a 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: operation-success-response-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Component schemas should have a title
  given: $.components.schemas[*]
  name: schema-title-required
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: http-get-no-request-body
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/applied-industrial-technologies-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/applied-industrial-technologies/refs/heads/main/rules/applied-industrial-technologies-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 0
  warn: 8
slug: applied-industrial-technologies-spectral-rules
source_filename: applied-industrial-technologies-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: API title must be present\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-version-required:\n    description: API version must be specified\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-description-required:\n    description: API description should be present\n    severity: warn\n    given: $.info\n    then:\n      field: description\n      function: minLength\n      functionOptions:\n        min: 20\n\n  # SERVERS\n  servers-required:\n    description: At least one server must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\
  \n\n  # PATHS\n  paths-kebab-case:\n    description: Path segments must use kebab-case\n    severity: warn\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}/_-]+)+$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have\
  \ at least one tag\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  operation-success-response-required:\n    description: Every operation must have a 2xx response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n\
  \      function: truthy\n\n  # SCHEMAS\n  schema-title-required:\n    description: Component schemas should have a title\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: title\n      function: truthy\n\n  http-get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: warn\n    given: $..description\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/applied-industrial-technologies/refs/heads/main/rules/applied-industrial-technologies-spectral-rules.yml
tags:
- Industrial Distribution
- Bearings
- Power Transmission
- Fluid Power
- Supply Chain
- Spectral
- Linting
- API Governance
---
