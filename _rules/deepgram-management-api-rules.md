---
api_specs:
- filename: deepgram-speech-to-text-openapi.yml
  format: yaml
  label: Deepgram Speech-To-Text API
  slug: speech-to-text-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/deepgram/refs/heads/main/openapi/deepgram-speech-to-text-openapi.yml
- filename: deepgram-text-to-speech-openapi.yml
  format: yaml
  label: Deepgram Text-To-Speech API
  slug: text-to-speech-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/deepgram/refs/heads/main/openapi/deepgram-text-to-speech-openapi.yml
- filename: deepgram-voice-agent-asyncapi.yml
  format: yaml
  label: Deepgram Voice Agent API
  slug: voice-agent-api
  spec_type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/deepgram/refs/heads/main/asyncapi/deepgram-voice-agent-asyncapi.yml
- filename: deepgram-speech-to-text-openapi.yml
  format: yaml
  label: Deepgram Audio Intelligence API
  slug: audio-intelligence-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/deepgram/refs/heads/main/openapi/deepgram-speech-to-text-openapi.yml
- filename: deepgram-management-openapi.yml
  format: yaml
  label: Deepgram Management API
  slug: management-api
  spec_type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/deepgram/refs/heads/main/openapi/deepgram-management-openapi.yml
categories:
- deepgram
description: Spectral linting rules defining API design standards and conventions for Deepgram.
layout: rules
name: Deepgram API Rules
provider_name: Deepgram
provider_slug: deepgram
rule_count: 4
rules:
- description: Management API info should include a Deepgram developer contact.
  given: $.info
  name: deepgram-mgmt-info-contact
  severity: warn
- description: Servers should reference api.deepgram.com.
  given: $.servers[*].url
  name: deepgram-mgmt-base-url
  severity: warn
- description: API should expose /v1/projects for project management.
  given: $.paths
  name: deepgram-mgmt-projects-resource
  severity: warn
- description: API should expose API key management endpoints.
  given: $.paths
  name: deepgram-mgmt-keys-resource
  severity: warn
rules_file: rules/deepgram-management-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/deepgram/refs/heads/main/rules/deepgram-management-api-rules.yml
severity_counts:
  error: 0
  hint: 0
  info: 0
  warn: 4
slug: deepgram-management-api-rules
source_filename: deepgram-management-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  deepgram-mgmt-info-contact:\n    description: Management API info should include a Deepgram developer contact.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  deepgram-mgmt-base-url:\n    description: Servers should reference api.deepgram.com.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"api\\\\.deepgram\\\\.com\"\n  deepgram-mgmt-projects-resource:\n    description: API should expose /v1/projects for project management.\n    given: $.paths\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/v1/projects\"\n  deepgram-mgmt-keys-resource:\n    description: API should expose API key management endpoints.\n    given: $.paths\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/keys\"\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/deepgram/refs/heads/main/rules/deepgram-management-api-rules.yml
tags:
- Artificial Intelligence
- Speech-To-Text
- Text-To-Speech
- Transcription
- Voice AI
- Spectral
- Linting
- API Governance
---
