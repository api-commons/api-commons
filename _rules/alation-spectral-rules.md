---
api_specs:
- filename: alation-data-catalog-openapi.yaml
  format: yaml
  label: Alation Data Catalog API
  slug: data-catalog-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/alation/refs/heads/main/openapi/alation-data-catalog-openapi.yaml
- filename: alation-lineage-openapi.yaml
  format: yaml
  label: Alation Lineage API
  slug: lineage-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/alation/refs/heads/main/openapi/alation-lineage-openapi.yaml
- filename: alation-governance-openapi.yaml
  format: yaml
  label: Alation Governance API
  slug: governance-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/alation/refs/heads/main/openapi/alation-governance-openapi.yaml
- filename: alation-search-openapi.yaml
  format: yaml
  label: Alation Search API
  slug: search-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/alation/refs/heads/main/openapi/alation-search-openapi.yaml
categories:
- alation
description: Spectral linting rules defining API design standards and conventions for Alation.
layout: rules
name: Alation API Rules
provider_name: Alation
provider_slug: alation
rule_count: 26
rules:
- description: Alation APIs must use bearer token authentication
  given: $.components.securitySchemes
  name: alation-auth-bearer-required
  severity: error
- description: Global security must be defined
  given: $.security[*]
  name: alation-global-security-defined
  severity: error
- description: API title must be present
  given: $.info
  name: alation-info-title
  severity: error
- description: API description must be present
  given: $.info
  name: alation-info-description
  severity: error
- description: API version must be present
  given: $.info
  name: alation-info-version
  severity: error
- description: Alation API paths must end with a trailing slash
  given: $.paths
  name: alation-path-trailing-slash
  severity: warn
- description: Paths must be lowercase
  given: $.paths
  name: alation-path-no-uppercase
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: alation-operation-id-required
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: alation-operation-summary-required
  severity: error
- description: All operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: alation-operation-description-required
  severity: warn
- description: All operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: alation-operation-tags-required
  severity: error
- description: GET operations must define a 200 response
  given: $.paths[*].get.responses
  name: alation-response-200-required
  severity: error
- description: POST operations that create resources should return 201
  given: $.paths[*].post.responses
  name: alation-response-201-post
  severity: warn
- description: APIs must document 401 Unauthorized
  given: $.paths[*][get,post,put,patch,delete].responses
  name: alation-response-401-required
  severity: warn
- description: Successful responses must specify content type
  given: $.paths[*][get,post,put,patch,delete].responses[200,201].content
  name: alation-response-content-type
  severity: error
- description: All schemas must have descriptions
  given: $.components.schemas[*]
  name: alation-schema-description
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: alation-property-description
  severity: info
- description: Reuse schemas via $ref rather than inlining
  given: $.paths[*][*].responses[*].content[*].schema
  name: alation-no-inline-schemas
  severity: warn
- description: Parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: alation-parameter-description
  severity: warn
- description: List operations should support limit parameter
  given: $.paths[*].get.parameters[*]
  name: alation-pagination-limit
  severity: info
- description: operationId must use camelCase
  given: $.paths[*][*].operationId
  name: alation-operation-id-camel-case
  severity: warn
- description: Schema names must use PascalCase
  given: $.components.schemas
  name: alation-schema-name-pascal-case
  severity: warn
- description: Request bodies must specify application/json
  given: $.paths[*][post,put,patch].requestBody.content
  name: alation-request-body-content-type
  severity: error
- description: Request bodies must have a schema
  given: $.paths[*][post,put,patch].requestBody.content.application/json
  name: alation-request-body-schema
  severity: error
- description: API must define at least one server
  given: $
  name: alation-servers-required
  severity: error
- description: All operation tags must be defined at root level
  given: $
  name: alation-tags-defined
  severity: warn
rules_file: rules/alation-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/alation/refs/heads/main/rules/alation-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 2
  warn: 10
slug: alation-spectral-rules
source_filename: alation-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  # Authentication Rules\n  alation-auth-bearer-required:\n    description: Alation APIs must use bearer token authentication\n    message: Security scheme must include BearerToken\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      field: BearerToken\n      function: truthy\n\n  alation-global-security-defined:\n    description: Global security must be defined\n    message: Top-level security must reference BearerToken\n    severity: error\n    given: \"$.security[*]\"\n    then:\n      field: BearerToken\n      function: defined\n\n  # Info Rules\n  alation-info-title:\n    description: API title must be present\n    message: Info object must have a title\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  alation-info-description:\n    description: API description must be present\n    message: Info object must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n\
  \      field: description\n      function: truthy\n\n  alation-info-version:\n    description: API version must be present\n    message: Info object must have a version\n    severity: error\n    given: \"$.info\"\n    then:\n      field: version\n      function: truthy\n\n  # Path Rules\n  alation-path-trailing-slash:\n    description: Alation API paths must end with a trailing slash\n    message: \"Path '{{property}}' should end with a trailing slash\"\n    severity: warn\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \".*/$\"\n\n  alation-path-no-uppercase:\n    description: Paths must be lowercase\n    message: \"Path '{{property}}' must not contain uppercase letters\"\n    severity: error\n    given: \"$.paths\"\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"[A-Z]\"\n\n  # Operation Rules\n  alation-operation-id-required:\n    description: All operations must have an operationId\n    message: Operation\
  \ must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  alation-operation-summary-required:\n    description: All operations must have a summary\n    message: Operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  alation-operation-description-required:\n    description: All operations must have a description\n    message: Operation should have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: description\n      function: truthy\n\n  alation-operation-tags-required:\n    description: All operations must have tags\n    message: Operation must have at least one tag\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: truthy\n\n  # Response\
  \ Rules\n  alation-response-200-required:\n    description: GET operations must define a 200 response\n    message: GET operation must define a 200 response\n    severity: error\n    given: \"$.paths[*].get.responses\"\n    then:\n      field: \"200\"\n      function: defined\n\n  alation-response-201-post:\n    description: POST operations that create resources should return 201\n    message: POST operation should define a 201 response\n    severity: warn\n    given: \"$.paths[*].post.responses\"\n    then:\n      field: \"201\"\n      function: defined\n\n  alation-response-401-required:\n    description: APIs must document 401 Unauthorized\n    message: Operations should define a 401 response\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete].responses\"\n    then:\n      field: \"401\"\n      function: defined\n\n  alation-response-content-type:\n    description: Successful responses must specify content type\n    message: Response must define content type\n  \
  \  severity: error\n    given: \"$.paths[*][get,post,put,patch,delete].responses[200,201].content\"\n    then:\n      field: application/json\n      function: defined\n\n  # Schema Rules\n  alation-schema-description:\n    description: All schemas must have descriptions\n    message: Schema must have a description\n    severity: warn\n    given: \"$.components.schemas[*]\"\n    then:\n      field: description\n      function: truthy\n\n  alation-property-description:\n    description: Schema properties should have descriptions\n    message: Schema property should have a description\n    severity: info\n    given: \"$.components.schemas[*].properties[*]\"\n    then:\n      field: description\n      function: truthy\n\n  alation-no-inline-schemas:\n    description: Reuse schemas via $ref rather than inlining\n    message: Use $ref for complex schemas\n    severity: warn\n    given: \"$.paths[*][*].responses[*].content[*].schema\"\n    then:\n      function: schema\n      functionOptions:\n\
  \        schema:\n          oneOf:\n            - required: [\"$ref\"]\n            - required: [\"type\"]\n\n  # Parameter Rules\n  alation-parameter-description:\n    description: Parameters must have descriptions\n    message: Parameter must have a description\n    severity: warn\n    given: \"$.paths[*][*].parameters[*]\"\n    then:\n      field: description\n      function: truthy\n\n  alation-pagination-limit:\n    description: List operations should support limit parameter\n    message: List operations should support a limit query parameter\n    severity: info\n    given: \"$.paths[*].get.parameters[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          properties:\n            name:\n              enum: [limit, skip, page, page_size]\n\n  # Naming Conventions\n  alation-operation-id-camel-case:\n    description: operationId must use camelCase\n    message: \"operationId '{{value}}' must use camelCase\"\n    severity: warn\n    given: \"$.paths[*][*].operationId\"\
  \n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  alation-schema-name-pascal-case:\n    description: Schema names must use PascalCase\n    message: \"Schema '{{property}}' must use PascalCase\"\n    severity: warn\n    given: \"$.components.schemas\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[A-Z][a-zA-Z0-9]*$\"\n\n  # Request Body Rules\n  alation-request-body-content-type:\n    description: Request bodies must specify application/json\n    message: Request body must define application/json content type\n    severity: error\n    given: \"$.paths[*][post,put,patch].requestBody.content\"\n    then:\n      field: application/json\n      function: defined\n\n  alation-request-body-schema:\n    description: Request bodies must have a schema\n    message: Request body content must define a schema\n    severity: error\n    given: \"$.paths[*][post,put,patch].requestBody.content.application/json\"\n \
  \   then:\n      field: schema\n      function: truthy\n\n  # Documentation Rules\n  alation-servers-required:\n    description: API must define at least one server\n    message: API must define servers\n    severity: error\n    given: \"$\"\n    then:\n      field: servers\n      function: truthy\n\n  alation-tags-defined:\n    description: All operation tags must be defined at root level\n    message: Tags used in operations should be defined at the root tags section\n    severity: warn\n    given: \"$\"\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/alation/refs/heads/main/rules/alation-spectral-rules.yml
tags:
- Data Catalog
- Data Governance
- Data Intelligence
- Data Lineage
- Data Quality
- Business Glossary
- Metadata Management
- AI
- Spectral
- Linting
- API Governance
---
