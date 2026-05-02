---
api_specs:
- filename: assistants-openapi-original.yml
  format: yaml
  label: OpenAI Assistants API
  slug: openai-assistants-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/openapi/assistants-openapi-original.yml
- filename: audio-openapi-original.yml
  format: yaml
  label: OpenAI Audio API
  slug: openai-audio-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/openapi/audio-openapi-original.yml
- filename: chat-openapi-original.yml
  format: yaml
  label: OpenAI Chat API
  slug: openai-chat-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/openapi/chat-openapi-original.yml
- filename: openai-chat-completions-openapi.yml
  format: yaml
  label: OpenAI Chat Completions API
  slug: openai-chat-completions-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/openapi/openai-chat-completions-openapi.yml
- filename: embeddings-openapi-original.yml
  format: yaml
  label: OpenAI Embeddings API
  slug: openai-embeddings-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/openapi/embeddings-openapi-original.yml
- filename: files-openapi-original.yml
  format: yaml
  label: OpenAI Files API
  slug: openai-files-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/openapi/files-openapi-original.yml
- filename: fine-tuning-openapi-original.yml
  format: yaml
  label: OpenAI Fine Tuning API
  slug: openai-fine-tuning-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/openapi/fine-tuning-openapi-original.yml
- filename: images-openapi-original.yml
  format: yaml
  label: OpenAI Images API
  slug: openai-images-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/openapi/images-openapi-original.yml
- filename: models-openapi-original.yml
  format: yaml
  label: OpenAI Models API
  slug: openai-models-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/openapi/models-openapi-original.yml
- filename: threads-openapi-original.yml
  format: yaml
  label: OpenAI Threads API
  slug: openai-threads-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/openapi/threads-openapi-original.yml
- filename: completions-openapi-original.yml
  format: yaml
  label: OpenAI Completions API
  slug: openai-completions-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/openapi/completions-openapi-original.yml
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for OpenAI.
layout: rules
name: OpenAI API Rules
provider_name: OpenAI
provider_slug: openai
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
rules_file: rules/openai-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/rules/openai-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: openai-spectral-rules
source_filename: openai-spectral-rules.yml
source_heading: Spectral Ruleset
source_yaml: "rules:\n  info-title-required:\n    description: Info title must be present\n    severity: error\n    given: $.info\n    then: {field: title, function: truthy}\n  info-description-required:\n    description: Info description must be present\n    severity: error\n    given: $.info\n    then: {field: description, function: truthy}\n  operation-operationid-required:\n    description: Every operation must have an operationId\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: operationId, function: truthy}\n  operation-summary-required:\n    description: Every operation must have a summary\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: summary, function: truthy}\n  operation-tags-required:\n    description: Every operation must have tags\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete]\n    then: {field: tags, function: truthy}\n  response-description-required:\n    description:\
  \ Every response must have a description\n    severity: error\n    given: $.paths[*][get,post,put,patch,delete].responses[*]\n    then: {field: description, function: truthy}\n  no-empty-descriptions:\n    description: Descriptions must not be empty\n    severity: error\n    given: $..description\n    then: {function: truthy}\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/rules/openai-spectral-rules.yml
tags:
- AI
- Artificial Intelligence
- Large Language Models
- T1
- Spectral
- Linting
- API Governance
---
