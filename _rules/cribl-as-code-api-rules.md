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
  name: cribl-as-code-info-contact
  severity: error
- description: Server URL should reference gateway.cribl.cloud.
  given: $.servers[*].url
  name: cribl-as-code-server-gateway
  severity: warn
- description: API must declare bearerAuth security scheme.
  given: $.components.securitySchemes
  name: cribl-as-code-bearer-auth
  severity: error
- description: As Code API must define export and import configuration paths.
  given: $.paths
  name: cribl-as-code-config-paths
  severity: error
- description: All operations must define an operationId.
  given: $.paths.*.*
  name: cribl-as-code-operation-id
  severity: error
- description: All operations must define tags.
  given: $.paths.*.*
  name: cribl-as-code-tags
  severity: error
rules_file: rules/cribl-as-code-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cribl/refs/heads/main/rules/cribl-as-code-api-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 0
  warn: 1
slug: cribl-as-code-api-rules
source_filename: cribl-as-code-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [\"spectral:oas\"]\ndocumentationUrl: https://docs.cribl.io/cribl-as-code/api/\nrules:\n  cribl-as-code-info-contact:\n    description: API info object should reference Cribl support contact.\n    given: \"$.info.contact\"\n    severity: error\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"cribl\"\n  cribl-as-code-server-gateway:\n    description: Server URL should reference gateway.cribl.cloud.\n    given: \"$.servers[*].url\"\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"gateway\\\\.cribl\\\\.cloud\"\n  cribl-as-code-bearer-auth:\n    description: API must declare bearerAuth security scheme.\n    given: \"$.components.securitySchemes\"\n    severity: error\n    then:\n      field: bearerAuth\n      function: truthy\n  cribl-as-code-config-paths:\n    description: As Code API must define export and import configuration paths.\n    given: \"$.paths\"\n    severity:\
  \ error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - /export\n            - /import\n  cribl-as-code-operation-id:\n    description: All operations must define an operationId.\n    given: \"$.paths.*.*\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n  cribl-as-code-tags:\n    description: All operations must define tags.\n    given: \"$.paths.*.*\"\n    severity: error\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cribl/refs/heads/main/rules/cribl-as-code-api-rules.yml
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
