---
api_specs:
- filename: openapi.json
  format: json
  label: Hugging Face Inference API
  slug: ''
  spec_type: OpenAPI
  url: https://huggingface.co/api-inference/openapi.json
- filename: openapi.json
  format: json
  label: Hugging Face Hub API
  slug: ''
  spec_type: OpenAPI
  url: https://huggingface.co/.well-known/openapi.json
- filename: hugging-face-inference-endpoints-api.yml
  format: yaml
  label: Hugging Face Inference Endpoints API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/hugging-face/refs/heads/main/openapi/hugging-face-inference-endpoints-api.yml
- filename: hugging-face-inference-providers-api.yml
  format: yaml
  label: Hugging Face Inference Providers API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/hugging-face/refs/heads/main/openapi/hugging-face-inference-providers-api.yml
- filename: openapi.json
  format: json
  label: Hugging Face Dataset Viewer API
  slug: ''
  spec_type: OpenAPI
  url: https://datasets-server.huggingface.co/openapi.json
- filename: hugging-face-text-generation-inference-api.yml
  format: yaml
  label: Hugging Face Text Generation Inference API
  slug: ''
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/hugging-face/refs/heads/main/openapi/hugging-face-text-generation-inference-api.yml
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Hugging Face.
layout: rules
name: Hugging Face API Rules
provider_name: Hugging Face
provider_slug: hugging-face
rule_count: 7
rules:
- description: Info title must be present
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/hugging-face-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/hugging-face/refs/heads/main/rules/hugging-face-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: hugging-face-spectral-rules
source_filename: hugging-face-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: summary, function: truthy}\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  response-description-required:\n    description:\
  \ Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/hugging-face/refs/heads/main/rules/hugging-face-spectral-rules.yml
tags:
- Spectral
- Linting
- API Governance
---
