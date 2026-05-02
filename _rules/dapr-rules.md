---
api_specs:
- filename: dapr-state-management-openapi.yml
  format: yaml
  label: Dapr State Management API
  slug: state-management
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dapr/refs/heads/main/openapi/dapr-state-management-openapi.yml
- filename: dapr-pubsub-openapi.yml
  format: yaml
  label: Dapr Pub/Sub API
  slug: pubsub
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dapr/refs/heads/main/openapi/dapr-pubsub-openapi.yml
- filename: dapr-service-invocation-openapi.yml
  format: yaml
  label: Dapr Service Invocation API
  slug: service-invocation
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dapr/refs/heads/main/openapi/dapr-service-invocation-openapi.yml
- filename: dapr-bindings-openapi.yml
  format: yaml
  label: Dapr Bindings API
  slug: bindings
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dapr/refs/heads/main/openapi/dapr-bindings-openapi.yml
- filename: dapr-secrets-openapi.yml
  format: yaml
  label: Dapr Secrets API
  slug: secrets
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dapr/refs/heads/main/openapi/dapr-secrets-openapi.yml
- filename: dapr-actors-openapi.yml
  format: yaml
  label: Dapr Actors API
  slug: actors
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dapr/refs/heads/main/openapi/dapr-actors-openapi.yml
- filename: dapr-workflow-openapi.yml
  format: yaml
  label: Dapr Workflow API
  slug: workflow
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dapr/refs/heads/main/openapi/dapr-workflow-openapi.yml
- filename: dapr-configuration-openapi.yml
  format: yaml
  label: Dapr Configuration API
  slug: configuration
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dapr/refs/heads/main/openapi/dapr-configuration-openapi.yml
- filename: dapr-distributed-lock-openapi.yml
  format: yaml
  label: Dapr Distributed Lock API
  slug: distributed-lock
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dapr/refs/heads/main/openapi/dapr-distributed-lock-openapi.yml
- filename: dapr-cryptography-openapi.yml
  format: yaml
  label: Dapr Cryptography API
  slug: cryptography
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dapr/refs/heads/main/openapi/dapr-cryptography-openapi.yml
- filename: dapr-jobs-openapi.yml
  format: yaml
  label: Dapr Jobs API
  slug: jobs
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dapr/refs/heads/main/openapi/dapr-jobs-openapi.yml
- filename: dapr-health-openapi.yml
  format: yaml
  label: Dapr Health API
  slug: health
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dapr/refs/heads/main/openapi/dapr-health-openapi.yml
- filename: dapr-metadata-openapi.yml
  format: yaml
  label: Dapr Metadata API
  slug: metadata
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dapr/refs/heads/main/openapi/dapr-metadata-openapi.yml
categories:
- dapr
description: Spectral linting rules defining API design standards and conventions for Dapr.
layout: rules
name: Dapr API Rules
provider_name: Dapr
provider_slug: dapr
rule_count: 5
rules:
- description: API info should provide a contact for the Dapr project.
  given: $.info
  name: dapr-info-contact
  severity: warn
- description: Servers should use the /v1.0 path prefix used by Dapr building blocks.
  given: $.servers[*].url
  name: dapr-server-prefix
  severity: warn
- description: State, secrets, and configuration paths must be parameterised by storeName.
  given: $.paths
  name: dapr-store-name-path-param
  severity: warn
- description: Every operation must be tagged with its building block.
  given: $.paths[*][*]
  name: dapr-operation-tags
  severity: error
- description: Pub/sub publish endpoints should accept application/cloudevents+json.
  given: $.paths[*].post.requestBody.content
  name: dapr-cloudevent-content-type
  severity: warn
rules_file: rules/dapr-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/dapr/refs/heads/main/rules/dapr-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 4
slug: dapr-rules
source_filename: dapr-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  dapr-info-contact:\n    description: API info should provide a contact for the Dapr project.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  dapr-server-prefix:\n    description: Servers should use the /v1.0 path prefix used by Dapr building blocks.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/v1\\\\.0\"\n  dapr-store-name-path-param:\n    description: State, secrets, and configuration paths must be parameterised by storeName.\n    given: $.paths\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"\\\\{storeName\\\\}|\\\\{secretStoreName\\\\}|\\\\{pubsubname\\\\}|\\\\{name\\\\}\"\n  dapr-operation-tags:\n    description: Every operation must be tagged with its building block.\n    given: $.paths[*][*]\n    severity: error\n    then:\n      field: tags\n      function:\
  \ truthy\n  dapr-cloudevent-content-type:\n    description: Pub/sub publish endpoints should accept application/cloudevents+json.\n    given: $.paths[*].post.requestBody.content\n    severity: warn\n    then:\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/dapr/refs/heads/main/rules/dapr-rules.yml
tags:
- Distributed Systems
- Microservices
- Platform
- Pub/Sub
- State Management
- Workflows
- Spectral
- Linting
- API Governance
---
