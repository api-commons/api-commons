---
api_specs:
- filename: consul-connect-openapi.yml
  format: yaml
  label: Consul Connect HTTP API
  slug: consul-connect-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/consul-connect/refs/heads/main/openapi/consul-connect-openapi.yml
categories:
- consul
description: Spectral linting rules defining API design standards and conventions for Consul Connect.
layout: rules
name: Consul Connect API Rules
provider_name: Consul Connect
provider_slug: consul-connect
rule_count: 6
rules:
- description: Connect OpenAPI info.title must reference Consul Connect
  given: $.info.title
  name: consul-connect-info-title
  severity: error
- description: At least one server URL must be defined
  given: $.servers
  name: consul-connect-server-defined
  severity: error
- description: All paths should sit under the /v1 prefix at the server URL level
  given: $.servers[*].url
  name: consul-connect-v1-prefix
  severity: warn
- description: Connect operations must be tagged with Intentions or CA
  given: $.paths.*[get,put,post,delete,patch].tags[*]
  name: consul-connect-tag-required
  severity: warn
- description: Every operation must define an operationId using camelCase
  given: $.paths.*[get,put,post,delete,patch].operationId
  name: consul-connect-operation-id-camelcase
  severity: error
- description: A ConsulToken security scheme should be declared
  given: $.components.securitySchemes
  name: consul-connect-token-security
  severity: warn
rules_file: rules/consul-connect-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/consul-connect/refs/heads/main/rules/consul-connect-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 3
slug: consul-connect-rules
source_filename: consul-connect-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - \"spectral:oas\"\ndocumentationUrl: https://developer.hashicorp.com/consul/api-docs/connect\nrules:\n  consul-connect-info-title:\n    description: Connect OpenAPI info.title must reference Consul Connect\n    severity: error\n    given: \"$.info.title\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"(?i)Consul\\\\s+Connect\"\n  consul-connect-server-defined:\n    description: At least one server URL must be defined\n    severity: error\n    given: \"$.servers\"\n    then:\n      function: length\n      functionOptions:\n        min: 1\n  consul-connect-v1-prefix:\n    description: All paths should sit under the /v1 prefix at the server URL level\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/v1$\"\n  consul-connect-tag-required:\n    description: Connect operations must be tagged with Intentions or CA\n    severity: warn\n    given: \"$.paths.*[get,put,post,delete,patch].tags[*]\"\
  \n    then:\n      function: enumeration\n      functionOptions:\n        values:\n          - Intentions\n          - CA\n  consul-connect-operation-id-camelcase:\n    description: Every operation must define an operationId using camelCase\n    severity: error\n    given: \"$.paths.*[get,put,post,delete,patch].operationId\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^[a-z][a-zA-Z0-9]+$\"\n  consul-connect-token-security:\n    description: A ConsulToken security scheme should be declared\n    severity: warn\n    given: \"$.components.securitySchemes\"\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/consul-connect/refs/heads/main/rules/consul-connect-rules.yml
tags:
- Consul
- Envoy
- HashiCorp
- Intentions
- Kubernetes
- mTLS
- Service Mesh
- Sidecar
- Zero Trust
- Spectral
- Linting
- API Governance
---
