---
api_specs:
- filename: convex-http-api-openapi.yml
  format: yaml
  label: Convex HTTP API
  slug: http-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/convex/refs/heads/main/openapi/convex-http-api-openapi.yml
- filename: openapi.json
  format: json
  label: Convex Management API
  slug: management-api
  spec_type: OpenAPI
  url: https://api.convex.dev/v1/openapi.json
- filename: convex-deployment-platform-api-openapi.yml
  format: yaml
  label: Convex Deployment Platform API
  slug: deployment-platform-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/convex/refs/heads/main/openapi/convex-deployment-platform-api-openapi.yml
categories:
- convex
description: Spectral linting rules defining API design standards and conventions for Convex.
layout: rules
name: Convex API Rules
provider_name: Convex
provider_slug: convex
rule_count: 7
rules:
- description: Management API OpenAPI info.title must reference Convex Management
  given: $.info.title
  name: convex-mgmt-info-title
  severity: error
- description: At least one server URL must be defined
  given: $.servers
  name: convex-mgmt-server-defined
  severity: error
- description: Management API server URL must point to api.convex.dev
  given: $.servers[*].url
  name: convex-mgmt-server-host
  severity: error
- description: Management API must declare bearer authentication
  given: $.components.securitySchemes
  name: convex-mgmt-bearer-auth
  severity: error
- description: Tags must declare Projects, Deployments, Teams, AccessTokens, DeployKeys, CustomDomains, or EnvironmentVariables scope
  given: $.tags[*].name
  name: convex-mgmt-tag-required
  severity: warn
- description: Every operation must define an operationId in camelCase or snake_case
  given: $.paths.*[get,put,post,delete,patch].operationId
  name: convex-mgmt-operation-id-camelcase
  severity: warn
- description: Management API paths must live under /teams, /projects, /deployments, or /token
  given: $.paths
  name: convex-mgmt-paths-prefix
  severity: warn
rules_file: rules/convex-management-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/convex/refs/heads/main/rules/convex-management-api-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 3
slug: convex-management-api-rules
source_filename: convex-management-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - \"spectral:oas\"\ndocumentationUrl: https://docs.convex.dev/management-api\nrules:\n  convex-mgmt-info-title:\n    description: Management API OpenAPI info.title must reference Convex Management\n    severity: error\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(?i)Convex\\\\s+Management\"\n  convex-mgmt-server-defined:\n    description: At least one server URL must be defined\n    severity: error\n    given: \"$.servers\"\n    then:\n      function: length\n      functionOptions:\n        min: 1\n  convex-mgmt-server-host:\n    description: Management API server URL must point to api.convex.dev\n    severity: error\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"https://api\\\\.convex\\\\.dev/v1\"\n  convex-mgmt-bearer-auth:\n    description: Management API must declare bearer authentication\n    severity: error\n    given: \"$.components.securitySchemes\"\
  \n    then:\n      function: defined\n  convex-mgmt-tag-required:\n    description: Tags must declare Projects, Deployments, Teams, AccessTokens, DeployKeys, CustomDomains, or EnvironmentVariables scope\n    severity: warn\n    given: \"$.tags[*].name\"\n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - AccessTokens\n          - CustomDomains\n          - DeployKeys\n          - Deployments\n          - EnvironmentVariables\n          - Projects\n          - Teams\n  convex-mgmt-operation-id-camelcase:\n    description: Every operation must define an operationId in camelCase or snake_case\n    severity: warn\n    given: \"$.paths.*[get,put,post,delete,patch].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-zA-Z][a-zA-Z0-9_]+$\"\n  convex-mgmt-paths-prefix:\n    description: Management API paths must live under /teams, /projects, /deployments, or /token\n    severity: warn\n    given: \"$.paths\"\n\
  \    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^/(teams|projects|deployments|token|list_personal_access_tokens|create_personal_access_token|delete_personal_access_token)\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/convex/refs/heads/main/rules/convex-management-api-rules.yml
tags:
- Backend
- Database
- Functions
- Real-Time
- Reactive
- Serverless
- TypeScript
- Spectral
- Linting
- API Governance
---
