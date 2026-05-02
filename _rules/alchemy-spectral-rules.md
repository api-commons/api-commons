---
api_specs:
- filename: alchemy-gas-manager-api-openapi.yml
  format: yaml
  label: Alchemy Gas Manager API
  slug: alchemy-gas-manager-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/alchemy/refs/heads/main/openapi/alchemy-gas-manager-api-openapi.yml
- filename: alchemy-token-api-openapi.yml
  format: yaml
  label: Alchemy Token API
  slug: alchemy-token-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/alchemy/refs/heads/main/openapi/alchemy-token-api-openapi.yml
- filename: alchemy-transfers-api-openapi.yml
  format: yaml
  label: Alchemy Transfers API
  slug: alchemy-transfers-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/alchemy/refs/heads/main/openapi/alchemy-transfers-api-openapi.yml
categories:
- examples
- http
- info
- 'no'
- openapi
- operation
- parameter
- paths
- request
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Alchemy.
layout: rules
name: Alchemy API Rules
provider_name: Alchemy
provider_slug: alchemy
rule_count: 32
rules:
- description: API title must start with "Alchemy" to follow provider naming convention.
  given: $.info.title
  name: info-title-pattern
  severity: warn
- description: API info must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: API info must declare a version.
  given: $.info
  name: info-version-required
  severity: error
- description: API info should include contact information.
  given: $.info
  name: info-contact-required
  severity: warn
- description: Specs must use OpenAPI 3.0.x.
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Each server must have a description.
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Paths must not end with a trailing slash.
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Paths must not contain query strings.
  given: $.paths[*]~
  name: paths-no-query-strings
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Alchemy" and use Title Case.
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-title-case
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-id-required
  severity: error
- description: operationId must use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-tags-required
  severity: warn
- description: Global tags array must be defined.
  given: $
  name: tags-global-defined
  severity: warn
- description: Each global tag should have a description.
  given: $.tags[*]
  name: tags-description-required
  severity: warn
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json
  severity: info
- description: Request bodies should have a description.
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: info
- description: Every operation must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations with security should define a 401 response.
  given: $.paths[*][get,post,put,patch,delete][?(@.security)]
  name: response-401-for-secured
  severity: warn
- description: Top-level component schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-on-top-level
  severity: warn
- description: Schemas should define a type.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: info
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Security schemes should have a description.
  given: $.components.securitySchemes[*]
  name: security-scheme-description
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: http-get-no-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: http-delete-no-body
  severity: warn
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should include request/response examples.
  given: $.paths[*][post,get].responses[*].content[*]
  name: examples-encouraged
  severity: info
rules_file: rules/alchemy-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/alchemy/refs/heads/main/rules/alchemy-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 4
  warn: 15
slug: alchemy-spectral-rules
source_filename: alchemy-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # INFO / METADATA\n  info-title-pattern:\n    description: API title must start with \"Alchemy\" to follow provider naming convention.\n    message: \"Info title must start with 'Alchemy'. Found: {{value}}\"\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Alchemy \"\n\n  info-description-required:\n    description: API info must have a description.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API info must declare a version.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: API info should include contact information.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Specs must\
  \ use OpenAPI 3.0.x.\n    message: \"OpenAPI version must be 3.0.x. Found: {{value}}\"\n    severity: error\n    given: \"$.openapi\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: All server URLs must use HTTPS.\n    message: \"Server URL must use HTTPS. Found: {{value}}\"\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description-required:\n    description: Each server must have a description.\n    severity: warn\n    given: \"$.servers[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # PATHS — NAMING CONVENTIONS\n  paths-no-trailing-slash:\n    description: Paths must not end with a\
  \ trailing slash.\n    message: \"Path must not end with a trailing slash. Found: {{path}}\"\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  paths-no-query-strings:\n    description: Paths must not contain query strings.\n    severity: error\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\?\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-title-case:\n    description: Operation summaries must start with \"Alchemy\" and use Title Case.\n    message: \"Summary should start with 'Alchemy'. Found: {{value}}\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function:\
  \ pattern\n      functionOptions:\n        match: \"^Alchemy \"\n\n  operation-description-required:\n    description: Every operation must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId must use camelCase.\n    message: \"operationId must be camelCase. Found: {{value}}\"\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given:\
  \ \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: tags\n      function: truthy\n\n  # TAGS\n  tags-global-defined:\n    description: Global tags array must be defined.\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n\n  tags-description-required:\n    description: Each global tag should have a description.\n    severity: warn\n    given: \"$.tags[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # REQUEST BODIES\n  request-body-json:\n    description: Request bodies should use application/json content type.\n    severity: info\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      function: truthy\n\n  request-body-description:\n\
  \    description: Request bodies should have a description.\n    severity: info\n    given: \"$.paths[*][post,put,patch].requestBody\"\n    then:\n      field: description\n      function: defined\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must define at least one 2xx response.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-description-required:\n    description: Every response must have a description.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-401-for-secured:\n    description: Operations with security should define a 401 response.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete][?(@.security)]\"\n    then:\n      field: responses\n\
  \      function: defined\n\n  # SCHEMAS — PROPERTY NAMING\n  schema-description-on-top-level:\n    description: Top-level component schemas should have a description.\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  schema-type-defined:\n    description: Schemas should define a type.\n    severity: info\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: defined\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined in components.\n    severity: error\n    given: \"$.components\"\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-scheme-description:\n    description: Security schemes should have a description.\n    severity: warn\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  http-get-no-body:\n    description: GET\
  \ operations must not have a request body.\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  http-delete-no-body:\n    description: DELETE operations should not have a request body.\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    message: \"Description must not be an empty string.\"\n    severity: error\n    given: \"$..description\"\n    then:\n      function: truthy\n\n  examples-encouraged:\n    description: Operations should include request/response examples.\n    severity: info\n    given: \"$.paths[*][post,get].responses[*].content[*]\"\n    then:\n      field: examples\n      function: defined\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/alchemy/refs/heads/main/rules/alchemy-spectral-rules.yml
tags:
- Blockchain
- Cryptocurrency
- Web3
- Account Abstraction
- Ethereum
- Spectral
- Linting
- API Governance
---
