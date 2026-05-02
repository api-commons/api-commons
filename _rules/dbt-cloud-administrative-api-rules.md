---
api_specs:
- filename: dbt-cloud-administrative-api-openapi.yml
  format: yaml
  label: dbt Cloud Administrative API
  slug: dbt-cloud-administrative-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dbt/refs/heads/main/openapi/dbt-cloud-administrative-api-openapi.yml
- filename: dbt-cloud-discovery-api-openapi.yml
  format: yaml
  label: dbt Cloud Discovery API
  slug: dbt-cloud-discovery-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dbt/refs/heads/main/openapi/dbt-cloud-discovery-api-openapi.yml
- filename: dbt-cloud-semantic-layer-api-openapi.yml
  format: yaml
  label: dbt Cloud Semantic Layer API
  slug: dbt-cloud-semantic-layer-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dbt/refs/heads/main/openapi/dbt-cloud-semantic-layer-api-openapi.yml
categories:
- dbt
description: Spectral linting rules defining API design standards and conventions for dbt.
layout: rules
name: dbt API Rules
provider_name: dbt
provider_slug: dbt
rule_count: 5
rules:
- description: API info should include a dbt Labs contact.
  given: $.info
  name: dbt-info-contact
  severity: warn
- description: Servers should reference cloud.getdbt.com.
  given: $.servers[*].url
  name: dbt-cloud-base-url
  severity: warn
- description: API should declare a bearer token security scheme.
  given: $.components.securitySchemes
  name: dbt-bearer-auth
  severity: error
- description: Resource paths should be scoped under /accounts/{accountId}.
  given: $.paths
  name: dbt-account-scoped-paths
  severity: warn
- description: Operations should be tagged Accounts, Projects, Jobs, Runs, or Environments.
  given: $.paths[*][*]
  name: dbt-operation-tags
  severity: warn
rules_file: rules/dbt-cloud-administrative-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/dbt/refs/heads/main/rules/dbt-cloud-administrative-api-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 4
slug: dbt-cloud-administrative-api-rules
source_filename: dbt-cloud-administrative-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  dbt-info-contact:\n    description: API info should include a dbt Labs contact.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  dbt-cloud-base-url:\n    description: Servers should reference cloud.getdbt.com.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"cloud\\\\.getdbt\\\\.com\"\n  dbt-bearer-auth:\n    description: API should declare a bearer token security scheme.\n    given: $.components.securitySchemes\n    severity: error\n    then:\n      field: bearerAuth\n      function: truthy\n  dbt-account-scoped-paths:\n    description: Resource paths should be scoped under /accounts/{accountId}.\n    given: $.paths\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/accounts/\"\n  dbt-operation-tags:\n    description: Operations should be tagged Accounts, Projects,\
  \ Jobs, Runs, or Environments.\n    given: $.paths[*][*]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/dbt/refs/heads/main/rules/dbt-cloud-administrative-api-rules.yml
tags:
- Analytics Engineering
- Data
- ELT
- Metrics
- Projects
- SQL
- Transformation
- Spectral
- Linting
- API Governance
---
