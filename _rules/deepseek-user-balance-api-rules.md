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
- description: Servers should reference api.deepseek.com.
  given: $.servers[*].url
  name: deepseek-balance-server
  severity: warn
- description: API should expose the /user/balance resource.
  given: $.paths
  name: deepseek-balance-path
  severity: error
- description: Operations should declare an operationId.
  given: $.paths[*][*]
  name: deepseek-balance-operation-id
  severity: warn
rules_file: rules/deepseek-user-balance-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/deepseek/refs/heads/main/rules/deepseek-user-balance-api-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 2
slug: deepseek-user-balance-api-rules
source_filename: deepseek-user-balance-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  deepseek-balance-server:\n    description: Servers should reference api.deepseek.com.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"api.deepseek.com\"\n  deepseek-balance-path:\n    description: API should expose the /user/balance resource.\n    given: $.paths\n    severity: error\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/user/balance\"\n  deepseek-balance-operation-id:\n    description: Operations should declare an operationId.\n    given: $.paths[*][*]\n    severity: warn\n    then:\n      field: operationId\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/deepseek/refs/heads/main/rules/deepseek-user-balance-api-rules.yml
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
