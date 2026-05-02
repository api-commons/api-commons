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
- description: HTTPProxy OpenAPI info.title must reference Contour HTTPProxy
  given: $.info.title
  name: contour-httpproxy-info-title
  severity: error
- description: At least one server URL must be defined for the Kubernetes API
  given: $.servers
  name: contour-httpproxy-server-defined
  severity: error
- description: The HTTPProxy or TLSCertificateDelegation tags must be declared
  given: $.tags[*].name
  name: contour-httpproxy-tag-required
  severity: warn
- description: Every operation must define an operationId using camelCase
  given: $.paths.*[get,put,post,delete,patch].operationId
  name: contour-httpproxy-operation-id-camelcase
  severity: error
- description: Namespaced HTTPProxy paths must include the namespace parameter
  given: $.paths[?(@property =~ /httpproxies/)]
  name: contour-httpproxy-namespace-path
  severity: warn
rules_file: rules/contour-httpproxy-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/contour/refs/heads/main/rules/contour-httpproxy-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 2
slug: contour-httpproxy-rules
source_filename: contour-httpproxy-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - \"spectral:oas\"\ndocumentationUrl: https://projectcontour.io/docs/main/config/api/\nrules:\n  contour-httpproxy-info-title:\n    description: HTTPProxy OpenAPI info.title must reference Contour HTTPProxy\n    severity: error\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(?i)Contour\\\\s+HTTPProxy\"\n  contour-httpproxy-server-defined:\n    description: At least one server URL must be defined for the Kubernetes API\n    severity: error\n    given: \"$.servers\"\n    then:\n      function: length\n      functionOptions:\n        min: 1\n  contour-httpproxy-tag-required:\n    description: The HTTPProxy or TLSCertificateDelegation tags must be declared\n    severity: warn\n    given: \"$.tags[*].name\"\n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - HTTPProxy\n          - TLSCertificateDelegation\n  contour-httpproxy-operation-id-camelcase:\n    description:\
  \ Every operation must define an operationId using camelCase\n    severity: error\n    given: \"$.paths.*[get,put,post,delete,patch].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n  contour-httpproxy-namespace-path:\n    description: Namespaced HTTPProxy paths must include the namespace parameter\n    severity: warn\n    given: \"$.paths[?(@property =~ /httpproxies/)]\"\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/contour/refs/heads/main/rules/contour-httpproxy-rules.yml
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
