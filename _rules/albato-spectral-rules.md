---
api_specs:
- filename: albato-automations-openapi.yaml
  format: yaml
  label: Albato Automations API
  slug: automations-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/albato-a-single-no-code-platform-for-all-automations/refs/heads/main/openapi/albato-automations-openapi.yaml
- filename: albato-connections-openapi.yaml
  format: yaml
  label: Albato Connections API
  slug: connections-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/albato-a-single-no-code-platform-for-all-automations/refs/heads/main/openapi/albato-connections-openapi.yaml
categories:
- albato
description: Spectral linting rules defining API design standards and conventions for Albato A Single No Code Platform For All Automations.
layout: rules
name: Albato A Single No Code Platform For All Automations API Rules
provider_name: Albato A Single No Code Platform For All Automations
provider_slug: albato-a-single-no-code-platform-for-all-automations
rule_count: 25
rules:
- description: Albato APIs must define API key authentication
  given: $.components.securitySchemes
  name: albato-auth-apikey-required
  severity: error
- description: Global security must be defined
  given: $.security[*]
  name: albato-global-security-defined
  severity: error
- description: API title must be present
  given: $.info
  name: albato-info-title
  severity: error
- description: API description must be present
  given: $.info
  name: albato-info-description
  severity: error
- description: API version must be present
  given: $.info
  name: albato-info-version
  severity: error
- description: Paths must not end with a trailing slash
  given: $.paths
  name: albato-path-no-trailing-slash
  severity: warn
- description: Paths must be lowercase with hyphens
  given: $.paths
  name: albato-path-lowercase
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: albato-operation-id-required
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: albato-operation-summary-required
  severity: error
- description: All operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: albato-operation-description-required
  severity: warn
- description: All operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: albato-operation-tags-required
  severity: error
- description: GET operations must define a 200 response
  given: $.paths[*].get.responses
  name: albato-response-200-get
  severity: error
- description: POST create operations should return 201
  given: $.paths[*].post.responses
  name: albato-response-201-post
  severity: warn
- description: Operations should document 401 Unauthorized
  given: $.paths[*].get.responses
  name: albato-response-401
  severity: warn
- description: Responses must use application/json
  given: $.paths[*][get,post,put].responses[200,201].content
  name: albato-response-json
  severity: error
- description: Schemas must have descriptions
  given: $.components.schemas[*]
  name: albato-schema-description
  severity: warn
- description: Schema properties must have types
  given: $.components.schemas[*].properties[*]
  name: albato-property-type
  severity: error
- description: Parameters should have descriptions
  given: $.paths[*][*].parameters[*]
  name: albato-parameter-description
  severity: warn
- description: Path parameters must have schemas
  given: $.paths[*][*].parameters[?(@.in=='path')]
  name: albato-path-param-schema
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][*].operationId
  name: albato-operation-id-camel-case
  severity: warn
- description: Schema names must use PascalCase
  given: $.components.schemas
  name: albato-schema-pascal-case
  severity: warn
- description: Request bodies must use application/json
  given: $.paths[*][post,put,patch].requestBody.content
  name: albato-request-body-json
  severity: error
- description: POST operations should have required request bodies
  given: $.paths[*].post.requestBody
  name: albato-request-body-required
  severity: warn
- description: API must define servers
  given: $
  name: albato-servers-defined
  severity: error
- description: Tags must be documented at root level
  given: $
  name: albato-tags-documented
  severity: warn
rules_file: rules/albato-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/albato-a-single-no-code-platform-for-all-automations/refs/heads/main/rules/albato-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 0
  warn: 10
slug: albato-spectral-rules
source_filename: albato-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # Authentication Rules\n  albato-auth-apikey-required:\n    description: Albato APIs must define API key authentication\n    message: Security scheme must include ApiKeyAuth\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      field: ApiKeyAuth\n      function: truthy\n\n  albato-global-security-defined:\n    description: Global security must be defined\n    message: Top-level security must reference ApiKeyAuth\n    severity: error\n    given: \"$.security[*]\"\n    then:\n      field: ApiKeyAuth\n      function: defined\n\n  # Info Rules\n  albato-info-title:\n    description: API title must be present\n    message: Info object must have a title\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  albato-info-description:\n    description: API description must be present\n    message: Info object must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field:\
  \ description\n      function: truthy\n\n  albato-info-version:\n    description: API version must be present\n    message: Info object must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # Path Rules\n  albato-path-no-trailing-slash:\n    description: Paths must not end with a trailing slash\n    message: \"Path '{{property}}' should not end with a trailing slash\"\n    severity: warn\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \".+/$\"\n\n  albato-path-lowercase:\n    description: Paths must be lowercase with hyphens\n    message: \"Path '{{property}}' must use lowercase with hyphens\"\n    severity: error\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"[A-Z_]\"\n\n  # Operation Rules\n  albato-operation-id-required:\n    description: All operations must have an operationId\n    message: Operation\
  \ must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  albato-operation-summary-required:\n    description: All operations must have a summary\n    message: Operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  albato-operation-description-required:\n    description: All operations should have a description\n    message: Operation should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  albato-operation-tags-required:\n    description: All operations must have tags\n    message: Operation must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  # Response\
  \ Rules\n  albato-response-200-get:\n    description: GET operations must define a 200 response\n    message: GET operation must define a 200 response\n    severity: error\n    given: \"$.paths[*].get.responses\"\n    then:\n      field: \"200\"\n      function: defined\n\n  albato-response-201-post:\n    description: POST create operations should return 201\n    message: POST operation should define a 201 response\n    severity: warn\n    given: \"$.paths[*].post.responses\"\n    then:\n      field: \"201\"\n      function: defined\n\n  albato-response-401:\n    description: Operations should document 401 Unauthorized\n    message: Operations should define a 401 response\n    severity: warn\n    given: \"$.paths[*].get.responses\"\n    then:\n      field: \"401\"\n      function: defined\n\n  albato-response-json:\n    description: Responses must use application/json\n    message: Response must define application/json content type\n    severity: error\n    given: \"$.paths[*][get,post,put].responses[200,201].content\"\
  \n    then:\n      field: application/json\n      function: defined\n\n  # Schema Rules\n  albato-schema-description:\n    description: Schemas must have descriptions\n    message: Schema must have a description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  albato-property-type:\n    description: Schema properties must have types\n    message: Property must define a type\n    severity: error\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: type\n      function: truthy\n\n  # Parameter Rules\n  albato-parameter-description:\n    description: Parameters should have descriptions\n    message: Parameter should have a description\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  albato-path-param-schema:\n    description: Path parameters must have schemas\n    message: Path parameter must define a schema\n\
  \    severity: error\n    given: \"$.paths[*][*].parameters[?(@.in=='path')]\"\n    then:\n      field: schema\n      function: truthy\n\n  # Naming Conventions\n  albato-operation-id-camel-case:\n    description: operationId must use camelCase\n    message: \"operationId '{{value}}' must use camelCase\"\n    severity: warn\n    given: \"$.paths[*][*].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  albato-schema-pascal-case:\n    description: Schema names must use PascalCase\n    message: \"Schema '{{property}}' must use PascalCase\"\n    severity: warn\n    given: \"$.components.schemas\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*$\"\n\n  # Request Body Rules\n  albato-request-body-json:\n    description: Request bodies must use application/json\n    message: Request body must define application/json\n    severity: error\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\
  \n    then:\n      field: application/json\n      function: defined\n\n  albato-request-body-required:\n    description: POST operations should have required request bodies\n    message: POST request body should be marked required\n    severity: warn\n    given: \"$.paths[*].post.requestBody\"\n    then:\n      field: required\n      function: truthy\n\n  # Server Rules\n  albato-servers-defined:\n    description: API must define servers\n    message: API must include servers section\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  albato-tags-documented:\n    description: Tags must be documented at root level\n    message: Tags used in operations should be defined at root level\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/albato-a-single-no-code-platform-for-all-automations/refs/heads/main/rules/albato-spectral-rules.yml
tags:
- No-Code Automation
- Workflow Automation
- App Integration
- Embedded iPaaS
- Integrations
- Webhooks
- Spectral
- Linting
- API Governance
---
