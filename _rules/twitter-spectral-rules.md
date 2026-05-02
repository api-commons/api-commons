---
api_specs:
- filename: x-api-openapi.json
  format: json
  label: X API
  slug: x-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/twitter/refs/heads/main/openapi/x-api-openapi.json
categories:
- delete
- deprecated
- external
- get
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
- tags
description: Spectral linting rules defining API design standards and conventions for X (Twitter).
layout: rules
name: X (Twitter) API Rules
provider_name: X (Twitter)
provider_slug: twitter
rule_count: 53
rules:
- description: API title must be present and non-empty.
  given: $.info
  name: info-title-required
  severity: error
- description: API title should follow the pattern "X API" or "X [Name] API".
  given: $.info.title
  name: info-title-format
  severity: warn
- description: API description must be present and meaningful.
  given: $.info
  name: info-description-required
  severity: error
- description: API description should be at least 50 characters.
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: API version must be specified.
  given: $.info
  name: info-version-required
  severity: error
- description: Contact information should be provided.
  given: $.info
  name: info-contact-required
  severity: warn
- description: License information should be provided.
  given: $.info
  name: info-license-required
  severity: info
- description: OpenAPI version must be 3.0.x.
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Server entries should have descriptions.
  given: $.servers[*]
  name: servers-description
  severity: info
- description: Server URLs should use api.x.com or ads-api.x.com domains.
  given: $.servers[*].url
  name: servers-x-domain
  severity: info
- description: Paths should start with a version prefix (e.g., /2/).
  given: $.paths
  name: paths-version-prefix
  severity: warn
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Paths must not contain query strings.
  given: $.paths
  name: paths-no-query-strings
  severity: error
- description: Path segments should use snake_case (the dominant X API convention).
  given: $.paths
  name: paths-snake-case
  severity: info
- description: Path parameters should use snake_case.
  given: $.paths
  name: paths-path-params-snake-case
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Operation IDs must be unique across the API.
  given: $
  name: operation-operationid-unique
  severity: error
- description: Operation IDs should use camelCase with verb prefixes (e.g., getTweets, createPost, deleteUser).
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Global tags array should be defined.
  given: $
  name: tags-defined
  severity: warn
- description: Tag names should use Title Case (e.g., "Direct Messages", "Community Notes").
  given: $.tags[*].name
  name: tags-title-case
  severity: info
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Parameter names should use snake_case (the dominant X API convention).
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-snake-case
  severity: warn
- description: Parameters must have a schema with a type defined.
  given: $.paths[*][get,post,put,patch,delete].parameters[*].schema
  name: parameter-schema-type
  severity: error
- description: Pagination limit parameters should be named max_results.
  given: $.paths[*].get.parameters[?(@.in=='query')]
  name: parameter-pagination-max-results
  severity: info
- description: Pagination cursor parameters should use next_token or pagination_token.
  given: $.paths[*].get.parameters[?(@.in=='query')]
  name: parameter-pagination-token
  severity: info
- description: Expansion parameters should be named expansions for including related objects.
  given: $.paths[*].get.parameters[?(@.in=='query')]
  name: parameter-expansions
  severity: info
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must define a success response (2xx).
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations should define a default error response for unexpected errors.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-default-error
  severity: info
- description: Success responses should use application/json content type.
  given: $.paths[*][get,post,put,patch].responses.200.content
  name: response-success-json
  severity: warn
- description: Schema names should use PascalCase.
  given: $.components.schemas
  name: schema-names-pascalcase
  severity: warn
- description: Schemas should have a type defined.
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Schema properties should use snake_case (the dominant X API convention).
  given: $.components.schemas[*].properties
  name: schema-properties-snake-case
  severity: info
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-top-level
  severity: info
- description: Security schemes should be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: A BearerToken security scheme should be defined for app-only auth.
  given: $.components.securitySchemes
  name: security-bearer-token
  severity: info
- description: An OAuth2UserToken security scheme should be defined for user context auth.
  given: $.components.securitySchemes
  name: security-oauth2-user
  severity: info
- description: Every operation should define its security requirements.
  given: $.paths[*][get,post,put,patch,delete]
  name: security-operation-defined
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: POST operations should have a request body.
  given: $.paths[*].post
  name: post-request-body
  severity: info
- description: Success responses should use a data wrapper object for consistency.
  given: $.paths[*][get,post].responses.200.content.application/json.schema.properties
  name: response-data-wrapper
  severity: info
- description: Error responses should include an errors array.
  given: $.components.schemas[?(@.properties.errors)]
  name: response-errors-array
  severity: info
- description: Field selection parameters should use dot notation (e.g., tweet.fields, user.fields, media.fields).
  given: $.paths[*].get.parameters[?(@.name)]
  name: parameter-fields-dot-notation
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: External documentation link should be provided.
  given: $
  name: external-docs-encouraged
  severity: info
- description: Deprecated operations should explain the deprecation in their description.
  given: $.paths[*][get,post,put,patch,delete][?(@.deprecated==true)]
  name: deprecated-description
  severity: warn
rules_file: rules/twitter-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/twitter/refs/heads/main/rules/twitter-spectral-rules.yml
severity_counts:
  error: 17
  hint: 0
  info: 18
  warn: 18
slug: twitter-spectral-rules
source_filename: twitter-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # ============================================================\n  # INFO / METADATA\n  # ============================================================\n\n  info-title-required:\n    description: API title must be present and non-empty.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-title-format:\n    description: API title should follow the pattern \"X API\" or \"X [Name] API\".\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^X \"\n\n  info-description-required:\n    description: API description must be present and meaningful.\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-description-min-length:\n    description: API description should be at least 50 characters.\n    severity: warn\n    given: $.info.description\n    then:\n      function: length\n      functionOptions:\n\
  \        min: 50\n\n  info-version-required:\n    description: API version must be specified.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Contact information should be provided.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  info-license-required:\n    description: License information should be provided.\n    severity: info\n    given: $.info\n    then:\n      field: license\n      function: truthy\n\n  # ============================================================\n  # OPENAPI VERSION\n  # ============================================================\n\n  openapi-version-3:\n    description: OpenAPI version must be 3.0.x.\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # ============================================================\n\
  \  # SERVERS\n  # ============================================================\n\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  servers-description:\n    description: Server entries should have descriptions.\n    severity: info\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  servers-x-domain:\n    description: Server URLs should use api.x.com or ads-api.x.com domains.\n    severity: info\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(api\\\\.x\\\\.com|ads-api\\\\.x\\\\.com)\"\n\n  # ============================================================\n  # PATHS\
  \ — NAMING CONVENTIONS\n  # ============================================================\n\n  paths-version-prefix:\n    description: Paths should start with a version prefix (e.g., /2/).\n    severity: warn\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^\\\\/[0-9]\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes.\n    severity: error\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n\n  paths-no-query-strings:\n    description: Paths must not contain query strings.\n    severity: error\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\?\"\n\n  paths-snake-case:\n    description: Path segments should use snake_case (the dominant X API convention).\n    severity: info\n    given: $.paths\n    then:\n      field: \"@key\"\
  \n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/[a-z]+[A-Z]\"\n\n  paths-path-params-snake-case:\n    description: Path parameters should use snake_case.\n    severity: warn\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\{[a-z]+[A-Z]\"\n\n  # ============================================================\n  # OPERATIONS\n  # ============================================================\n\n  operation-summary-required:\n    description: Every operation must have a summary.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: Every operation must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-operationid-required:\n    description: Every operation\
  \ must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-unique:\n    description: Operation IDs must be unique across the API.\n    severity: error\n    given: $\n    then:\n      function: oasOpId\n\n  operation-operationid-camelcase:\n    description: Operation IDs should use camelCase with verb prefixes (e.g., getTweets, createPost, deleteUser).\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  # ============================================================\n  # TAGS\n  # ============================================================\n\
  \n  tags-defined:\n    description: Global tags array should be defined.\n    severity: warn\n    given: $\n    then:\n      field: tags\n      function: truthy\n\n  tags-title-case:\n    description: Tag names should use Title Case (e.g., \"Direct Messages\", \"Community Notes\").\n    severity: info\n    given: $.tags[*].name\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*(\\\\s[A-Za-z0-9]+)*$\"\n\n  # ============================================================\n  # PARAMETERS\n  # ============================================================\n\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-snake-case:\n    description: Parameter names should use snake_case (the dominant X API convention).\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n\
  \    then:\n      field: name\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9_]*(\\\\.[a-z][a-z0-9_]*)*$\"\n\n  parameter-schema-type:\n    description: Parameters must have a schema with a type defined.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*].schema\n    then:\n      field: type\n      function: truthy\n\n  parameter-pagination-max-results:\n    description: Pagination limit parameters should be named max_results.\n    severity: info\n    given: $.paths[*].get.parameters[?(@.in=='query')]\n    then:\n      field: name\n      function: pattern\n      functionOptions:\n        notMatch: \"^(page_size|per_page|limit|count|size)$\"\n\n  parameter-pagination-token:\n    description: Pagination cursor parameters should use next_token or pagination_token.\n    severity: info\n    given: $.paths[*].get.parameters[?(@.in=='query')]\n    then:\n      field: name\n      function: pattern\n      functionOptions:\n     \
  \   notMatch: \"^(cursor|page_token|continuation_token|offset)$\"\n\n  parameter-expansions:\n    description: Expansion parameters should be named expansions for including related objects.\n    severity: info\n    given: $.paths[*].get.parameters[?(@.in=='query')]\n    then:\n      field: name\n      function: pattern\n      functionOptions:\n        notMatch: \"^(expand|include|embed)$\"\n\n  # ============================================================\n  # REQUEST BODIES\n  # ============================================================\n\n  request-body-json-content:\n    description: Request bodies should use application/json content type.\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      field: application/json\n      function: truthy\n\n  # ============================================================\n  # RESPONSES\n  # ============================================================\n\n  response-success-required:\n    description: Every\
  \ operation must define a success response (2xx).\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: All responses must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-default-error:\n    description: Operations should define a default error response for unexpected errors.\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      field: default\n      function: truthy\n\n  response-success-json:\n    description: Success responses should use application/json content type.\n    severity: warn\n    given: $.paths[*][get,post,put,patch].responses.200.content\n\
  \    then:\n      field: application/json\n      function: truthy\n\n  # ============================================================\n  # SCHEMAS — PROPERTY NAMING\n  # ============================================================\n\n  schema-names-pascalcase:\n    description: Schema names should use PascalCase.\n    severity: warn\n    given: $.components.schemas\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*$\"\n\n  schema-type-required:\n    description: Schemas should have a type defined.\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  schema-properties-snake-case:\n    description: Schema properties should use snake_case (the dominant X API convention).\n    severity: info\n    given: $.components.schemas[*].properties\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9]*(_[a-z0-9]+)*$\"\
  \n\n  schema-description-top-level:\n    description: Top-level schemas should have a description.\n    severity: info\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  # ============================================================\n  # SECURITY\n  # ============================================================\n\n  security-schemes-defined:\n    description: Security schemes should be defined in components.\n    severity: warn\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-bearer-token:\n    description: A BearerToken security scheme should be defined for app-only auth.\n    severity: info\n    given: $.components.securitySchemes\n    then:\n      field: BearerToken\n      function: truthy\n\n  security-oauth2-user:\n    description: An OAuth2UserToken security scheme should be defined for user context auth.\n    severity: info\n    given: $.components.securitySchemes\n    then:\n\
  \      field: OAuth2UserToken\n      function: truthy\n\n  security-operation-defined:\n    description: Every operation should define its security requirements.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: security\n      function: truthy\n\n  # ============================================================\n  # HTTP METHOD CONVENTIONS\n  # ============================================================\n\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body.\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  post-request-body:\n    description: POST operations should have a request body.\n    severity: info\n    given: $.paths[*].post\n    then:\n\
  \      field: requestBody\n      function: truthy\n\n  # ============================================================\n  # X API SPECIFIC PATTERNS\n  # ============================================================\n\n  response-data-wrapper:\n    description: Success responses should use a data wrapper object for consistency.\n    severity: info\n    given: $.paths[*][get,post].responses.200.content.application/json.schema.properties\n    then:\n      field: data\n      function: truthy\n\n  response-errors-array:\n    description: Error responses should include an errors array.\n    severity: info\n    given: $.components.schemas[?(@.properties.errors)]\n    then:\n      field: properties.errors\n      function: truthy\n\n  parameter-fields-dot-notation:\n    description: Field selection parameters should use dot notation (e.g., tweet.fields, user.fields, media.fields).\n    severity: info\n    given: $.paths[*].get.parameters[?(@.name)]\n    then:\n      field: name\n      function: pattern\n\
  \      functionOptions:\n        notMatch: \"^(fields|select_fields|include_fields)$\"\n\n  # ============================================================\n  # GENERAL QUALITY\n  # ============================================================\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: error\n    given: \"$..description\"\n    then:\n      function: truthy\n\n  external-docs-encouraged:\n    description: External documentation link should be provided.\n    severity: info\n    given: $\n    then:\n      field: externalDocs\n      function: truthy\n\n  deprecated-description:\n    description: Deprecated operations should explain the deprecation in their description.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete][?(@.deprecated==true)]\n    then:\n      field: description\n      function: pattern\n      functionOptions:\n        match: \"[Dd]eprecated|[Ss]unset|[Rr]etired|[Rr]eplaced|[Mm]igrat\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/twitter/refs/heads/main/rules/twitter-spectral-rules.yml
tags:
- Social Media
- Microblogging
- Real-Time Data
- Streaming
- Advertising
- Content
- Spectral
- Linting
- API Governance
---
