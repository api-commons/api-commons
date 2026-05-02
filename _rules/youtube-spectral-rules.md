---
api_specs:
- filename: youtube-data-api-openapi.yml
  format: yaml
  label: Youtube Activities API
  slug: youtube-activities-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/openapi/youtube-data-api-openapi.yml
- filename: youtube-data-api-openapi.yml
  format: yaml
  label: Youtube Channels API
  slug: youtube-channels-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/openapi/youtube-data-api-openapi.yml
- filename: youtube-data-api-openapi.yml
  format: yaml
  label: Youtube Comments API
  slug: youtube-comments-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/openapi/youtube-data-api-openapi.yml
- filename: youtube-data-api-openapi.yml
  format: yaml
  label: Youtube Comment Threads API
  slug: youtube-comment-threads-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/openapi/youtube-data-api-openapi.yml
- filename: youtube-data-api-openapi.yml
  format: yaml
  label: Youtube Playlists API
  slug: youtube-playlists-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/openapi/youtube-data-api-openapi.yml
- filename: youtube-data-api-openapi.yml
  format: yaml
  label: Youtube Playlist Items API
  slug: youtube-playlist-items-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/openapi/youtube-data-api-openapi.yml
- filename: youtube-data-api-openapi.yml
  format: yaml
  label: Youtube Search API
  slug: youtube-search-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/openapi/youtube-data-api-openapi.yml
- filename: youtube-data-api-openapi.yml
  format: yaml
  label: Youtube Subscriptions API
  slug: youtube-subscriptions-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/openapi/youtube-data-api-openapi.yml
- filename: youtube-data-api-openapi.yml
  format: yaml
  label: Youtube Videos API
  slug: youtube-videos-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/openapi/youtube-data-api-openapi.yml
- filename: youtube-data-api-openapi.yml
  format: yaml
  label: Youtube Captions API
  slug: youtube-captions-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/openapi/youtube-data-api-openapi.yml
- filename: youtube-data-api-openapi.yml
  format: yaml
  label: Youtube Video Categories API
  slug: youtube-video-categories-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/openapi/youtube-data-api-openapi.yml
- filename: youtube-data-api-openapi.yml
  format: yaml
  label: Youtube I18n Languages API
  slug: youtube-i18n-languages-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/openapi/youtube-data-api-openapi.yml
- filename: youtube-data-api-openapi.yml
  format: yaml
  label: Youtube I18n Regions API
  slug: youtube-i18n-regions-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/openapi/youtube-data-api-openapi.yml
- filename: youtube-analytics-openapi.yml
  format: yaml
  label: YouTube Analytics API
  slug: youtube-analytics-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/openapi/youtube-analytics-openapi.yml
- filename: youtube-reporting-openapi.yml
  format: yaml
  label: YouTube Reporting API
  slug: youtube-reporting-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/openapi/youtube-reporting-openapi.yml
- filename: youtube-live-streaming-openapi.yml
  format: yaml
  label: YouTube Live Streaming API
  slug: youtube-live-streaming-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/openapi/youtube-live-streaming-openapi.yml
categories:
- deprecated
- http
- info
- list
- microcks
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
description: Spectral linting rules defining API design standards and conventions for Youtube.
layout: rules
name: Youtube API Rules
provider_name: Youtube
provider_slug: youtube
rule_count: 55
rules:
- description: Info title must be present and non-empty
  given: $.info
  name: info-title-required
  severity: error
- description: Info title should start with "YouTube"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: error
- description: Info description should be at least 50 characters
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: API version must be specified
  given: $.info
  name: info-version-required
  severity: error
- description: Contact information should be provided
  given: $.info
  name: info-contact-required
  severity: warn
- description: Terms of service URL should be provided
  given: $.info
  name: info-terms-of-service
  severity: info
- description: OpenAPI version should be 3.0.x or 3.1.x
  given: $
  name: openapi-version
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Server URLs should use googleapis.com domain
  given: $.servers[*].url
  name: servers-googleapis-domain
  severity: info
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Paths must not include query strings
  given: $.paths
  name: paths-no-query-strings
  severity: error
- description: YouTube paths use camelCase for resource names
  given: $.paths
  name: paths-camel-case
  severity: warn
- description: Resource paths should use plural nouns
  given: $.paths
  name: paths-plural-resources
  severity: info
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: OperationId should follow youtube.resource.action or youtubeAnalytics.resource.action format
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-format
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Youtube" prefix
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Operation summaries should use Title Case
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-title-case
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Operations should have exactly one tag
  given: $.paths[*][get,post,put,patch,delete].tags
  name: operation-single-tag
  severity: info
- description: Global tags array should be defined
  given: $
  name: tags-defined
  severity: warn
- description: Each tag should have a description
  given: $.tags[*]
  name: tags-description
  severity: warn
- description: Tag names should use PascalCase (YouTube convention)
  given: $.tags[*].name
  name: tags-pascal-case
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Every parameter must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Parameter names should use camelCase (YouTube convention)
  given: $.paths[*][get,post,put,patch,delete].parameters[*].name
  name: parameter-camel-case
  severity: warn
- description: Parameters should have example values
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-example
  severity: info
- description: Pagination should use pageToken and maxResults (YouTube convention)
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.name=='page' || @.name=='offset' || @.name=='cursor')]
  name: parameter-pagination-naming
  severity: info
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json
  severity: warn
- description: Every operation must have a 2xx success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Success responses should use application/json
  given: $.paths[*][get,post,put,patch].responses[?(@property >= 200 && @property < 300)].content
  name: response-json-content
  severity: warn
- description: Responses should include named examples for Microcks compatibility
  given: $.paths[*][get,post,put,patch,delete].responses[*].content.application/json
  name: response-examples
  severity: info
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description
  severity: warn
- description: Schema properties must define a type
  given: $.components.schemas[*].properties[*]
  name: schema-type-required
  severity: error
- description: Schema property names should use camelCase (YouTube convention)
  given: $.components.schemas[*].properties
  name: schema-property-camel-case
  severity: warn
- description: YouTube resource schemas should include a kind property
  given: $.components.schemas[?(@.properties.etag)].properties
  name: schema-kind-property
  severity: info
- description: YouTube resource schemas should include an etag property
  given: $.components.schemas[?(@.properties.kind)].properties
  name: schema-etag-property
  severity: info
- description: Schema properties should have example values
  given: $.components.schemas[*].properties[*]
  name: schema-property-example
  severity: info
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: error
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: YouTube APIs should use OAuth 2.0 authentication
  given: $.components.securitySchemes
  name: security-oauth2-scheme
  severity: warn
- description: YouTube APIs should support API key authentication for read operations
  given: $.components.securitySchemes
  name: security-api-key-scheme
  severity: info
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: http-get-no-body
  severity: error
- description: DELETE operations must not have a request body
  given: $.paths[*].delete
  name: http-delete-no-body
  severity: error
- description: POST operations should have a request body
  given: $.paths[*].post
  name: http-post-has-body
  severity: warn
- description: PUT operations should have a request body
  given: $.paths[*].put
  name: http-put-has-body
  severity: warn
- description: Operations should have x-microcks-operation for mock server compatibility
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Deprecated operations should have a description explaining the deprecation
  given: $.paths[*][get,post,put,patch,delete][?(@.deprecated==true)]
  name: deprecated-documented
  severity: warn
- description: List responses should contain an items array (YouTube convention)
  given: $.components.schemas[?(@.properties.nextPageToken)].properties
  name: list-response-items-array
  severity: info
rules_file: rules/youtube-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/rules/youtube-spectral-rules.yml
severity_counts:
  error: 22
  hint: 0
  info: 13
  warn: 20
slug: youtube-spectral-rules
source_filename: youtube-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# =============================================================================\n# YouTube API Spectral Ruleset\n# Generated from analysis of YouTube Data API, Analytics API,\n# Live Streaming API, and Reporting API OpenAPI specifications\n# =============================================================================\n\nrules:\n\n  # ---------------------------------------------------------------------------\n  # INFO / METADATA\n  # ---------------------------------------------------------------------------\n\n  info-title-required:\n    description: Info title must be present and non-empty\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-title-prefix:\n    description: Info title should start with \"YouTube\"\n    severity: warn\n    given: $.info.title\n    then:\n      function: pattern\n      functionOptions:\n        match: ^YouTube\n\n  info-description-required:\n    description: Info description must be present\n\
  \    severity: error\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-description-min-length:\n    description: Info description should be at least 50 characters\n    severity: warn\n    given: $.info.description\n    then:\n      function: length\n      functionOptions:\n        min: 50\n\n  info-version-required:\n    description: API version must be specified\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  info-contact-required:\n    description: Contact information should be provided\n    severity: warn\n    given: $.info\n    then:\n      field: contact\n      function: truthy\n\n  info-terms-of-service:\n    description: Terms of service URL should be provided\n    severity: info\n    given: $.info\n    then:\n      field: termsOfService\n      function: truthy\n\n  # ---------------------------------------------------------------------------\n  # OPENAPI VERSION\n  # ---------------------------------------------------------------------------\n\
  \n  openapi-version:\n    description: OpenAPI version should be 3.0.x or 3.1.x\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: ^3\\.[01]\\.\\d+$\n\n  # ---------------------------------------------------------------------------\n  # SERVERS\n  # ---------------------------------------------------------------------------\n\n  servers-defined:\n    description: At least one server must be defined\n    severity: error\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  servers-https:\n    description: Server URLs must use HTTPS\n    severity: error\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: ^https://\n\n  servers-description:\n    description: Each server should have a description\n    severity: warn\n    given: $.servers[*]\n    then:\n      field: description\n      function: truthy\n\n  servers-googleapis-domain:\n \
  \   description: Server URLs should use googleapis.com domain\n    severity: info\n    given: $.servers[*].url\n    then:\n      function: pattern\n      functionOptions:\n        match: googleapis\\.com\n\n  # ---------------------------------------------------------------------------\n  # PATHS — NAMING CONVENTIONS\n  # ---------------------------------------------------------------------------\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: error\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: .+\\/$\n\n  paths-no-query-strings:\n    description: Paths must not include query strings\n    severity: error\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        notMatch: \\?\n\n  paths-camel-case:\n    description: YouTube paths use camelCase for resource names\n    severity: warn\n    given: $.paths\n    then:\n\
  \      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: ^(/[a-z][a-zA-Z0-9]*(\\/{[a-zA-Z]+})?)+$\n\n  paths-plural-resources:\n    description: Resource paths should use plural nouns\n    severity: info\n    given: $.paths\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: ^(/[a-z][a-zA-Z]*s|/[a-z][a-zA-Z]*s/|/[a-z][a-zA-Z]*(Items|Types|Reasons|Languages|Regions|Banners|Sections|Levels|Events))\n\n  # ---------------------------------------------------------------------------\n  # OPERATIONS\n  # ---------------------------------------------------------------------------\n\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-operationid-format:\n    description: OperationId should follow youtube.resource.action or youtubeAnalytics.resource.action\
  \ format\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: ^(youtube|youtubeAnalytics|youtubeReporting)\\.[a-zA-Z]+\\.[a-zA-Z]+$\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: summary\n      function: truthy\n\n  operation-summary-prefix:\n    description: Operation summaries should start with \"Youtube\" prefix\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: ^Youtube\n\n  operation-summary-title-case:\n    description: Operation summaries should use Title Case\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z]+(\\\\s[A-Za-z]+)*$\"\
  \n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: description\n      function: truthy\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: tags\n      function: truthy\n\n  operation-single-tag:\n    description: Operations should have exactly one tag\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].tags\n    then:\n      function: length\n      functionOptions:\n        max: 1\n\n  # ---------------------------------------------------------------------------\n  # TAGS\n  # ---------------------------------------------------------------------------\n\n  tags-defined:\n    description: Global tags array should be defined\n    severity: warn\n    given: $\n    then:\n      field: tags\n      function:\
  \ truthy\n\n  tags-description:\n    description: Each tag should have a description\n    severity: warn\n    given: $.tags[*]\n    then:\n      field: description\n      function: truthy\n\n  tags-pascal-case:\n    description: Tag names should use PascalCase (YouTube convention)\n    severity: warn\n    given: $.tags[*].name\n    then:\n      function: pattern\n      functionOptions:\n        match: ^[A-Z][a-zA-Z0-9]+$\n\n  # ---------------------------------------------------------------------------\n  # PARAMETERS\n  # ---------------------------------------------------------------------------\n\n  parameter-description-required:\n    description: Every parameter must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  parameter-schema-required:\n    description: Every parameter must have a schema\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n\
  \    then:\n      field: schema\n      function: truthy\n\n  parameter-camel-case:\n    description: Parameter names should use camelCase (YouTube convention)\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete].parameters[*].name\n    then:\n      function: pattern\n      functionOptions:\n        match: ^[a-z][a-zA-Z0-9]*$\n\n  parameter-example:\n    description: Parameters should have example values\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].parameters[*]\n    then:\n      field: example\n      function: truthy\n\n  parameter-pagination-naming:\n    description: Pagination should use pageToken and maxResults (YouTube convention)\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].parameters[?(@.name=='page' || @.name=='offset' || @.name=='cursor')]\n    then:\n      field: name\n      function: pattern\n      functionOptions:\n        match: ^(pageToken|maxResults|pageSize)$\n\n  # ---------------------------------------------------------------------------\n\
  \  # REQUEST BODIES\n  # ---------------------------------------------------------------------------\n\n  request-body-json:\n    description: Request bodies should use application/json content type\n    severity: warn\n    given: $.paths[*][post,put,patch].requestBody.content\n    then:\n      field: application/json\n      function: truthy\n\n  # ---------------------------------------------------------------------------\n  # RESPONSES\n  # ---------------------------------------------------------------------------\n\n  response-success-required:\n    description: Every operation must have a 2xx success response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"200\"]\n            - required: [\"201\"]\n            - required: [\"204\"]\n\n  response-description-required:\n    description: Every response must have a description\n   \
  \ severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-json-content:\n    description: Success responses should use application/json\n    severity: warn\n    given: $.paths[*][get,post,put,patch].responses[?(@property >= 200 && @property < 300)].content\n    then:\n      field: application/json\n      function: truthy\n\n  response-examples:\n    description: Responses should include named examples for Microcks compatibility\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete].responses[*].content.application/json\n    then:\n      field: examples\n      function: truthy\n\n  # ---------------------------------------------------------------------------\n  # SCHEMAS — PROPERTY NAMING\n  # ---------------------------------------------------------------------------\n\n  schema-description:\n    description: Top-level schemas should have descriptions\n    severity: warn\n \
  \   given: $.components.schemas[*]\n    then:\n      field: description\n      function: truthy\n\n  schema-type-required:\n    description: Schema properties must define a type\n    severity: error\n    given: $.components.schemas[*].properties[*]\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"type\"]\n            - required: [\"$ref\"]\n            - required: [\"allOf\"]\n            - required: [\"oneOf\"]\n            - required: [\"anyOf\"]\n\n  schema-property-camel-case:\n    description: Schema property names should use camelCase (YouTube convention)\n    severity: warn\n    given: $.components.schemas[*].properties\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: ^[a-z][a-zA-Z0-9]*$\n\n  schema-kind-property:\n    description: YouTube resource schemas should include a kind property\n    severity: info\n    given: $.components.schemas[?(@.properties.etag)].properties\n\
  \    then:\n      field: kind\n      function: truthy\n\n  schema-etag-property:\n    description: YouTube resource schemas should include an etag property\n    severity: info\n    given: $.components.schemas[?(@.properties.kind)].properties\n    then:\n      field: etag\n      function: truthy\n\n  schema-property-example:\n    description: Schema properties should have example values\n    severity: info\n    given: $.components.schemas[*].properties[*]\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          anyOf:\n            - required: [\"example\"]\n            - required: [\"$ref\"]\n            - required: [\"enum\"]\n\n  # ---------------------------------------------------------------------------\n  # SECURITY\n  # ---------------------------------------------------------------------------\n\n  security-global-defined:\n    description: Global security must be defined\n    severity: error\n    given: $\n    then:\n      field: security\n      function:\
  \ truthy\n\n  security-schemes-defined:\n    description: Security schemes must be defined in components\n    severity: error\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  security-oauth2-scheme:\n    description: YouTube APIs should use OAuth 2.0 authentication\n    severity: warn\n    given: $.components.securitySchemes\n    then:\n      field: oauth2\n      function: truthy\n\n  security-api-key-scheme:\n    description: YouTube APIs should support API key authentication for read operations\n    severity: info\n    given: $.components.securitySchemes\n    then:\n      field: apiKey\n      function: truthy\n\n  # ---------------------------------------------------------------------------\n  # HTTP METHOD CONVENTIONS\n  # ---------------------------------------------------------------------------\n\n  http-get-no-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n\
  \      field: requestBody\n      function: falsy\n\n  http-delete-no-body:\n    description: DELETE operations must not have a request body\n    severity: error\n    given: $.paths[*].delete\n    then:\n      field: requestBody\n      function: falsy\n\n  http-post-has-body:\n    description: POST operations should have a request body\n    severity: warn\n    given: $.paths[*].post\n    then:\n      field: requestBody\n      function: truthy\n\n  http-put-has-body:\n    description: PUT operations should have a request body\n    severity: warn\n    given: $.paths[*].put\n    then:\n      field: requestBody\n      function: truthy\n\n  # ---------------------------------------------------------------------------\n  # MICROCKS COMPATIBILITY\n  # ---------------------------------------------------------------------------\n\n  microcks-operation-extension:\n    description: Operations should have x-microcks-operation for mock server compatibility\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete]\n\
  \    then:\n      field: x-microcks-operation\n      function: truthy\n\n  # ---------------------------------------------------------------------------\n  # GENERAL QUALITY\n  # ---------------------------------------------------------------------------\n\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: error\n    given: $..description\n    then:\n      function: truthy\n\n  deprecated-documented:\n    description: Deprecated operations should have a description explaining the deprecation\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete][?(@.deprecated==true)]\n    then:\n      field: description\n      function: truthy\n\n  list-response-items-array:\n    description: List responses should contain an items array (YouTube convention)\n    severity: info\n    given: $.components.schemas[?(@.properties.nextPageToken)].properties\n    then:\n      field: items\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/rules/youtube-spectral-rules.yml
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
- Spectral
- Linting
- API Governance
---
