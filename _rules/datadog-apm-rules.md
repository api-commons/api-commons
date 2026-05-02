---
api_specs:
- filename: datadog-apm-api.yml
  format: yaml
  label: Datadog APM API
  slug: datadog-apm-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/datadog-apm/refs/heads/main/openapi/datadog-apm-api.yml
categories:
- datadog
description: Spectral linting rules defining API design standards and conventions for Datadog APM.
layout: rules
name: Datadog APM API Rules
provider_name: Datadog APM
provider_slug: datadog-apm
rule_count: 5
rules:
- description: API info should provide a contact for Datadog support.
  given: $.info
  name: datadog-apm-info-contact
  severity: warn
- description: Servers should target one of the Datadog regional sites.
  given: $.servers[*].url
  name: datadog-apm-server-region
  severity: warn
- description: Operation paths should be versioned under /api/v1 or /api/v2.
  given: $.paths
  name: datadog-apm-api-version-prefix
  severity: warn
- description: Every operation must declare at least one tag.
  given: $.paths[*][*]
  name: datadog-apm-operation-tags
  severity: error
- description: Operations should require both API key and application key auth.
  given: $.security
  name: datadog-apm-security-keys
  severity: warn
rules_file: rules/datadog-apm-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/datadog-apm/refs/heads/main/rules/datadog-apm-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 4
slug: datadog-apm-rules
source_filename: datadog-apm-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  datadog-apm-info-contact:\n    description: API info should provide a contact for Datadog support.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  datadog-apm-server-region:\n    description: Servers should target one of the Datadog regional sites.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"datadoghq\\\\.(com|eu)|datadoghq\\\\.com\"\n  datadog-apm-api-version-prefix:\n    description: Operation paths should be versioned under /api/v1 or /api/v2.\n    given: $.paths\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/api/v[12]\"\n  datadog-apm-operation-tags:\n    description: Every operation must declare at least one tag.\n    given: $.paths[*][*]\n    severity: error\n    then:\n      field: tags\n      function: truthy\n  datadog-apm-security-keys:\n    description:\
  \ Operations should require both API key and application key auth.\n    given: $.security\n    severity: warn\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/datadog-apm/refs/heads/main/rules/datadog-apm-rules.yml
tags:
- APM
- Distributed Tracing
- Microservices
- Observability
- Performance Monitoring
- Spectral
- Linting
- API Governance
---
