---
api_specs:
- filename: consul-http-api.yml
  format: yaml
  label: Consul HTTP API
  slug: http-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/consul/refs/heads/main/openapi/consul-http-api.yml
categories:
- consul
description: Spectral linting rules defining API design standards and conventions for HashiCorp Consul.
layout: rules
name: HashiCorp Consul API Rules
provider_name: HashiCorp Consul
provider_slug: consul
rule_count: 8
rules:
- description: API contact information must be present.
  given: $.info
  name: consul-info-contact
  severity: error
- description: Server URLs must include /v1 base path.
  given: $.servers[*].url
  name: consul-server-base-path
  severity: warn
- description: A Consul token security scheme (apiKey via X-Consul-Token) must be defined.
  given: $.components.securitySchemes[*]
  name: consul-token-security
  severity: error
- description: Every operation must declare a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: consul-operation-id
  severity: error
- description: Operations must declare at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: consul-operation-tags
  severity: warn
- description: Operations that target a specific datacenter should accept a `dc` query parameter.
  given: $.paths[?(@property.match(/(catalog|health|kv|acl|connect|config)/))].get
  name: consul-dc-parameter
  severity: info
- description: Mutating operations should declare 4xx/5xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: consul-error-responses
  severity: warn
- description: List endpoints should support blocking queries via an `index` parameter.
  given: $.paths[?(@property.match(/(catalog\/services|catalog\/nodes|health\/service|kv)/))].get
  name: consul-blocking-query-index
  severity: info
rules_file: rules/consul-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/consul/refs/heads/main/rules/consul-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 2
  warn: 3
slug: consul-rules
source_filename: consul-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\n\n# Spectral linting rules for HashiCorp Consul HTTP APIs.\n# Tuned to /v1 base path, ConsulToken (X-Consul-Token) auth, datacenter\n# query parameters, and PascalCase JSON payloads.\nrules:\n  consul-info-contact:\n    description: API contact information must be present.\n    severity: error\n    given: \"$.info\"\n    then:\n      field: contact\n      function: truthy\n\n  consul-server-base-path:\n    description: Server URLs must include /v1 base path.\n    severity: warn\n    given: \"$.servers[*].url\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/v1\"\n\n  consul-token-security:\n    description: A Consul token security scheme (apiKey via X-Consul-Token) must be defined.\n    severity: error\n    given: \"$.components.securitySchemes[*]\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          properties:\n            type:\n              enum: [\"apiKey\"\
  , \"http\"]\n\n  consul-operation-id:\n    description: Every operation must declare a unique operationId.\n    severity: error\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: operationId\n      function: truthy\n\n  consul-operation-tags:\n    description: Operations must declare at least one tag.\n    severity: warn\n    given: \"$.paths[*][get,post,put,patch,delete]\"\n    then:\n      field: tags\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          minItems: 1\n\n  consul-dc-parameter:\n    description: Operations that target a specific datacenter should accept a `dc` query parameter.\n    severity: info\n    given: \"$.paths[?(@property.match(/(catalog|health|kv|acl|connect|config)/))].get\"\n    then:\n      field: parameters\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            type: object\n            properties:\n              name:\n\
  \                enum: [\"dc\"]\n\n  consul-error-responses:\n    description: Mutating operations should declare 4xx/5xx error responses.\n    severity: warn\n    given: \"$.paths[*][post,put,patch,delete].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          anyOf:\n            - required: [\"400\"]\n            - required: [\"403\"]\n            - required: [\"404\"]\n            - required: [\"500\"]\n\n  consul-blocking-query-index:\n    description: List endpoints should support blocking queries via an `index` parameter.\n    severity: info\n    given: \"$.paths[?(@property.match(/(catalog\\\\/services|catalog\\\\/nodes|health\\\\/service|kv)/))].get\"\n    then:\n      field: parameters\n      function: schema\n      functionOptions:\n        schema:\n          type: array\n          contains:\n            type: object\n            properties:\n              name:\n                enum: [\"index\", \"wait\"]\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/consul/refs/heads/main/rules/consul-rules.yml
tags:
- ACL
- Configuration
- Health Checking
- Key/Value Store
- Multi-Datacenter
- Open Source
- Service Discovery
- Service Mesh
- Spectral
- Linting
- API Governance
---
