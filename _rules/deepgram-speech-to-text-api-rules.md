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
rule_count: 5
rules:
- description: API info should include a Deepgram developer contact.
  given: $.info
  name: deepgram-info-contact
  severity: warn
- description: Servers should reference api.deepgram.com.
  given: $.servers[*].url
  name: deepgram-base-url
  severity: warn
- description: API should declare Token-based bearer authentication.
  given: $.components.securitySchemes
  name: deepgram-token-security
  severity: error
- description: API should expose /v1/listen for transcription.
  given: $.paths
  name: deepgram-listen-resource
  severity: warn
- description: Operations should be tagged Transcription, Speak, or Read.
  given: $.paths[*][*]
  name: deepgram-operation-tags
  severity: warn
rules_file: rules/deepgram-speech-to-text-api-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/deepgram/refs/heads/main/rules/deepgram-speech-to-text-api-rules.yml
severity_counts:
  error: 1
  hint: 0
  info: 0
  warn: 4
slug: deepgram-speech-to-text-api-rules
source_filename: deepgram-speech-to-text-api-rules.yml
source_heading: Spectral Ruleset
source_yaml: "extends:\n  - spectral:oas\nrules:\n  deepgram-info-contact:\n    description: API info should include a Deepgram developer contact.\n    given: $.info\n    severity: warn\n    then:\n      field: contact\n      function: truthy\n  deepgram-base-url:\n    description: Servers should reference api.deepgram.com.\n    given: $.servers[*].url\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"api\\\\.deepgram\\\\.com\"\n  deepgram-token-security:\n    description: API should declare Token-based bearer authentication.\n    given: $.components.securitySchemes\n    severity: error\n    then:\n      field: TokenAuth\n      function: truthy\n  deepgram-listen-resource:\n    description: API should expose /v1/listen for transcription.\n    given: $.paths\n    severity: warn\n    then:\n      function: pattern\n      functionOptions:\n        match: \"/v1/listen\"\n  deepgram-operation-tags:\n    description: Operations should be tagged Transcription,\
  \ Speak, or Read.\n    given: $.paths[*][*]\n    severity: warn\n    then:\n      field: tags\n      function: truthy\n"
source_yaml_url: https://raw.githubusercontent.com/api-evangelist/deepgram/refs/heads/main/rules/deepgram-speech-to-text-api-rules.yml
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
