---
api_specs:
- filename: coresignal-multi-source-company-api-openapi.yml
  format: yaml
  label: Coresignal Multi-source Company API
  slug: multi-source-company-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/coresignal/refs/heads/main/openapi/coresignal-multi-source-company-api-openapi.yml
- filename: coresignal-multi-source-employee-api-openapi.yml
  format: yaml
  label: Coresignal Multi-source Employee API
  slug: multi-source-employee-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/coresignal/refs/heads/main/openapi/coresignal-multi-source-employee-api-openapi.yml
- filename: coresignal-multi-source-jobs-api-openapi.yml
  format: yaml
  label: Coresignal Multi-source Jobs API
  slug: multi-source-jobs-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/coresignal/refs/heads/main/openapi/coresignal-multi-source-jobs-api-openapi.yml
categories:
- coresignal
description: Spectral linting rules defining API design standards and conventions for Coresignal.
layout: rules
name: Coresignal API Rules
provider_name: Coresignal
provider_slug: coresignal
rule_count: 7
rules:
- description: Servers must use HTTPS.
  given: $.servers[*].url
  name: coresignal-employee-server-https
  severity: error
- description: Base URL must reference api.coresignal.com/cdapi/v2/multi_source_employee.
  given: $.servers[*].url
  name: coresignal-employee-base-url
  severity: error
- description: API must use apikey header authentication.
  given: $.components.securitySchemes.apiKey.name
  name: coresignal-employee-apikey
  severity: error
- description: API should expose filter and Elasticsearch DSL search endpoints.
  given: $.paths
  name: coresignal-employee-search-paths
  severity: warn
- description: Description should acknowledge that records contain personal data.
  given: $.info.description
  name: coresignal-employee-pii-flag
  severity: info
- description: Operations must define an operationId.
  given: $.paths.*[get,post]
  name: coresignal-employee-operation-id
  severity: error
- description: Operations must define tags.
  given: $.paths.*[get,post]
  name: coresignal-employee-operation-tags
  severity: error
rules_file: rules/coresignal-multi-source-employee-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/coresignal/refs/heads/main/rules/coresignal-multi-source-employee-api-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 1
  warn: 1
slug: coresignal-multi-source-employee-api-rules
source_filename: coresignal-multi-source-employee-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [\"spectral:oas\"]\ndocumentationUrl: https://docs.coresignal.com/multi-source-employee-api/\nrules:\n  coresignal-employee-server-https:\n    description: Servers must use HTTPS.\n    given: \"$.servers[*].url\"\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  coresignal-employee-base-url:\n    description: Base URL must reference api.coresignal.com/cdapi/v2/multi_source_employee.\n    given: \"$.servers[*].url\"\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"api.coresignal.com/cdapi/v2/multi_source_employee\"\n  coresignal-employee-apikey:\n    description: API must use apikey header authentication.\n    given: \"$.components.securitySchemes.apiKey.name\"\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^apikey$\"\n  coresignal-employee-search-paths:\n    description: API should expose filter and Elasticsearch\
  \ DSL search endpoints.\n    given: \"$.paths\"\n    severity: warn\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - /search/filter\n            - /search/es_dsl\n            - /collect/{id}\n  coresignal-employee-pii-flag:\n    description: Description should acknowledge that records contain personal data.\n    given: \"$.info.description\"\n    severity: info\n    then:\n      function: pattern\n      functionOptions:\n        match: \"employee|profile|personal\"\n  coresignal-employee-operation-id:\n    description: Operations must define an operationId.\n    given: \"$.paths.*[get,post]\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n  coresignal-employee-operation-tags:\n    description: Operations must define tags.\n    given: \"$.paths.*[get,post]\"\n    severity: error\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/coresignal/refs/heads/main/rules/coresignal-multi-source-employee-api-rules.yml
tags:
- Agentic Search
- B2B Data
- Companies
- Company Data
- Data as a Service
- Elasticsearch
- Employee Data
- Employees
- Enrichment
- Firmographics
- Job Postings
- Jobs
- Lead Generation
- People Data
- Sales Intelligence
- Talent Intelligence
- Web Data
- Spectral
- Linting
- API Governance
---
