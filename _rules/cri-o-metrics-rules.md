---
api_specs:
- filename: cri-o-status-openapi.yml
  format: yaml
  label: CRI-O Status API
  slug: cri-o-status-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cri-o/refs/heads/main/openapi/cri-o-status-openapi.yml
- filename: cri-o-metrics-openapi.yml
  format: yaml
  label: CRI-O Metrics API
  slug: cri-o-metrics-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cri-o/refs/heads/main/openapi/cri-o-metrics-openapi.yml
categories:
- cri
description: Spectral linting rules defining API design standards and conventions for CRI-O.
layout: rules
name: CRI-O API Rules
provider_name: CRI-O
provider_slug: cri-o
rule_count: 7
rules:
- description: API info object should declare the Apache 2.0 license.
  given: $.info.license
  name: cri-o-metrics-info-license
  severity: error
- description: Server URL should reference the default metrics port 9090.
  given: $.servers[*].url
  name: cri-o-metrics-server-port
  severity: warn
- description: API must define the /metrics path.
  given: $.paths
  name: cri-o-metrics-paths
  severity: error
- description: Metrics endpoint must only support GET.
  given: $.paths['/metrics']
  name: cri-o-metrics-get-only
  severity: error
- description: Metrics 200 response must be text/plain (Prometheus exposition format).
  given: $.paths['/metrics'].get.responses.200.content
  name: cri-o-metrics-text-plain-response
  severity: error
- description: Operations must define an operationId.
  given: $.paths.*.get
  name: cri-o-metrics-operation-id
  severity: error
- description: Operations must define tags.
  given: $.paths.*.get
  name: cri-o-metrics-tags
  severity: error
rules_file: rules/cri-o-metrics-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cri-o/refs/heads/main/rules/cri-o-metrics-rules.yml
severity_counts:
  error: 6
  hint: 0
  info: 0
  warn: 1
slug: cri-o-metrics-rules
source_filename: cri-o-metrics-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [\"spectral:oas\"]\ndocumentationUrl: https://github.com/cri-o/cri-o/blob/main/docs/metrics.md\nrules:\n  cri-o-metrics-info-license:\n    description: API info object should declare the Apache 2.0 license.\n    given: \"$.info.license\"\n    severity: error\n    then:\n      field: name\n      function: pattern\n      functionOptions:\n        match: \"Apache\"\n  cri-o-metrics-server-port:\n    description: Server URL should reference the default metrics port 9090.\n    given: \"$.servers[*].url\"\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"9090\"\n  cri-o-metrics-paths:\n    description: API must define the /metrics path.\n    given: \"$.paths\"\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - /metrics\n  cri-o-metrics-get-only:\n    description: Metrics endpoint must only support GET.\n    given: \"$.paths['/metrics']\"\
  \n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            get:\n              type: object\n          additionalProperties: false\n  cri-o-metrics-text-plain-response:\n    description: Metrics 200 response must be text/plain (Prometheus exposition format).\n    given: \"$.paths['/metrics'].get.responses.200.content\"\n    severity: error\n    then:\n      field: text/plain\n      function: truthy\n  cri-o-metrics-operation-id:\n    description: Operations must define an operationId.\n    given: \"$.paths.*.get\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n  cri-o-metrics-tags:\n    description: Operations must define tags.\n    given: \"$.paths.*.get\"\n    severity: error\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cri-o/refs/heads/main/rules/cri-o-metrics-rules.yml
tags:
- Apache 2.0
- CNCF
- Cloud Native
- conmon
- Container Runtime
- Containers
- CRI
- Go
- Graduated
- Kubernetes
- OCI
- Open Source
- Prometheus
- runc
- Spectral
- Linting
- API Governance
---
