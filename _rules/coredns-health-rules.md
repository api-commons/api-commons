---
api_specs:
- filename: coredns-health-openapi.yml
  format: yaml
  label: CoreDNS Health API
  slug: coredns-health-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/coredns/refs/heads/main/openapi/coredns-health-openapi.yml
- filename: coredns-metrics-openapi.yml
  format: yaml
  label: CoreDNS Metrics API
  slug: coredns-metrics-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/coredns/refs/heads/main/openapi/coredns-metrics-openapi.yml
categories:
- coredns
description: Spectral linting rules defining API design standards and conventions for CoreDNS.
layout: rules
name: CoreDNS API Rules
provider_name: CoreDNS
provider_slug: coredns
rule_count: 8
rules:
- description: API info object should include Apache 2.0 license.
  given: $.info.license
  name: coredns-health-info-license
  severity: error
- description: Servers should reference the localhost CoreDNS health endpoint.
  given: $.servers[*].url
  name: coredns-health-server-localhost
  severity: warn
- description: API must define /health and /ready paths.
  given: $.paths
  name: coredns-health-paths
  severity: error
- description: Health and readiness endpoints must only support GET.
  given: $.paths['/health','/ready']
  name: coredns-health-get-only
  severity: error
- description: Health and readiness 200 responses should return text/plain.
  given: $.paths['/health','/ready'].get.responses.200.content
  name: coredns-health-text-plain-response
  severity: warn
- description: Health and readiness endpoints should document 503 responses.
  given: $.paths['/health','/ready'].get.responses
  name: coredns-health-503-response
  severity: error
- description: Operations must define an operationId.
  given: $.paths.*.get
  name: coredns-health-operation-id
  severity: error
- description: Operations must define tags.
  given: $.paths.*.get
  name: coredns-health-tags
  severity: error
rules_file: rules/coredns-health-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/coredns/refs/heads/main/rules/coredns-health-rules.yml
severity_counts:
  error: 6
  hint: 0
  info: 0
  warn: 2
slug: coredns-health-rules
source_filename: coredns-health-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [\"spectral:oas\"]\ndocumentationUrl: https://coredns.io/plugins/health/\nrules:\n  coredns-health-info-license:\n    description: API info object should include Apache 2.0 license.\n    given: \"$.info.license\"\n    severity: error\n    then:\n      field: name\n      function: pattern\n      functionOptions:\n        match: \"Apache\"\n  coredns-health-server-localhost:\n    description: Servers should reference the localhost CoreDNS health endpoint.\n    given: \"$.servers[*].url\"\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"localhost\"\n  coredns-health-paths:\n    description: API must define /health and /ready paths.\n    given: \"$.paths\"\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - /health\n            - /ready\n  coredns-health-get-only:\n    description: Health and readiness endpoints must\
  \ only support GET.\n    given: \"$.paths['/health','/ready']\"\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            get:\n              type: object\n          additionalProperties: false\n  coredns-health-text-plain-response:\n    description: Health and readiness 200 responses should return text/plain.\n    given: \"$.paths['/health','/ready'].get.responses.200.content\"\n    severity: warn\n    then:\n      field: text/plain\n      function: truthy\n  coredns-health-503-response:\n    description: Health and readiness endpoints should document 503 responses.\n    given: \"$.paths['/health','/ready'].get.responses\"\n    severity: error\n    then:\n      field: '503'\n      function: truthy\n  coredns-health-operation-id:\n    description: Operations must define an operationId.\n    given: \"$.paths.*.get\"\n    severity: error\n    then:\n      field: operationId\n      function:\
  \ truthy\n  coredns-health-tags:\n    description: Operations must define tags.\n    given: \"$.paths.*.get\"\n    severity: error\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/coredns/refs/heads/main/rules/coredns-health-rules.yml
tags:
- Apache 2.0
- Cloud Native
- CNCF
- DNS
- Go
- Graduated
- Kubernetes
- Networking
- Open Source
- Plugins
- Prometheus
- Service Discovery
- Spectral
- Linting
- API Governance
---
