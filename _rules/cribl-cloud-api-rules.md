---
api_specs:
- filename: cribl-cloud-api-openapi.yml
  format: yaml
  label: Cribl Cloud API
  slug: cribl-cloud-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cribl/refs/heads/main/openapi/cribl-cloud-api-openapi.yml
- filename: cribl-stream-api-openapi.yml
  format: yaml
  label: Cribl Stream API
  slug: cribl-stream-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cribl/refs/heads/main/openapi/cribl-stream-api-openapi.yml
- filename: cribl-edge-api-openapi.yml
  format: yaml
  label: Cribl Edge API
  slug: cribl-edge-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cribl/refs/heads/main/openapi/cribl-edge-api-openapi.yml
- filename: cribl-search-api-openapi.yml
  format: yaml
  label: Cribl Search API
  slug: cribl-search-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cribl/refs/heads/main/openapi/cribl-search-api-openapi.yml
- filename: cribl-lake-api-openapi.yml
  format: yaml
  label: Cribl Lake API
  slug: cribl-lake-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cribl/refs/heads/main/openapi/cribl-lake-api-openapi.yml
- filename: cribl-as-code-api-openapi.yml
  format: yaml
  label: Cribl As Code API
  slug: cribl-as-code-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cribl/refs/heads/main/openapi/cribl-as-code-api-openapi.yml
categories:
- cribl
description: Spectral linting rules defining API design standards and conventions for Cribl.
layout: rules
name: Cribl API Rules
provider_name: Cribl
provider_slug: cribl
rule_count: 6
rules:
- description: API info object should reference Cribl support contact.
  given: $.info.contact
  name: cribl-cloud-info-contact
  severity: error
- description: Server URL should reference cribl.cloud workspace pattern or on-prem deployment.
  given: $.servers[*].url
  name: cribl-cloud-server-cribl-cloud
  severity: warn
- description: API must declare bearerAuth security scheme for Bearer tokens.
  given: $.components.securitySchemes
  name: cribl-cloud-bearer-auth
  severity: error
- description: Cloud API must define authentication, health, and core resource paths.
  given: $.paths
  name: cribl-cloud-required-paths
  severity: error
- description: All operations must define an operationId.
  given: $.paths.*.*
  name: cribl-cloud-operation-id
  severity: error
- description: All operations must define tags.
  given: $.paths.*.*
  name: cribl-cloud-tags
  severity: error
rules_file: rules/cribl-cloud-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cribl/refs/heads/main/rules/cribl-cloud-api-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 0
  warn: 1
slug: cribl-cloud-api-rules
source_filename: cribl-cloud-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [\"spectral:oas\"]\ndocumentationUrl: https://docs.cribl.io/api-reference/\nrules:\n  cribl-cloud-info-contact:\n    description: API info object should reference Cribl support contact.\n    given: \"$.info.contact\"\n    severity: error\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"cribl\"\n  cribl-cloud-server-cribl-cloud:\n    description: Server URL should reference cribl.cloud workspace pattern or on-prem deployment.\n    given: \"$.servers[*].url\"\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(cribl\\\\.cloud|api/v1)\"\n  cribl-cloud-bearer-auth:\n    description: API must declare bearerAuth security scheme for Bearer tokens.\n    given: \"$.components.securitySchemes\"\n    severity: error\n    then:\n      field: bearerAuth\n      function: truthy\n  cribl-cloud-required-paths:\n    description: Cloud API must define authentication, health, and core resource\
  \ paths.\n    given: \"$.paths\"\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - /auth/login\n            - /health\n            - /system/sources\n  cribl-cloud-operation-id:\n    description: All operations must define an operationId.\n    given: \"$.paths.*.*\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n  cribl-cloud-tags:\n    description: All operations must define tags.\n    given: \"$.paths.*.*\"\n    severity: error\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cribl/refs/heads/main/rules/cribl-cloud-api-rules.yml
tags:
- Configuration
- Data Lake
- Data Pipelines
- Data Routing
- Edge Computing
- Infrastructure as Code
- Observability
- Search
- Security Data
- Stream Processing
- Telemetry
- Spectral
- Linting
- API Governance
---
