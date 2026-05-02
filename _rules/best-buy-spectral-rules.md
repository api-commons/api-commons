---
api_specs:
- filename: best-buy-products-api.yaml
  format: yaml
  label: Best Buy Products API
  slug: products-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/best-buy/refs/heads/main/openapi/best-buy-products-api.yaml
- filename: best-buy-stores-api.yaml
  format: yaml
  label: Best Buy Stores API
  slug: stores-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/best-buy/refs/heads/main/openapi/best-buy-stores-api.yaml
- filename: best-buy-recommendations-api.yaml
  format: yaml
  label: Best Buy Recommendations API
  slug: recommendations-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/best-buy/refs/heads/main/openapi/best-buy-recommendations-api.yaml
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
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Best Buy.
layout: rules
name: Best Buy API Rules
provider_name: Best Buy
provider_slug: best-buy
rule_count: 32
rules:
- description: API info must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: API title should begin with "Best Buy".
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
- description: Server URLs should use the api.bestbuy.com domain.
  given: $.servers[*].url
  name: servers-bestbuy-domain
  severity: warn
- description: Path segments should use kebab-case (lowercase with hyphens).
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
- description: Operation summaries should start with "Best Buy" and use Title Case.
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-title-case
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
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Best Buy API uses apiKey as a query parameter for authentication.
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.name == 'apiKey')]
  name: parameter-api-key-query
  severity: info
- description: Parameter names should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].parameters[*].name
  name: parameter-naming-camel-case
  severity: info
- description: Operations must define at least one 2xx success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations requiring authentication should define a 401 response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-unauthorized
  severity: warn
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Success responses should return application/json content.
  given: $.paths[*][get,post,put,patch,delete].responses['200','201'].content
  name: response-json-content
  severity: warn
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema property names should use camelCase.
  given: $.components.schemas[*].properties[*]~
  name: schema-properties-camel-case
  severity: info
- description: Schema definitions should have an explicit type.
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Security schemes must be defined in components.
  given: $.components.securitySchemes
  name: security-scheme-defined
  severity: error
- description: Security schemes should have a description.
  given: $.components.securitySchemes[*]
  name: security-scheme-description
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Operations should include examples for better developer experience.
  given: $.paths[*][get,post,put,patch,delete].responses[*].content[*]
  name: operation-examples-encouraged
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/best-buy-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/best-buy/refs/heads/main/rules/best-buy-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 4
  warn: 13
slug: best-buy-spectral-rules
source_filename: best-buy-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: API info must have a title.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-title-prefix:\n    description: API title should begin with \"Best Buy\".\n    severity: warn\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Best Buy\"\n\n  info-description-required:\n    description: API info must have a description.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: API info must have a version.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: All specs must use OpenAPI 3.0.x.\n    severity: error\n    given: \"$\"\n    then:\n      field: openapi\n      function: pattern\n    \
  \  functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-bestbuy-domain:\n    description: Server URLs should use the api.bestbuy.com domain.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"bestbuy\\\\.com\"\n\n  # PATHS - NAMING CONVENTIONS\n  paths-kebab-case:\n    description: Path segments should use kebab-case (lowercase with hyphens).\n    severity: warn\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9{}-]+)+$\"\n\n  paths-no-trailing-slash:\n\
  \    description: Paths must not have a trailing slash.\n    severity: error\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: All operations must have a summary.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-title-case:\n    description: Operation summaries should start with \"Best Buy\" and use Title Case.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].summary\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Best Buy [A-Z]\"\n\n  operation-description-required:\n    description: All operations must have a description.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n\
  \    description: All operations must have an operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: operationId should use camelCase.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n\n  operation-tags-required:\n    description: All operations must have at least one tag.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete,options,head]\"\n    then:\n      field: tags\n      function: truthy\n\n  # PARAMETERS\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  parameter-api-key-query:\n\
  \    description: Best Buy API uses apiKey as a query parameter for authentication.\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[?(@.name == 'apiKey')]\"\n    then:\n      field: in\n      function: enumeration\n      functionOptions:\n        values:\n          - query\n\n  parameter-naming-camel-case:\n    description: Parameter names should use camelCase.\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].parameters[*].name\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  # RESPONSES\n  response-success-required:\n    description: Operations must define at least one 2xx success response.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          oneOf:\n            - required: ['200']\n            - required: ['201']\n            - required: ['204']\n\n  response-401-unauthorized:\n\
  \    description: Operations requiring authentication should define a 401 response.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          required: ['401']\n\n  response-description-required:\n    description: All responses must have a description.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  response-json-content:\n    description: Success responses should return application/json content.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses['200','201'].content\"\n    then:\n      function: truthy\n\n  # SCHEMAS - PROPERTY NAMING\n  schema-description-required:\n    description: Top-level schemas should have a description.\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function:\
  \ truthy\n\n  schema-properties-camel-case:\n    description: Schema property names should use camelCase.\n    severity: info\n    given: \"$.components.schemas[*].properties[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  schema-type-required:\n    description: Schema definitions should have an explicit type.\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-scheme-defined:\n    description: Security schemes must be defined in components.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  security-scheme-description:\n    description: Security schemes should have a description.\n    severity: warn\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      field: description\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET\
  \ operations must not have a request body.\n    severity: error\n    given: \"$.paths[*].get\"\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body.\n    severity: warn\n    given: \"$.paths[*].delete\"\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  operation-examples-encouraged:\n    description: Operations should include examples for better developer experience.\n    severity: info\n    given: \"$.paths[*][get,post,put,patch,delete].responses[*].content[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: ['example']\n            - required: ['examples']\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: warn\n    given: \"$..description\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".+\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/best-buy/refs/heads/main/rules/best-buy-spectral-rules.yml
tags:
- Retail
- Consumer Electronics
- E-Commerce
- Products
- Stores
- Spectral
- Linting
- API Governance
---
