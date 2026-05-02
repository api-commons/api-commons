---
api_specs:
- filename: backstage-catalog-openapi.yml
  format: yaml
  label: Backstage Catalog API
  slug: catalog-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/backstage/refs/heads/main/openapi/backstage-catalog-openapi.yml
- filename: backstage-scaffolder-openapi.yml
  format: yaml
  label: Backstage Scaffolder API
  slug: scaffolder-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/backstage/refs/heads/main/openapi/backstage-scaffolder-openapi.yml
- filename: backstage-auth-openapi.yml
  format: yaml
  label: Backstage Auth API
  slug: auth-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/backstage/refs/heads/main/openapi/backstage-auth-openapi.yml
- filename: backstage-techdocs-openapi.yml
  format: yaml
  label: Backstage TechDocs API
  slug: techdocs-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/backstage/refs/heads/main/openapi/backstage-techdocs-openapi.yml
- filename: backstage-search-openapi.yml
  format: yaml
  label: Backstage Search API
  slug: search-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/backstage/refs/heads/main/openapi/backstage-search-openapi.yml
- filename: backstage-permissions-openapi.yml
  format: yaml
  label: Backstage Permissions API
  slug: permissions-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/backstage/refs/heads/main/openapi/backstage-permissions-openapi.yml
- filename: backstage-events-asyncapi.yml
  format: yaml
  label: Backstage Events System
  slug: events-system
  spec_type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/backstage/refs/heads/main/asyncapi/backstage-events-asyncapi.yml
categories:
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
description: Spectral linting rules defining API design standards and conventions for Backstage.
layout: rules
name: Backstage API Rules
provider_name: Backstage
provider_slug: backstage
rule_count: 21
rules:
- description: Info must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: Info must have a description
  given: $.info
  name: info-description-required
  severity: warn
- description: Info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.0.x or 3.1.x
  given: $
  name: openapi-version-3
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: OperationIds should use camelCase
  given: $.paths[*][get,post,put,patch,delete,head,options].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: warn
- description: Operation summaries should start with "Backstage"
  given: $.paths[*][get,post,put,patch,delete,head,options].summary
  name: operation-summary-backstage-prefix
  severity: info
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete,head,options].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Protected operations should define a 401 response
  given: $.paths[*][post,put,patch,delete]
  name: response-401-defined
  severity: info
- description: All schemas should have a type
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes must be defined if auth is used
  given: $.components
  name: security-schemes-defined
  severity: info
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/backstage-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/backstage/refs/heads/main/rules/backstage-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 3
  warn: 10
slug: backstage-spectral-rules
source_filename: backstage-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n\n  # INFO / METADATA\n  info-title-required:\n    description: Info must have a title\n    severity: error\n    given: $.info\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: Info must have a description\n    severity: warn\n    given: $.info\n    then:\n      field: description\n      function: truthy\n\n  info-version-required:\n    description: Info must have a version\n    severity: error\n    given: $.info\n    then:\n      field: version\n      function: truthy\n\n  # OPENAPI VERSION\n  openapi-version-3:\n    description: Must use OpenAPI 3.0.x or 3.1.x\n    severity: error\n    given: $\n    then:\n      field: openapi\n      function: pattern\n      functionOptions:\n        match: \"^3\\\\.\"\n\n  # SERVERS\n  servers-defined:\n    description: Servers must be defined\n    severity: warn\n    given: $\n    then:\n      field: servers\n      function: truthy\n\n  # PATHS — NAMING CONVENTIONS\n  paths-kebab-case:\n\
  \    description: Path segments should use kebab-case\n    severity: warn\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(/[a-z0-9][a-z0-9-]*(/[a-z0-9][a-z0-9-]*|/\\\\{[a-zA-Z0-9_]+\\\\})*)*$\"\n\n  paths-no-trailing-slash:\n    description: Paths must not have trailing slashes\n    severity: warn\n    given: $.paths\n    then:\n      function: pattern\n      functionOptions:\n        notMatch: \"/$\"\n\n  # OPERATIONS\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: summary\n      function: truthy\n\n  operation-description-required:\n    description: Every operation must have a description\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: description\n      function: truthy\n\n  operation-id-required:\n    description: Every operation\
  \ must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: operationId\n      function: truthy\n\n  operation-id-camel-case:\n    description: OperationIds should use camelCase\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options].operationId\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]*$\"\n\n  operation-tags-required:\n    description: Every operation must have at least one tag\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options]\n    then:\n      field: tags\n      function: truthy\n\n  operation-summary-backstage-prefix:\n    description: Operation summaries should start with \"Backstage\"\n    severity: info\n    given: $.paths[*][get,post,put,patch,delete,head,options].summary\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^Backstage\"\n\n  # PARAMETERS\n  parameter-description-required:\n\
  \    description: All parameters must have descriptions\n    severity: warn\n    given: $.paths[*][get,post,put,patch,delete,head,options].parameters[*]\n    then:\n      field: description\n      function: truthy\n\n  # RESPONSES\n  response-success-required:\n    description: Every operation must have at least one 2xx response\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then:\n      field: responses\n      function: truthy\n\n  response-description-required:\n    description: Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then:\n      field: description\n      function: truthy\n\n  response-401-defined:\n    description: Protected operations should define a 401 response\n    severity: info\n    given: $.paths[*][post,put,patch,delete]\n    then:\n      field: responses.401\n      function: truthy\n\n  # SCHEMAS\n  schema-type-defined:\n    description: All schemas should have\
  \ a type\n    severity: warn\n    given: $.components.schemas[*]\n    then:\n      field: type\n      function: truthy\n\n  # SECURITY\n  security-schemes-defined:\n    description: Security schemes must be defined if auth is used\n    severity: info\n    given: $.components\n    then:\n      field: securitySchemes\n      function: truthy\n\n  # HTTP METHOD CONVENTIONS\n  get-no-request-body:\n    description: GET operations must not have a request body\n    severity: error\n    given: $.paths[*].get\n    then:\n      field: requestBody\n      function: falsy\n\n  # GENERAL QUALITY\n  no-empty-descriptions:\n    description: Descriptions must not be empty strings\n    severity: warn\n    given: $..description\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/backstage/refs/heads/main/rules/backstage-spectral-rules.yml
tags:
- Developer Portal
- Internal Developer Platform
- Software Catalog
- Open Source
- Spectral
- Linting
- API Governance
---
