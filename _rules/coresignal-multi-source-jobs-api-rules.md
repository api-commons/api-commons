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
  name: coresignal-jobs-server-https
  severity: error
- description: Base URL must reference api.coresignal.com/cdapi/v2/multi_source_jobs.
  given: $.servers[*].url
  name: coresignal-jobs-base-url
  severity: error
- description: API must use apikey header authentication.
  given: $.components.securitySchemes.apiKey.name
  name: coresignal-jobs-apikey
  severity: error
- description: API should expose filter and Elasticsearch DSL search endpoints.
  given: $.paths
  name: coresignal-jobs-search-paths
  severity: warn
- description: Operations must define an operationId.
  given: $.paths.*[get,post]
  name: coresignal-jobs-operation-id
  severity: error
- description: Operations must define tags.
  given: $.paths.*[get,post]
  name: coresignal-jobs-operation-tags
  severity: error
- description: Date fields should use ISO 8601 date-time format.
  given: $.components.schemas.Job.properties.date_posted
  name: coresignal-jobs-date-format
  severity: warn
rules_file: rules/coresignal-multi-source-jobs-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/coresignal/refs/heads/main/rules/coresignal-multi-source-jobs-api-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 0
  warn: 2
slug: coresignal-multi-source-jobs-api-rules
source_filename: coresignal-multi-source-jobs-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [\"spectral:oas\"]\ndocumentationUrl: https://docs.coresignal.com/multi-source-jobs-api/\nrules:\n  coresignal-jobs-server-https:\n    description: Servers must use HTTPS.\n    given: \"$.servers[*].url\"\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  coresignal-jobs-base-url:\n    description: Base URL must reference api.coresignal.com/cdapi/v2/multi_source_jobs.\n    given: \"$.servers[*].url\"\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"api.coresignal.com/cdapi/v2/multi_source_jobs\"\n  coresignal-jobs-apikey:\n    description: API must use apikey header authentication.\n    given: \"$.components.securitySchemes.apiKey.name\"\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^apikey$\"\n  coresignal-jobs-search-paths:\n    description: API should expose filter and Elasticsearch DSL search endpoints.\n\
  \    given: \"$.paths\"\n    severity: warn\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - /search/filter\n            - /search/es_dsl\n            - /collect/{id}\n  coresignal-jobs-operation-id:\n    description: Operations must define an operationId.\n    given: \"$.paths.*[get,post]\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n  coresignal-jobs-operation-tags:\n    description: Operations must define tags.\n    given: \"$.paths.*[get,post]\"\n    severity: error\n    then:\n      field: tags\n      function: truthy\n  coresignal-jobs-date-format:\n    description: Date fields should use ISO 8601 date-time format.\n    given: \"$.components.schemas.Job.properties.date_posted\"\n    severity: warn\n    then:\n      field: format\n      function: pattern\n      functionOptions:\n        match: \"date-time\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/coresignal/refs/heads/main/rules/coresignal-multi-source-jobs-api-rules.yml
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
