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
rule_count: 6
rules:
- description: API info object should declare the Apache 2.0 license.
  given: $.info.license
  name: cri-o-status-info-license
  severity: error
- description: Servers should reference localhost for the Unix-socket-served HTTP API.
  given: $.servers[*].url
  name: cri-o-status-server-localhost
  severity: warn
- description: API must define core informational paths /info and /config.
  given: $.paths
  name: cri-o-status-info-paths
  severity: error
- description: API must define lifecycle paths for pause and unpause by container ID.
  given: $.paths
  name: cri-o-status-lifecycle-paths
  severity: error
- description: Every operation must define an operationId.
  given: $.paths.*.*
  name: cri-o-status-operation-id
  severity: error
- description: Every operation must define tags.
  given: $.paths.*.*
  name: cri-o-status-tags
  severity: error
rules_file: rules/cri-o-status-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cri-o/refs/heads/main/rules/cri-o-status-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 0
  warn: 1
slug: cri-o-status-rules
source_filename: cri-o-status-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [\"spectral:oas\"]\ndocumentationUrl: https://github.com/cri-o/cri-o\nrules:\n  cri-o-status-info-license:\n    description: API info object should declare the Apache 2.0 license.\n    given: \"$.info.license\"\n    severity: error\n    then:\n      field: name\n      function: pattern\n      functionOptions:\n        match: \"Apache\"\n  cri-o-status-server-localhost:\n    description: Servers should reference localhost for the Unix-socket-served HTTP API.\n    given: \"$.servers[*].url\"\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"localhost\"\n  cri-o-status-info-paths:\n    description: API must define core informational paths /info and /config.\n    given: \"$.paths\"\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - /info\n            - /config\n  cri-o-status-lifecycle-paths:\n    description: API must\
  \ define lifecycle paths for pause and unpause by container ID.\n    given: \"$.paths\"\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - /pause/{id}\n            - /unpause/{id}\n  cri-o-status-operation-id:\n    description: Every operation must define an operationId.\n    given: \"$.paths.*.*\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n  cri-o-status-tags:\n    description: Every operation must define tags.\n    given: \"$.paths.*.*\"\n    severity: error\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/cri-o/refs/heads/main/rules/cri-o-status-rules.yml
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
