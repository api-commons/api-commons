---
api_specs:
- filename: deepseek-chat-completion-api-openapi.yml
  format: yaml
  label: DeepSeek Chat Completion API
  slug: deepseek-chat-completion-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/deepseek/refs/heads/main/openapi/deepseek-chat-completion-api-openapi.yml
- filename: deepseek-fim-completion-openapi.yml
  format: yaml
  label: DeepSeek Fill-In-The-Middle (FIM) Completion API
  slug: deepseek-fim-completion
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/deepseek/refs/heads/main/openapi/deepseek-fim-completion-openapi.yml
- filename: deepseek-lists-models-api-openapi.yml
  format: yaml
  label: DeepSeek List Models API
  slug: deepseek-lists-models-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/deepseek/refs/heads/main/openapi/deepseek-lists-models-api-openapi.yml
- filename: deepseek-user-balance-api-openapi.yml
  format: yaml
  label: DeepSeek User Balance API
  slug: deepseek-user-balance-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/deepseek/refs/heads/main/openapi/deepseek-user-balance-api-openapi.yml
categories:
- deepseek
description: Spectral linting rules defining API design standards and conventions for DeepSeek.
layout: rules
name: DeepSeek API Rules
provider_name: DeepSeek
provider_slug: deepseek
rule_count: 3
rules:
- description: Servers should reference the DeepSeek beta endpoint.
  given: $.servers[*].url
  name: deepseek-fim-beta-server
  severity: warn
- description: API should expose the /completions resource for FIM completions.
  given: $.paths
  name: deepseek-fim-completions-path
  severity: error
- description: Operations should declare an operationId.
  given: $.paths[*][*]
  name: deepseek-fim-operation-id
  severity: warn
rules_file: rules/deepseek-fim-completion-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/deepseek/refs/heads/main/rules/deepseek-fim-completion-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 2
slug: deepseek-fim-completion-rules
source_filename: deepseek-fim-completion-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  deepseek-fim-beta-server:\n    description: Servers should reference the DeepSeek beta endpoint.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"deepseek.com\"\n  deepseek-fim-completions-path:\n    description: API should expose the /completions resource for FIM completions.\n    given: $.paths\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/completions\"\n  deepseek-fim-operation-id:\n    description: Operations should declare an operationId.\n    given: $.paths[*][*]\n    severity: warn\n    then:\n      field: operationId\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/deepseek/refs/heads/main/rules/deepseek-fim-completion-rules.yml
tags:
- AI
- Artificial Intelligence
- Chat
- Chat Completion
- LLM
- Large Language Models
- Reasoning
- Code Completion
- Spectral
- Linting
- API Governance
---
