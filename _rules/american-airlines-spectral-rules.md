---
api_specs:
- filename: american-airlines-runway-developer-api-openapi.yml
  format: yaml
  label: American Airlines Runway Developer API
  slug: runway-developer-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/american-airlines/refs/heads/main/openapi/american-airlines-runway-developer-api-openapi.yml
categories:
- get
- info
- operation
- parameter
- paths
- response
- schema
- servers
description: Spectral linting rules defining API design standards and conventions for American Airlines.
layout: rules
name: American Airlines API Rules
provider_name: American Airlines
provider_slug: american-airlines
rule_count: 12
rules:
- description: API title must start with "American Airlines"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Operations must have a success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: info
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Parameters should have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
rules_file: rules/american-airlines-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/american-airlines/refs/heads/main/rules/american-airlines-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 1
  warn: 3
slug: american-airlines-spectral-rules
source_filename: american-airlines-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: spectral:oas\nrules:\n  info-title-prefix:\n    description: API title must start with \"American Airlines\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^American Airlines\"\n\n  info-description-required:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  servers-defined:\n    description: At least one server must be defined\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  operation-summary-required:\n    description: Operations must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n\
  \    then:\n      field: summary\n      function: truthy\n\n  operation-id-required:\n    description: Operations must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: Operations must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  response-success-required:\n    description: Operations must have a success response\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n\
  \      field: requestBody\n      function: falsy\n\n  paths-kebab-case:\n    description: Path segments should use kebab-case\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(\\\\/([a-z0-9-]+|\\\\{[a-zA-Z]+\\\\}))*$\"\n\n  schema-description-required:\n    description: Component schemas should have descriptions\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-description-required:\n    description: Parameters should have descriptions\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/american-airlines/refs/heads/main/rules/american-airlines-spectral-rules.yml
tags:
- Airlines
- Aviation
- Flights
- Travel
- Booking
- Developer Experience
- Spectral
- Linting
- API Governance
---
