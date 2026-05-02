---
api_specs:
- filename: contour-httpproxy-openapi.yml
  format: yaml
  label: Contour HTTPProxy API
  slug: contour-httpproxy-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/contour/refs/heads/main/openapi/contour-httpproxy-openapi.yml
- filename: contour-gateway-openapi.yml
  format: yaml
  label: Contour Gateway API
  slug: contour-gateway-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/contour/refs/heads/main/openapi/contour-gateway-openapi.yml
categories:
- contour
description: Spectral linting rules defining API design standards and conventions for Contour.
layout: rules
name: Contour API Rules
provider_name: Contour
provider_slug: contour
rule_count: 5
rules:
- description: Gateway OpenAPI info.title must reference Contour Gateway
  given: $.info.title
  name: contour-gateway-info-title
  severity: error
- description: At least one server URL must be defined for the Kubernetes API
  given: $.servers
  name: contour-gateway-server-defined
  severity: error
- description: Tags must declare GatewayClass, Gateway, HTTPRoute, or TLSRoute scope
  given: $.tags[*].name
  name: contour-gateway-tag-required
  severity: warn
- description: Every operation must define an operationId using camelCase
  given: $.paths.*[get,put,post,delete,patch].operationId
  name: contour-gateway-operation-id-camelcase
  severity: error
- description: Gateway API paths must live under /apis/gateway.networking.k8s.io
  given: $.paths
  name: contour-gateway-api-group-prefix
  severity: error
rules_file: rules/contour-gateway-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/contour/refs/heads/main/rules/contour-gateway-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 1
slug: contour-gateway-rules
source_filename: contour-gateway-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - \"spectral:oas\"\ndocumentationUrl: https://projectcontour.io/docs/main/config/gateway-api/\nrules:\n  contour-gateway-info-title:\n    description: Gateway OpenAPI info.title must reference Contour Gateway\n    severity: error\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(?i)Contour\\\\s+Gateway\"\n  contour-gateway-server-defined:\n    description: At least one server URL must be defined for the Kubernetes API\n    severity: error\n    given: \"$.servers\"\n    then:\n      function: length\n      functionOptions:\n        min: 1\n  contour-gateway-tag-required:\n    description: Tags must declare GatewayClass, Gateway, HTTPRoute, or TLSRoute scope\n    severity: warn\n    given: \"$.tags[*].name\"\n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - GatewayClass\n          - Gateway\n          - HTTPRoute\n          - TLSRoute\n          - GRPCRoute\n    \
  \      - TCPRoute\n          - UDPRoute\n  contour-gateway-operation-id-camelcase:\n    description: Every operation must define an operationId using camelCase\n    severity: error\n    given: \"$.paths.*[get,put,post,delete,patch].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n  contour-gateway-api-group-prefix:\n    description: Gateway API paths must live under /apis/gateway.networking.k8s.io\n    severity: error\n    given: \"$.paths\"\n    then:\n      field: \"@key\"\n      function: pattern\n      functionOptions:\n        match: \"^/apis/gateway\\\\.networking\\\\.k8s\\\\.io/\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/contour/refs/heads/main/rules/contour-gateway-rules.yml
tags:
- Envoy
- Ingress Controller
- Kubernetes
- Networking
- Proxy
- Spectral
- Linting
- API Governance
---
