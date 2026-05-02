---
api_specs:
- filename: google-analytics-data-api.yaml
  format: yaml
  label: Google Analytics Data API (GA4)
  slug: google-analytics-data-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/google-analytics/refs/heads/main/openapi/google-analytics-data-api.yaml
- filename: google-analytics-admin-api.yaml
  format: yaml
  label: Google Analytics Admin API
  slug: google-analytics-admin-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/google-analytics/refs/heads/main/openapi/google-analytics-admin-api.yaml
- filename: google-analytics-measurement-protocol.yaml
  format: yaml
  label: Google Analytics Measurement Protocol (GA4)
  slug: google-analytics-measurement-protocol
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/google-analytics/refs/heads/main/openapi/google-analytics-measurement-protocol.yaml
- filename: google-analytics-user-deletion-api.yaml
  format: yaml
  label: Google Analytics User Deletion API
  slug: google-analytics-user-deletion-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/google-analytics/refs/heads/main/openapi/google-analytics-user-deletion-api.yaml
- filename: google-analytics-reporting-api-v4.yaml
  format: yaml
  label: Google Analytics Reporting API v4 (Universal Analytics)
  slug: google-analytics-reporting-api-v4
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/google-analytics/refs/heads/main/openapi/google-analytics-reporting-api-v4.yaml
- filename: google-analytics-management-api-v3.yaml
  format: yaml
  label: Google Analytics Management API v3
  slug: google-analytics-management-api-v3
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/google-analytics/refs/heads/main/openapi/google-analytics-management-api-v3.yaml
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
- patch
- paths
- post
- put
- request
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Google Analytics.
layout: rules
name: Google Analytics API Rules
provider_name: Google Analytics
provider_slug: google-analytics
rule_count: 66
rules:
- description: API title must be present and non-empty.
  given: $.info
  name: info-title-required
  severity: error
- description: API title should follow the pattern "Google Analytics [Name]".
  given: $.info.title
  name: info-title-format
  severity: warn
- description: API description must be present and meaningful.
  given: $.info
  name: info-description-required
  severity: error
- description: API description should be at least 50 characters to be meaningful.
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
- description: Contact name should be provided.
  given: $.info.contact
  name: info-contact-name
  severity: info
- description: Contact URL should be provided.
  given: $.info.contact
  name: info-contact-url
  severity: info
- description: License information should be provided.
  given: $.info
  name: info-license-required
  severity: warn
- description: Terms of service URL should be provided.
  given: $.info
  name: info-terms-of-service
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
- description: Server URLs should use googleapis.com or google-analytics.com domains.
  given: $.servers[*].url
  name: servers-google-domain
  severity: info
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Paths must not contain query strings.
  given: $.paths
  name: paths-no-query-strings
  severity: error
- description: Paths should include a version prefix (e.g., /v1beta/, /v1/, /v3/).
  given: $.paths
  name: paths-version-prefix
  severity: info
- description: Path segments (excluding parameters and custom actions) should use lowercase.
  given: $.paths
  name: paths-no-uppercase-in-segments
  severity: info
- description: Path parameters should use camelCase.
  given: $.paths
  name: paths-path-params-camelcase
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Operation descriptions should be at least 20 characters.
  given: $.paths[*][get,post,put,patch,delete].description
  name: operation-description-min-length
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Operation IDs must be unique across the API.
  given: $
  name: operation-operationid-unique
  severity: error
- description: Operation IDs should use dot-notation (service.resource.action) or camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-format
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Operations should have exactly one tag for clean grouping.
  given: $.paths[*][get,post,put,patch,delete].tags
  name: operation-tags-single
  severity: info
- description: Global tags array should be defined.
  given: $
  name: tags-defined
  severity: warn
- description: Tag names should use Title Case (e.g., "Account Summaries", "Data Streams").
  given: $.tags[*].name
  name: tags-title-case
  severity: info
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Query parameters should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in=='query')]
  name: parameter-query-camelcase
  severity: warn
- description: Path parameters should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in=='path')]
  name: parameter-path-camelcase
  severity: warn
- description: Parameters must have a schema with a type defined.
  given: $.paths[*][get,post,put,patch,delete].parameters[*].schema
  name: parameter-schema-type-required
  severity: error
- description: Pagination limit parameters should be named pageSize.
  given: $.paths[*].get.parameters[?(@.in=='query')]
  name: parameter-pagination-page-size
  severity: info
- description: Pagination cursor parameters should be named pageToken.
  given: $.paths[*].get.parameters[?(@.in=='query')]
  name: parameter-pagination-page-token
  severity: info
- description: API keys should be passed in headers, not query parameters.
  given: $.components.securitySchemes[?(@.type=='apiKey')]
  name: parameter-no-api-key-in-query
  severity: info
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Request bodies should have a description.
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: info
- description: Every operation must define a success response (2xx).
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Success responses with bodies should use application/json content type.
  given: $.paths[*][get,post,put,patch].responses.200.content
  name: response-success-json-content
  severity: warn
- description: Success responses with JSON content should have a schema defined.
  given: $.paths[*][get,post,put,patch].responses.200.content.application/json
  name: response-success-schema
  severity: warn
- description: Operations with security should define a 401 Unauthorized response.
  given: $.paths[*][get,post,put,patch,delete][?(@.security)]
  name: response-401-defined
  severity: info
- description: Operations with security should define a 403 Forbidden response.
  given: $.paths[*][get,post,put,patch,delete][?(@.security)]
  name: response-403-defined
  severity: info
- description: POST operations should define a 400 Bad Request response.
  given: $.paths[*].post.responses
  name: response-400-for-post
  severity: info
- description: Schema names should use PascalCase.
  given: $.components.schemas
  name: schema-names-pascalcase
  severity: warn
- description: Schemas should have a type defined.
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Schema properties should use snake_case or camelCase consistently.
  given: $.components.schemas[*].properties
  name: schema-properties-snake-case
  severity: info
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-top-level
  severity: info
- description: Enum values should use UPPER_CASE_WITH_UNDERSCORES.
  given: $.components.schemas[*].properties[*].enum[*]
  name: schema-enum-uppercase
  severity: info
- description: Global security should be defined or operations should have individual security.
  given: $
  name: security-global-defined
  severity: warn
- description: Security schemes should be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: Security schemes should have descriptions.
  given: $.components.securitySchemes[*]
  name: security-scheme-description
  severity: info
- description: OAuth2 security schemes should have properly defined flows.
  given: $.components.securitySchemes[?(@.type=='oauth2')]
  name: security-oauth2-flows
  severity: error
- description: OAuth2 flows should define scopes.
  given: $.components.securitySchemes[?(@.type=='oauth2')].flows[*]
  name: security-oauth2-scopes
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
- description: PUT operations should have a request body.
  given: $.paths[*].put
  name: put-request-body
  severity: info
- description: PATCH operations should have a request body.
  given: $.paths[*].patch
  name: patch-request-body
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: External documentation link should be provided.
  given: $
  name: external-docs-encouraged
  severity: info
- description: External documentation should have a URL.
  given: $.externalDocs
  name: external-docs-url
  severity: warn
- description: Deprecated operations should explain the deprecation in their description.
  given: $.paths[*][get,post,put,patch,delete][?(@.deprecated==true)]
  name: deprecated-description
  severity: warn
- description: Deprecated schema properties should explain the deprecation.
  given: $.components.schemas[*].properties[?(@.deprecated==true)]
  name: schema-deprecated-description
  severity: info
- description: Success responses should include examples.
  given: $.paths[*][get,post,put,patch].responses.200.content.application/json
  name: response-examples-encouraged
  severity: info
rules_file: rules/google-analytics-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/google-analytics/refs/heads/main/rules/google-analytics-spectral-rules.yml
severity_counts:
  error: 18
  hint: 0
  info: 26
  warn: 22
slug: google-analytics-spectral-rules
source_filename: google-analytics-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # ============================================================\n  # INFO / METADATA\n  # ============================================================\n\n  info-title-required:\n    description: API title must be present and non-empty.\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-title-format:\n    description: API title should follow the pattern \"Google Analytics [Name]\".\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Google Analytics \"\n\n  info-description-required:\n    description: API description must be present and meaningful.\n    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-description-min-length:\n    description: API description should be at least 50 characters to be meaningful.\n    severity: warn\n    given: $.info.description\n    then:\n      function:\
  \ length\n      functionOptions:\n        min: 50\n\n  info-version-required:\n    description: API version must be specified.\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Contact information should be provided.\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  info-contact-name:\n    description: Contact name should be provided.\n    severity: info\n    given: $.info.contact\n    then:\n      field: name\n      function: truthy\n\n  info-contact-url:\n    description: Contact URL should be provided.\n    severity: info\n    given: $.info.contact\n    then:\n      field: url\n      function: truthy\n\n  info-license-required:\n    description: License information should be provided.\n    severity: warn\n    given: $.info\n    then:\n      field: license\n      function: truthy\n\n  info-terms-of-service:\n    description: Terms of service\
  \ URL should be provided.\n    severity: info\n    given: $.info\n    then:\n      field: termsOfService\n      function: truthy\n\n  # ============================================================\n  # OPENAPI VERSION\n  # ============================================================\n\n  openapi-version-3:\n    description: OpenAPI version must be 3.0.x.\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.0\\\\.\"\n\n  # ============================================================\n  # SERVERS\n  # ============================================================\n\n  servers-defined:\n    description: At least one server must be defined.\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https-only:\n    description: Server URLs must use HTTPS.\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n\
  \        match: \"^https://\"\n\n  servers-description:\n    description: Server entries should have descriptions.\n    severity: info\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  servers-google-domain:\n    description: Server URLs should use googleapis.com or google-analytics.com domains.\n    severity: info\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(googleapis\\\\.com|google-analytics\\\\.com)\"\n\n  # ============================================================\n  # PATHS — NAMING CONVENTIONS\n  # ============================================================\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes.\n    severity: error\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/$\"\n\n  paths-no-query-strings:\n    description: Paths must not contain query strings.\n\
  \    severity: error\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\?\"\n\n  paths-version-prefix:\n    description: Paths should include a version prefix (e.g., /v1beta/, /v1/, /v3/).\n    severity: info\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^\\\\/v[0-9]\"\n\n  paths-no-uppercase-in-segments:\n    description: Path segments (excluding parameters and custom actions) should use lowercase.\n    severity: info\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\/[A-Z][^\\\\/\\\\{:]*(\\\\/|$)\"\n\n  paths-path-params-camelcase:\n    description: Path parameters should use camelCase.\n    severity: warn\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \"\\\\{[a-z]+_[a-z]\"\n\n  # ============================================================\n\
  \  # OPERATIONS\n  # ============================================================\n\n  operation-description-required:\n    description: Every operation must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-description-min-length:\n    description: Operation descriptions should be at least 20 characters.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].description\n    then:\n      function: length\n      functionOptions:\n        min: 20\n\n  operation-operationid-required:\n    description: Every operation must have an operationId.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-unique:\n    description: Operation IDs must be unique across the API.\n    severity: error\n    given: $\n    then:\n      function: oasOpId\n\n  operation-operationid-format:\n\
  \    description: Operation IDs should use dot-notation (service.resource.action) or camelCase.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*(\\\\.[a-z][a-zA-Z0-9]*)*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  operation-tags-single:\n    description: Operations should have exactly one tag for clean grouping.\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].tags\n    then:\n      function: length\n      functionOptions:\n        max: 1\n\n  # ============================================================\n  # TAGS\n  # ============================================================\n\n  tags-defined:\n    description: Global tags array should be defined.\n    severity:\
  \ warn\n    given: $\n    then:\n      field: tags\n      function: truthy\n\n  tags-title-case:\n    description: Tag names should use Title Case (e.g., \"Account Summaries\", \"Data Streams\").\n    severity: info\n    given: $.tags[*].name\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*(\\\\s[A-Za-z0-9]+)*$\"\n\n  # ============================================================\n  # PARAMETERS\n  # ============================================================\n\n  parameter-description-required:\n    description: All parameters must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-query-camelcase:\n    description: Query parameters should use camelCase.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in=='query')]\n    then:\n      field: name\n      function: pattern\n \
  \     functionOptions:\n        match: \"^[a-z][a-zA-Z0-9_$.]*$\"\n\n  parameter-path-camelcase:\n    description: Path parameters should use camelCase.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in=='path')]\n    then:\n      field: name\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  parameter-schema-type-required:\n    description: Parameters must have a schema with a type defined.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*].schema\n    then:\n      field: type\n      function: truthy\n\n  parameter-pagination-page-size:\n    description: Pagination limit parameters should be named pageSize.\n    severity: info\n    given: $.paths[*].get.parameters[?(@.in=='query')]\n    then:\n      field: name\n      function: pattern\n      functionOptions:\n        notMatch: \"^(page_size|per_page|limit|count|size)$\"\n\n  parameter-pagination-page-token:\n    description:\
  \ Pagination cursor parameters should be named pageToken.\n    severity: info\n    given: $.paths[*].get.parameters[?(@.in=='query')]\n    then:\n      field: name\n      function: pattern\n      functionOptions:\n        notMatch: \"^(page_token|cursor|next_token|continuation_token)$\"\n\n  parameter-no-api-key-in-query:\n    description: API keys should be passed in headers, not query parameters.\n    severity: info\n    given: $.components.securitySchemes[?(@.type=='apiKey')]\n    then:\n      field: in\n      function: pattern\n      functionOptions:\n        match: \"header\"\n\n  # ============================================================\n  # REQUEST BODIES\n  # ============================================================\n\n  request-body-json-content:\n    description: Request bodies should use application/json content type.\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      field: application/json\n      function: truthy\n\n  request-body-description:\n\
  \    description: Request bodies should have a description.\n    severity: info\n    given: $.paths[*][post,put,patch].requestBody\n    then:\n      field: description\n      function: truthy\n\n  # ============================================================\n  # RESPONSES\n  # ============================================================\n\n  response-success-required:\n    description: Every operation must define a success response (2xx).\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"202\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: All responses must have a description.\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n\
  \  response-success-json-content:\n    description: Success responses with bodies should use application/json content type.\n    severity: warn\n    given: $.paths[*][get,post,put,patch].responses.200.content\n    then:\n      field: application/json\n      function: truthy\n\n  response-success-schema:\n    description: Success responses with JSON content should have a schema defined.\n    severity: warn\n    given: $.paths[*][get,post,put,patch].responses.200.content.application/json\n    then:\n      field: schema\n      function: truthy\n\n  response-401-defined:\n    description: Operations with security should define a 401 Unauthorized response.\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete][?(@.security)]\n    then:\n      field: responses.401\n      function: truthy\n\n  response-403-defined:\n    description: Operations with security should define a 403 Forbidden response.\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete][?(@.security)]\n\
  \    then:\n      field: responses.403\n      function: truthy\n\n  response-400-for-post:\n    description: POST operations should define a 400 Bad Request response.\n    severity: info\n    given: $.paths[*].post.responses\n    then:\n      field: \"400\"\n      function: truthy\n\n  # ============================================================\n  # SCHEMAS — PROPERTY NAMING\n  # ============================================================\n\n  schema-names-pascalcase:\n    description: Schema names should use PascalCase.\n    severity: warn\n    given: $.components.schemas\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*$\"\n\n  schema-type-required:\n    description: Schemas should have a type defined.\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  schema-properties-snake-case:\n    description: Schema properties should use snake_case or camelCase\
  \ consistently.\n    severity: info\n    given: $.components.schemas[*].properties\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-z0-9]*([A-Z][a-z0-9]*|_[a-z0-9]+)*$\"\n\n  schema-description-top-level:\n    description: Top-level schemas should have a description.\n    severity: info\n    given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-enum-uppercase:\n    description: Enum values should use UPPER_CASE_WITH_UNDERSCORES.\n    severity: info\n    given: $.components.schemas[*].properties[*].enum[*]\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][A-Z0-9_]*$\"\n\n  # ============================================================\n  # SECURITY\n  # ============================================================\n\n  security-global-defined:\n    description: Global security should be defined or operations should have individual security.\n \
  \   severity: warn\n    given: $\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"security\"]\n            - not:\n                required: [\"security\"]\n\n  security-schemes-defined:\n    description: Security schemes should be defined in components.\n    severity: warn\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-scheme-description:\n    description: Security schemes should have descriptions.\n    severity: info\n    given: $.components.securitySchemes[*]\n    then:\n      field: description\n      function: truthy\n\n  security-oauth2-flows:\n    description: OAuth2 security schemes should have properly defined flows.\n    severity: error\n    given: $.components.securitySchemes[?(@.type=='oauth2')]\n    then:\n      field: flows\n      function: truthy\n\n  security-oauth2-scopes:\n    description: OAuth2 flows should define scopes.\n    severity: warn\n\
  \    given: $.components.securitySchemes[?(@.type=='oauth2')].flows[*]\n    then:\n      field: scopes\n      function: truthy\n\n  # ============================================================\n  # HTTP METHOD CONVENTIONS\n  # ============================================================\n\n  get-no-request-body:\n    description: GET operations must not have a request body.\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  delete-no-request-body:\n    description: DELETE operations should not have a request body.\n    severity: warn\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  post-request-body:\n    description: POST operations should have a request body.\n    severity: info\n    given: $.paths[*].post\n    then:\n      field: requestBody\n      function: truthy\n\n  put-request-body:\n    description: PUT operations should have a request body.\n    severity: info\n    given:\
  \ $.paths[*].put\n    then:\n      field: requestBody\n      function: truthy\n\n  patch-request-body:\n    description: PATCH operations should have a request body.\n    severity: info\n    given: $.paths[*].patch\n    then:\n      field: requestBody\n      function: truthy\n\n  # ============================================================\n  # GENERAL QUALITY\n  # ============================================================\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings.\n    severity: error\n    given: \"$..description\"\n    then:\n      function: truthy\n\n  external-docs-encouraged:\n    description: External documentation link should be provided.\n    severity: info\n    given: $\n    then:\n      field: externalDocs\n      function: truthy\n\n  external-docs-url:\n    description: External documentation should have a URL.\n    severity: warn\n    given: $.externalDocs\n    then:\n      field: url\n      function: truthy\n\n  deprecated-description:\n\
  \    description: Deprecated operations should explain the deprecation in their description.\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete][?(@.deprecated==true)]\n    then:\n      field: description\n      function: pattern\n      functionOptions:\n        match: \"[Dd]eprecated|[Ss]unset|[Rr]etired|[Rr]eplaced|[Mm]igrat\"\n\n  schema-deprecated-description:\n    description: Deprecated schema properties should explain the deprecation.\n    severity: info\n    given: $.components.schemas[*].properties[?(@.deprecated==true)]\n    then:\n      field: description\n      function: pattern\n      functionOptions:\n        match: \"[Dd]eprecated|[Rr]eplaced|[Uu]se .* instead\"\n\n  response-examples-encouraged:\n    description: Success responses should include examples.\n    severity: info\n    given: $.paths[*][get,post,put,patch].responses.200.content.application/json\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n  \
  \          - required: [\"example\"]\n            - required: [\"examples\"]\n            - not:\n                required: [\"example\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/google-analytics/refs/heads/main/rules/google-analytics-spectral-rules.yml
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
- Spectral
- Linting
- API Governance
---
