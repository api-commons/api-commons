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
rule_count: 9
rules:
- description: API info object should declare contact information.
  given: $.info
  name: coresignal-info-contact
  severity: error
- description: Servers must use HTTPS.
  given: $.servers[*].url
  name: coresignal-server-https
  severity: error
- description: Base URL must reference api.coresignal.com.
  given: $.servers[*].url
  name: coresignal-base-url
  severity: error
- description: Operations must require apikey authentication.
  given: $.components.securitySchemes.apiKey
  name: coresignal-apikey-security
  severity: error
- description: API should expose search and collect paths.
  given: $.paths
  name: coresignal-search-collect-paths
  severity: warn
- description: Operations must define an operationId.
  given: $.paths.*[get,post]
  name: coresignal-operation-id
  severity: error
- description: Operations must define tags.
  given: $.paths.*[get,post]
  name: coresignal-operation-tags
  severity: error
- description: Search operations should document a 402 credits-exhausted response.
  given: $.paths['/search/filter','/search/es_dsl'].post.responses
  name: coresignal-credits-error
  severity: warn
- description: Search operations should document a 429 rate-limit response.
  given: $.paths['/search/filter','/search/es_dsl'].post.responses
  name: coresignal-rate-limit-error
  severity: warn
rules_file: rules/coresignal-multi-source-company-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/coresignal/refs/heads/main/rules/coresignal-multi-source-company-api-rules.yml
severity_counts:
  error: 6
  hint: 0
  info: 0
  warn: 3
slug: coresignal-multi-source-company-api-rules
source_filename: coresignal-multi-source-company-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [\"spectral:oas\"]\ndocumentationUrl: https://docs.coresignal.com/multi-source-company-api/\nrules:\n  coresignal-info-contact:\n    description: API info object should declare contact information.\n    given: \"$.info\"\n    severity: error\n    then:\n      field: contact\n      function: truthy\n  coresignal-server-https:\n    description: Servers must use HTTPS.\n    given: \"$.servers[*].url\"\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n  coresignal-base-url:\n    description: Base URL must reference api.coresignal.com.\n    given: \"$.servers[*].url\"\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"api.coresignal.com\"\n  coresignal-apikey-security:\n    description: Operations must require apikey authentication.\n    given: \"$.components.securitySchemes.apiKey\"\n    severity: error\n    then:\n      field: name\n      function: pattern\n \
  \     functionOptions:\n        match: \"^apikey$\"\n  coresignal-search-collect-paths:\n    description: API should expose search and collect paths.\n    given: \"$.paths\"\n    severity: warn\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - /search/filter\n            - /search/es_dsl\n            - /collect/{id}\n  coresignal-operation-id:\n    description: Operations must define an operationId.\n    given: \"$.paths.*[get,post]\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n  coresignal-operation-tags:\n    description: Operations must define tags.\n    given: \"$.paths.*[get,post]\"\n    severity: error\n    then:\n      field: tags\n      function: truthy\n  coresignal-credits-error:\n    description: Search operations should document a 402 credits-exhausted response.\n    given: \"$.paths['/search/filter','/search/es_dsl'].post.responses\"\n    severity: warn\n\
  \    then:\n      field: '402'\n      function: truthy\n  coresignal-rate-limit-error:\n    description: Search operations should document a 429 rate-limit response.\n    given: \"$.paths['/search/filter','/search/es_dsl'].post.responses\"\n    severity: warn\n    then:\n      field: '429'\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/coresignal/refs/heads/main/rules/coresignal-multi-source-company-api-rules.yml
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
