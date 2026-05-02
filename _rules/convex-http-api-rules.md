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
- description: HTTP API OpenAPI info.title must reference Convex HTTP API
  given: $.info.title
  name: convex-http-info-title
  severity: error
- description: At least one server URL must be defined for the deployment
  given: $.servers
  name: convex-http-server-defined
  severity: error
- description: HTTP API server URLs must match the convex.cloud deployment pattern
  given: $.servers[*].url
  name: convex-http-server-pattern
  severity: warn
- description: Tags must declare Queries, Mutations, Actions, or Functions scope
  given: $.tags[*].name
  name: convex-http-tag-required
  severity: warn
- description: Every operation must define an operationId using camelCase
  given: $.paths.*[get,put,post,delete,patch].operationId
  name: convex-http-operation-id-camelcase
  severity: error
- description: HTTP API paths must live under /api
  given: $.paths
  name: convex-http-paths-prefix
  severity: error
- description: Function execution endpoints must be POST
  given: $.paths[?(@property =~ /^\/api\/(query|mutation|action|run)/)]
  name: convex-http-post-only
  severity: warn
rules_file: rules/convex-http-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/convex/refs/heads/main/rules/convex-http-api-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 3
slug: convex-http-api-rules
source_filename: convex-http-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - \"spectral:oas\"\ndocumentationUrl: https://docs.convex.dev/http-api/\nrules:\n  convex-http-info-title:\n    description: HTTP API OpenAPI info.title must reference Convex HTTP API\n    severity: error\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(?i)Convex\\\\s+HTTP\"\n  convex-http-server-defined:\n    description: At least one server URL must be defined for the deployment\n    severity: error\n    given: \"$.servers\"\n    then:\n      function: length\n      functionOptions:\n        min: 1\n  convex-http-server-pattern:\n    description: HTTP API server URLs must match the convex.cloud deployment pattern\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"convex\\\\.cloud\"\n  convex-http-tag-required:\n    description: Tags must declare Queries, Mutations, Actions, or Functions scope\n    severity: warn\n    given:\
  \ \"$.tags[*].name\"\n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - Queries\n          - Mutations\n          - Actions\n          - Functions\n  convex-http-operation-id-camelcase:\n    description: Every operation must define an operationId using camelCase\n    severity: error\n    given: \"$.paths.*[get,put,post,delete,patch].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n  convex-http-paths-prefix:\n    description: HTTP API paths must live under /api\n    severity: error\n    given: \"$.paths\"\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^/api/\"\n  convex-http-post-only:\n    description: Function execution endpoints must be POST\n    severity: warn\n    given: \"$.paths[?(@property =~ /^\\\\/api\\\\/(query|mutation|action|run)/)]\"\n    then:\n      function: defined\n      field: post\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/convex/refs/heads/main/rules/convex-http-api-rules.yml
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
