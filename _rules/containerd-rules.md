---
api_specs:
- filename: containerd-metrics-openapi.yml
  format: yaml
  label: Containerd Metrics API
  slug: containerd-metrics-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/containerd/refs/heads/main/openapi/containerd-metrics-openapi.yml
categories:
- containerd
description: Spectral linting rules defining API design standards and conventions for Containerd.
layout: rules
name: Containerd API Rules
provider_name: Containerd
provider_slug: containerd
rule_count: 7
rules:
- description: API contact information must be present.
  given: $.info
  name: containerd-info-contact
  severity: error
- description: containerd APIs must declare an Apache 2.0 license.
  given: $.info.license
  name: containerd-info-license
  severity: error
- description: Metrics endpoints typically bind to localhost; warn if the spec advertises a non-loopback host.
  given: $.servers[*].url
  name: containerd-server-localhost
  severity: info
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: containerd-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: containerd-operation-tags
  severity: warn
- description: Metrics responses must declare a Prometheus text-format content type.
  given: $.paths[*].get.responses['200'].content
  name: containerd-prometheus-content-type
  severity: warn
- description: The containerd metrics endpoint must not declare mutating operations.
  given: $.paths[*]
  name: containerd-no-mutations
  severity: error
rules_file: rules/containerd-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/containerd/refs/heads/main/rules/containerd-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 2
slug: containerd-rules
source_filename: containerd-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for containerd HTTP-style APIs (the metrics\n# plugin endpoint). Tuned to a localhost-only Prometheus scrape target\n# served from the containerd process, with no auth and a single GET\n# /v1/metrics path returning Prometheus text format.\nrules:\n  containerd-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  containerd-info-license:\n    description: containerd APIs must declare an Apache 2.0 license.\n    severity: error\n    given: \"$.info.license\"\n    then:\n      field: name\n      function: pattern\n      functionOptions:\n        match: \"Apache\"\n\n  containerd-server-localhost:\n    description: Metrics endpoints typically bind to localhost; warn if the spec advertises a non-loopback host.\n    severity: info\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n \
  \     functionOptions:\n        match: \"(localhost|127\\\\.0\\\\.0\\\\.1|0\\\\.0\\\\.0\\\\.0)\"\n\n  containerd-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  containerd-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  containerd-prometheus-content-type:\n    description: Metrics responses must declare a Prometheus text-format content type.\n    severity: warn\n    given: \"$.paths[*].get.responses['200'].content\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"text/plain\"\
  ]\n            - required: [\"application/openmetrics-text\"]\n            - required: [\"text/plain; version=0.0.4\"]\n\n  containerd-no-mutations:\n    description: The containerd metrics endpoint must not declare mutating operations.\n    severity: error\n    given: \"$.paths[*]\"\n    then:\n      function: falsy\n      field: post\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/containerd/refs/heads/main/rules/containerd-rules.yml
tags:
- Cloud Native
- Container Runtime
- CRI
- Docker
- gRPC
- Kubernetes
- OCI
- Spectral
- Linting
- API Governance
---
