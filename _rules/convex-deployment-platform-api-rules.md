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
rule_count: 5
rules:
- description: Deployment Platform API title must reference Convex Deployment Platform
  given: $.info.title
  name: convex-deploy-info-title
  severity: error
- description: At least one server URL must be defined
  given: $.servers
  name: convex-deploy-server-defined
  severity: error
- description: Deployment Platform API server URLs must match {deployment}.convex.cloud/api/v1
  given: $.servers[*].url
  name: convex-deploy-server-pattern
  severity: warn
- description: Tags must declare EnvironmentVariables or Configuration scope
  given: $.tags[*].name
  name: convex-deploy-tag-required
  severity: warn
- description: Every operation must define an operationId
  given: $.paths.*[get,put,post,delete,patch].operationId
  name: convex-deploy-operation-id-camelcase
  severity: error
rules_file: rules/convex-deployment-platform-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/convex/refs/heads/main/rules/convex-deployment-platform-api-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 2
slug: convex-deployment-platform-api-rules
source_filename: convex-deployment-platform-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - \"spectral:oas\"\ndocumentationUrl: https://docs.convex.dev/deployment-platform-api\nrules:\n  convex-deploy-info-title:\n    description: Deployment Platform API title must reference Convex Deployment Platform\n    severity: error\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(?i)Convex\\\\s+Deployment\\\\s+Platform\"\n  convex-deploy-server-defined:\n    description: At least one server URL must be defined\n    severity: error\n    given: \"$.servers\"\n    then:\n      function: length\n      functionOptions:\n        min: 1\n  convex-deploy-server-pattern:\n    description: Deployment Platform API server URLs must match {deployment}.convex.cloud/api/v1\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"convex\\\\.cloud/api/v1\"\n  convex-deploy-tag-required:\n    description: Tags must declare EnvironmentVariables or\
  \ Configuration scope\n    severity: warn\n    given: \"$.tags[*].name\"\n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - Configuration\n          - EnvironmentVariables\n          - Deployment\n  convex-deploy-operation-id-camelcase:\n    description: Every operation must define an operationId\n    severity: error\n    given: \"$.paths.*[get,put,post,delete,patch].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-zA-Z][a-zA-Z0-9_]+$\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/convex/refs/heads/main/rules/convex-deployment-platform-api-rules.yml
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
