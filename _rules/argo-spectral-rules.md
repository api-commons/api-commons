---
api_specs:
- filename: argo-workflows-openapi.yml
  format: yaml
  label: Argo Workflows API
  slug: argo-workflows-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/argo/refs/heads/main/openapi/argo-workflows-openapi.yml
- filename: argo-cd-openapi.yml
  format: yaml
  label: Argo CD API
  slug: argo-cd-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/argo/refs/heads/main/openapi/argo-cd-openapi.yml
- filename: argo-events-asyncapi.yml
  format: yaml
  label: Argo Events API
  slug: argo-events-api
  spec_type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/argo/refs/heads/main/asyncapi/argo-events-asyncapi.yml
categories:
- info
- 'no'
- operation
- paths
- response
description: Spectral linting rules defining API design standards and conventions for Argo.
layout: rules
name: Argo API Rules
provider_name: Argo
provider_slug: argo
rule_count: 9
rules:
- description: API title must be present
  given: $.info
  name: info-title-required
  severity: error
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-operationid-required
  severity: error
- description: Operations should be tagged
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: All paths should be versioned
  given: $.paths[*]~
  name: paths-versioned
  severity: info
- description: Every operation must define at least one response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: warn
- description: Summaries must not be empty
  given: $.paths[*][get,post,put,delete,patch].summary
  name: no-empty-summaries
  severity: error
rules_file: rules/argo-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/argo/refs/heads/main/rules/argo-spectral-rules.yml
severity_counts:
  error: 6
  hint: 0
  info: 1
  warn: 2
slug: argo-spectral-rules
source_filename: argo-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "# Argo Project Spectral Ruleset\n\nrules:\n\n  info-title-required:\n    description: API title must be present\n    severity: error\n    given: \"$.info\"\n    then:\n      field: title\n      function: truthy\n\n  info-description-required:\n    description: API must have a description\n    severity: error\n    given: \"$.info\"\n    then:\n      field: description\n      function: truthy\n\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: summary\n      function: truthy\n\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch]\"\n    then:\n      field: operationId\n      function: truthy\n\n  operation-tags-required:\n    description: Operations should be tagged\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch]\"\
  \n    then:\n      field: tags\n      function: truthy\n\n  paths-versioned:\n    description: All paths should be versioned\n    severity: info\n    given: \"$.paths[*]~\"\n    then:\n      function: pattern\n      functionOptions:\n        match: \"^/api/v\"\n\n  response-success-required:\n    description: Every operation must define at least one response\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].responses\"\n    then:\n      function: schema\n      functionOptions:\n        schema:\n          type: object\n          minProperties: 1\n\n  response-description-required:\n    description: All responses must have a description\n    severity: warn\n    given: \"$.paths[*][get,post,put,delete,patch].responses[*]\"\n    then:\n      field: description\n      function: truthy\n\n  no-empty-summaries:\n    description: Summaries must not be empty\n    severity: error\n    given: \"$.paths[*][get,post,put,delete,patch].summary\"\n    then:\n      function: pattern\n\
  \      functionOptions:\n        match: \".+\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/argo/refs/heads/main/rules/argo-spectral-rules.yml
tags:
- CNCF
- CI/CD
- GitOps
- Kubernetes
- Open Source
- Progressive Delivery
- Workflow Engine
- Spectral
- Linting
- API Governance
---
