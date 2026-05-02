---
api_specs:
- filename: crossplane-kubernetes-api-openapi.yml
  format: yaml
  label: Crossplane Kubernetes API
  slug: crossplane-kubernetes-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/crossplane/refs/heads/main/openapi/crossplane-kubernetes-api-openapi.yml
categories:
- crossplane
description: Spectral linting rules defining API design standards and conventions for Crossplane.
layout: rules
name: Crossplane API Rules
provider_name: Crossplane
provider_slug: crossplane
rule_count: 7
rules:
- description: API info object should reference Crossplane community contact.
  given: $.info.contact
  name: crossplane-info-contact
  severity: error
- description: Server URL should reference the Kubernetes API server.
  given: $.servers[*].url
  name: crossplane-server-kubernetes
  severity: warn
- description: API must define core Crossplane API extension paths.
  given: $.paths
  name: crossplane-required-paths
  severity: error
- description: API must define package management paths under pkg.crossplane.io.
  given: $.paths
  name: crossplane-pkg-paths
  severity: error
- description: All operations must define an operationId.
  given: $.paths.*.*
  name: crossplane-operation-id
  severity: error
- description: Operation IDs should start with a verb (list, get, create, replace, delete, patch).
  given: $.paths.*.*.operationId
  name: crossplane-operation-id-prefix
  severity: warn
- description: All operations must define tags.
  given: $.paths.*.*
  name: crossplane-tags
  severity: error
rules_file: rules/crossplane-kubernetes-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/crossplane/refs/heads/main/rules/crossplane-kubernetes-api-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 0
  warn: 2
slug: crossplane-kubernetes-api-rules
source_filename: crossplane-kubernetes-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends: [\"spectral:oas\"]\ndocumentationUrl: https://docs.crossplane.io/latest/api/\nrules:\n  crossplane-info-contact:\n    description: API info object should reference Crossplane community contact.\n    given: \"$.info.contact\"\n    severity: error\n    then:\n      field: url\n      function: pattern\n      functionOptions:\n        match: \"(crossplane|slack)\"\n  crossplane-server-kubernetes:\n    description: Server URL should reference the Kubernetes API server.\n    given: \"$.servers[*].url\"\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"kubernetes\"\n  crossplane-required-paths:\n    description: API must define core Crossplane API extension paths.\n    given: \"$.paths\"\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - /apis/apiextensions.crossplane.io/v1/compositions\n            - /apis/apiextensions.crossplane.io/v1/compositeresourcedefinitions\n\
  \  crossplane-pkg-paths:\n    description: API must define package management paths under pkg.crossplane.io.\n    given: \"$.paths\"\n    severity: error\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          required:\n            - /apis/pkg.crossplane.io/v1/providers\n  crossplane-operation-id:\n    description: All operations must define an operationId.\n    given: \"$.paths.*.*\"\n    severity: error\n    then:\n      field: operationId\n      function: truthy\n  crossplane-operation-id-prefix:\n    description: Operation IDs should start with a verb (list, get, create, replace, delete, patch).\n    given: \"$.paths.*.*.operationId\"\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^(list|get|create|replace|delete|patch)\"\n  crossplane-tags:\n    description: All operations must define tags.\n    given: \"$.paths.*.*\"\n    severity: error\n    then:\n      field: tags\n     \
  \ function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/crossplane/refs/heads/main/rules/crossplane-kubernetes-api-rules.yml
tags:
- Apache 2.0
- CNCF
- Cloud Native
- Composition
- Control Plane
- Custom Resource Definitions
- Graduated
- Infrastructure as Code
- Kubernetes
- Multi-Cloud
- Open Source
- Platform Engineering
- Providers
- Spectral
- Linting
- API Governance
---
