---
api_specs:
- filename: v1
  format: yaml
  label: ClickHouse Cloud API
  slug: clickhouse-cloud-api
  spec_type: OpenAPI
  url: https://api.clickhouse.cloud/v1
categories:
- clickhouse
description: Spectral linting rules defining API design standards and conventions for ClickHouse.
layout: rules
name: ClickHouse API Rules
provider_name: ClickHouse
provider_slug: clickhouse
rule_count: 9
rules:
- description: API contact information must be present.
  given: $.info
  name: clickhouse-info-contact
  severity: error
- description: API license must be declared.
  given: $.info
  name: clickhouse-info-license
  severity: warn
- description: All server URLs must use HTTPS for the Cloud control plane.
  given: $.servers[?(@.url && @.url.indexOf('clickhouse.cloud') > -1)].url
  name: clickhouse-server-https
  severity: error
- description: ClickHouse Cloud paths must be versioned (/v{N}).
  given: $.paths
  name: clickhouse-cloud-versioned
  severity: warn
- description: A security scheme (apiKey) must be declared for Cloud APIs.
  given: $.components.securitySchemes
  name: clickhouse-auth-required
  severity: error
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: clickhouse-operation-id
  severity: error
- description: Every operation must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: clickhouse-operation-tags
  severity: warn
- description: Every operation must include a short summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: clickhouse-operation-summary
  severity: warn
- description: Mutating operations should declare 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: clickhouse-error-responses
  severity: warn
rules_file: rules/clickhouse-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/clickhouse/refs/heads/main/rules/clickhouse-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 5
slug: clickhouse-rules
source_filename: clickhouse-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for ClickHouse Cloud and HTTP interface APIs.\nrules:\n  clickhouse-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  clickhouse-info-license:\n    description: API license must be declared.\n    severity: warn\n    given: \"$.info\"\n    then:\n      field: license\n      function: truthy\n\n  clickhouse-server-https:\n    description: All server URLs must use HTTPS for the Cloud control plane.\n    severity: error\n    given: \"$.servers[?(@.url && @.url.indexOf('clickhouse.cloud') > -1)].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^https://\"\n\n  clickhouse-cloud-versioned:\n    description: ClickHouse Cloud paths must be versioned (/v{N}).\n    severity: warn\n    given: \"$.paths\"\n    then:\n      function: schema\n      functionOptions:\n      \
  \  schema:\n          type: object\n          patternProperties:\n            \"^/v\\\\d+/.*\": {}\n          additionalProperties: true\n\n  clickhouse-auth-required:\n    description: A security scheme (apiKey) must be declared for Cloud APIs.\n    severity: error\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n\n  clickhouse-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  clickhouse-operation-tags:\n    description: Every operation must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  clickhouse-operation-summary:\n    description: Every operation must include a short summary.\n    severity:\
  \ warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: summary\n      function: truthy\n\n  clickhouse-error-responses:\n    description: Mutating operations should declare 4xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"401\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/clickhouse/refs/heads/main/rules/clickhouse-rules.yml
tags:
- Analytics
- Cloud Database
- Column-Oriented
- Database
- OLAP
- Open Source
- Real-Time
- SQL
- Spectral
- Linting
- API Governance
---
