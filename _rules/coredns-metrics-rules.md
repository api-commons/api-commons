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
- description: API info object should declare Apache 2.0.
  given: $.info.license
  name: coredns-metrics-info-license
  severity: error
- description: Servers should reference port 9153 (default Prometheus metrics port).
  given: $.servers[*].url
  name: coredns-metrics-port-9153
  severity: warn
- description: API must define the /metrics path.
  given: $.paths
  name: coredns-metrics-path
  severity: error
- description: The /metrics endpoint must only support GET.
  given: $.paths['/metrics']
  name: coredns-metrics-get-only
  severity: error
- description: 200 response should return text/plain Prometheus exposition format.
  given: $.paths['/metrics'].get.responses.200.content
  name: coredns-metrics-prometheus-response
  severity: warn
- description: Operations must define an operationId.
  given: $.paths.*.get
  name: coredns-metrics-operation-id
  severity: error
- description: Operations must define tags.
  given: $.paths.*.get
  name: coredns-metrics-tags
  severity: error
- description: Metrics endpoint typically does not require authentication; consider documenting this.
  given: $.paths['/metrics'].get
  name: coredns-metrics-no-auth
  severity: info
rules_file: rules/coredns-metrics-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/coredns/refs/heads/main/rules/coredns-metrics-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 1
  warn: 2
slug: coredns-metrics-rules
source_filename: coredns-metrics-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [\"spectral:oas\"]\ndocumentationUrl: https://coredns.io/plugins/metrics/\nrules:\n  coredns-metrics-info-license:\n    description: API info object should declare Apache 2.0.\n    given: \"$.info.license\"\n    severity: error\n    then:\n      field: name\n      function: pattern\n      functionOptions:\n        match: \"Apache\"\n  coredns-metrics-port-9153:\n    description: Servers should reference port 9153 (default Prometheus metrics port).\n    given: \"$.servers[*].url\"\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \":9153\"\n  coredns-metrics-path:\n    description: API must define the /metrics path.\n    given: \"$.paths\"\n    severity: error\n    then:\n      field: /metrics\n      function: truthy\n  coredns-metrics-get-only:\n    description: The /metrics endpoint must only support GET.\n    given: \"$.paths['/metrics']\"\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n\
  \        schema:\n          type: object\n          properties:\n            get:\n              type: object\n          additionalProperties: false\n  coredns-metrics-prometheus-response:\n    description: 200 response should return text/plain Prometheus exposition format.\n    given: \"$.paths['/metrics'].get.responses.200.content\"\n    severity: warn\n    then:\n      field: text/plain\n      function: truthy\n  coredns-metrics-operation-id:\n    description: Operations must define an operationId.\n    given: \"$.paths.*.get\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n  coredns-metrics-tags:\n    description: Operations must define tags.\n    given: \"$.paths.*.get\"\n    severity: error\n    then:\n      field: tags\n      function: truthy\n  coredns-metrics-no-auth:\n    description: Metrics endpoint typically does not require authentication; consider documenting this.\n    given: \"$.paths['/metrics'].get\"\n    severity: info\n    then:\n\
  \      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/coredns/refs/heads/main/rules/coredns-metrics-rules.yml
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
