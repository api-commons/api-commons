---
api_specs:
- filename: codehooks-database-rest-api-openapi.yml
  format: yaml
  label: Codehooks Database REST API
  slug: codehooks-database-rest-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/codehooks/refs/heads/main/openapi/codehooks-database-rest-api-openapi.yml
- filename: codehooks-events-asyncapi.yml
  format: yaml
  label: Codehooks Events (AsyncAPI)
  slug: codehooks-events
  spec_type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/codehooks/refs/heads/main/asyncapi/codehooks-events-asyncapi.yml
categories:
- codehooks
description: Spectral linting rules defining API design standards and conventions for Codehooks.
layout: rules
name: Codehooks API Rules
provider_name: Codehooks
provider_slug: codehooks
rule_count: 10
rules:
- description: API contact information must be present.
  given: $.info
  name: codehooks-info-contact
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: codehooks-server-https
  severity: error
- description: Codehooks server URL must use the {projectId}.api.codehooks.io/{space} template.
  given: $.servers[?(@.url && @.url.indexOf('codehooks.io') > -1)].url
  name: codehooks-server-template
  severity: warn
- description: An API key security scheme must be defined.
  given: $.components.securitySchemes[*]
  name: codehooks-apikey-security
  severity: error
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: codehooks-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: codehooks-operation-tags
  severity: warn
- description: Collection-level paths should be declared as /{collection} or sub-paths thereof.
  given: $.paths
  name: codehooks-collection-path
  severity: info
- description: Mutating operations should declare 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: codehooks-error-responses
  severity: warn
- description: List endpoints should accept the q query parameter for MongoDB-style filters.
  given: $.paths['/{collection}'].get.parameters[*]
  name: codehooks-query-parameter
  severity: info
- description: List endpoints should accept the h hints query parameter (sort, fields, offset, limit).
  given: $.paths['/{collection}'].get.parameters[*].name
  name: codehooks-pagination-hints
  severity: info
rules_file: rules/codehooks-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/codehooks/refs/heads/main/rules/codehooks-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 3
  warn: 3
slug: codehooks-rules
source_filename: codehooks-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for Codehooks REST API specifications.\n# Tuned to {projectId}.api.codehooks.io conventions: HTTPS-only, API key\n# authentication, project-scoped servers with the {projectId}/{space}\n# template, MongoDB-style query parameters, and standard CRUD operationIds.\nrules:\n  codehooks-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  codehooks-server-https:\n    description: All server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  codehooks-server-template:\n    description: Codehooks server URL must use the {projectId}.api.codehooks.io/{space} template.\n    severity: warn\n    given: \"$.servers[?(@.url && @.url.indexOf('codehooks.io') > -1)].url\"\n    then:\n      function:\
  \ pattern\n      functionOptions:\n        match: \"\\\\{projectId\\\\}\\\\.api\\\\.codehooks\\\\.io/\\\\{space\\\\}\"\n\n  codehooks-apikey-security:\n    description: An API key security scheme must be defined.\n    severity: error\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            type:\n              enum: [\"apiKey\", \"http\"]\n\n  codehooks-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  codehooks-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems:\
  \ 1\n\n  codehooks-collection-path:\n    description: Collection-level paths should be declared as /{collection} or sub-paths thereof.\n    severity: info\n    given: \"$.paths\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          patternProperties:\n            \"^/(\\\\{collection\\\\}|keyv|queue)\": {}\n\n  codehooks-error-responses:\n    description: Mutating operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n\n  codehooks-query-parameter:\n    description: List endpoints should accept the q query parameter for MongoDB-style filters.\n    severity: info\n    given: \"$.paths['/{collection}'].get.parameters[*]\"\
  \n    then:\n      field: name\n      function: truthy\n\n  codehooks-pagination-hints:\n    description: List endpoints should accept the h hints query parameter (sort, fields, offset, limit).\n    severity: info\n    given: \"$.paths['/{collection}'].get.parameters[*].name\"\n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - collection\n          - q\n          - h\n          - offset\n          - limit\n          - sort\n          - fields\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/codehooks/refs/heads/main/rules/codehooks-rules.yml
tags:
- Backend
- Database
- Events
- Hooks
- JavaScript
- NoSQL
- Queues
- Serverless
- Webhooks
- Workers
- Workflows
- Spectral
- Linting
- API Governance
---
