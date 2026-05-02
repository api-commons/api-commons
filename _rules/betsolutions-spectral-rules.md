---
api_specs:
- filename: betsolutions-wallet-api.yaml
  format: yaml
  label: BetSolutions Wallet API
  slug: wallet-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/betsolutions/refs/heads/main/openapi/betsolutions-wallet-api.yaml
categories:
- get
- hash
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
description: Spectral linting rules defining API design standards and conventions for BetSolutions.
layout: rules
name: BetSolutions API Rules
provider_name: BetSolutions
provider_slug: betsolutions
rule_count: 30
rules:
- description: API info must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: API title should begin with "BetSolutions".
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API info must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: API info must have a version.
  given: $.info
  name: info-version-required
  severity: error
- description: All specs must use OpenAPI 3.0.x.
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Server URLs should use a betsolutions.com domain.
  given: $.servers[*].url
  name: servers-betsolutions-domain
  severity: warn
- description: Path segments should use kebab-case.
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have a trailing slash.
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: All operations must have a summary.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "BetSolutions".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: All operations must have a description.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: All operations must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-tags-required
  severity: error
- description: POST operations should have a request body.
  given: $.paths[*].post
  name: post-request-body-required
  severity: warn
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json
  severity: warn
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: BetSolutions API requires SHA-256 hash parameter for authentication.
  given: $.paths[*][post].requestBody.content['application/json'].schema.properties
  name: hash-parameter-required
  severity: info
- description: Operations must define at least one 2xx success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Success responses should return application/json content.
  given: $.paths[*][get,post,put,patch,delete].responses['200'].content
  name: response-json-content
  severity: warn
- description: Operations should define a 401 unauthorized response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-defined
  severity: warn
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema definitions should have an explicit type.
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: BetSolutions response schemas should include a success boolean field.
  given: $.components.schemas[*].properties
  name: schema-success-flag
  severity: info
- description: Security schemes must be defined in components.
  given: $.components.securitySchemes
  name: security-scheme-defined
  severity: error
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/betsolutions-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/betsolutions/refs/heads/main/rules/betsolutions-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 2
  warn: 13
slug: betsolutions-spectral-rules
source_filename: betsolutions-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: API info must have a title.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-title-prefix:\n    description: API title should begin with \"BetSolutions\".\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^BetSolutions\"\n\n  info-description-required:\n    description: API info must have a description.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API info must have a version.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: All specs must use OpenAPI 3.0.x.\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n\
  \      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-betsolutions-domain:\n    description: Server URLs should use a betsolutions.com domain.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"betsolutions\\\\.com\"\n\n  # PATHS - NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case.\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}-]+)+$\"\n\n  paths-no-trailing-slash:\n \
  \   description: Paths must not have a trailing slash.\n    severity: error\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"BetSolutions\".\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^BetSolutions [A-Z]\"\n\n  operation-description-required:\n    description: All operations must have a description.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n \
  \   description: All operations must have an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId should use camelCase.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: All operations must have at least one tag.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: tags\n      function: truthy\n\n  # REQUEST BODIES\n  post-request-body-required:\n    description: POST operations should have a request body.\n    severity: warn\n    given: \"$.paths[*].post\"\n    then:\n      field: requestBody\n      function: truthy\n\n  request-body-json:\n    description: Request bodies should\
  \ use application/json content type.\n    severity: warn\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          required: ['application/json']\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  hash-parameter-required:\n    description: BetSolutions API requires SHA-256 hash parameter for authentication.\n    severity: info\n    given: \"$.paths[*][post].requestBody.content['application/json'].schema.properties\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          required: ['hash']\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must define at least one 2xx success response.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\
  \n    then:\n      function: schema\n      functionOptions:\n        schema:\n          oneOf:\n            - required: ['200']\n            - required: ['201']\n\n  response-description-required:\n    description: All responses must have a description.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-json-content:\n    description: Success responses should return application/json content.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses['200'].content\"\n    then:\n      function: truthy\n\n  response-401-defined:\n    description: Operations should define a 401 unauthorized response.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          required: ['401']\n\n  # SCHEMAS\n  schema-description-required:\n    description: Top-level\
  \ schemas should have a description.\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-type-required:\n    description: Schema definitions should have an explicit type.\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  schema-success-flag:\n    description: BetSolutions response schemas should include a success boolean field.\n    severity: info\n    given: \"$.components.schemas[*].properties\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          oneOf:\n            - required: ['success']\n            - not:\n                required: []\n\n  # SECURITY\n  security-scheme-defined:\n    description: Security schemes must be defined in components.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n\
  \    description: GET operations must not have a request body.\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/betsolutions/refs/heads/main/rules/betsolutions-spectral-rules.yml
tags:
- Betting
- Casinos
- Gaming
- Gambling
- Slots
- Sports Betting
- Spectral
- Linting
- API Governance
---
