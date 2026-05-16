---
name: OpenAI Plugin Manifest
description: OpenAI uses a plugin manifest that references an OpenAPI to allow for extending ChatGPT, and introduce more AI capabilities. Providing a ready to go OpenAI Plugin Manifest for API consumers to use when extending ChatGPT will become a new type of application or integration to consider.
image: /images/openai.png
url: '#'
machineReadable: true
source: platform
tags:
  - Artificial Intelligence
  - AI
  - Extension
  - Plugin
aliases:
  - ai-plugin.json
  - ChatGPT Plugin Manifest
  - OpenAI Plugin

standards:
  - name: ChatGPT Plugin Manifest (ai-plugin.json) — historical
    url: https://platform.openai.com/docs/plugins/getting-started
    kind: OpenAI (vendor, deprecated in favor of GPT Actions / MCP)
  - name: OpenAI GPT Actions (current OpenAI pattern)
    url: https://platform.openai.com/docs/actions
    kind: OpenAI (vendor)
  - name: Model Context Protocol (MCP)
    url: https://modelcontextprotocol.io/
    kind: Anthropic (open spec)
  - name: OpenAPI 3.x (the API surface the manifest points at)
    url: https://spec.openapis.org/oas/v3.1.0
    kind: OpenAPI Initiative
  - name: OAuth 2.0 Authorization Framework
    url: https://www.rfc-editor.org/rfc/rfc6749
    kind: IETF

well_known:
  - path: /.well-known/ai-plugin.json
    spec: ChatGPT Plugin Manifest (historical)
    description: Convention used by the original ChatGPT plugin system to locate the manifest. Not an IANA-registered well-known URI.

media_types:
  - type: application/json
    note: ai-plugin.json is served as JSON.
  - type: application/yaml
    note: The OpenAPI document referenced from the manifest may be JSON or YAML.

openapi_expression:
  - field: api.url
    spec: ChatGPT Plugin Manifest
    description: Manifest field pointing to an OpenAPI 3.x document describing the plugin's API.
  - field: auth
    spec: ChatGPT Plugin Manifest
    description: Authentication block — none, user_http, service_http, or oauth.
    types:
      - none
      - user_http
      - service_http
      - oauth

governance_rules:
  - id: plugin-manifest-schema
    source: OpenAI (historical)
    description: Manifest must include schema_version, name_for_model, name_for_human, description fields, and a reachable OpenAPI URL.
  - id: plugin-openapi-valid
    source: OpenAI (historical)
    description: Referenced OpenAPI document must validate and describe only the operations exposed to the model.
  - id: plugin-auth-explicit
    source: Convention
    description: Manifests with auth.type=none should be limited to read-only, non-sensitive operations.
  - id: plugin-rate-limits-documented
    source: Convention
    description: OpenAPI document should document rate limits the model should respect.

risk:
  owasp:
    - 'OWASP API Security Top 10: API2:2023 Broken Authentication — plugin OAuth flows often misconfigure scopes and redirect URIs'
    - 'OWASP LLM Top 10: LLM01 Prompt Injection — tool descriptions and response bodies can carry instructions to the model'
    - 'OWASP LLM Top 10: LLM07 Insecure Plugin Design — over-broad operations enable unintended actions on behalf of the user'
  compliance:
    - SOC 2 CC6.1 — plugin auth tokens are an access surface
    - GDPR Art. 6 — lawful basis required when the model acts on personal data on the user's behalf
  security_implications: AI plugins / tools turn an LLM into a confused-deputy client. Scope OAuth tightly, never include destructive operations without explicit user confirmation, treat all model-supplied parameters as untrusted, log every tool call, and assume tool responses may carry prompt-injection payloads. The original ai-plugin.json pattern has been largely superseded — new integrations should target GPT Actions (OpenAI) or MCP (Anthropic and a growing set of clients) rather than the legacy manifest.

tools:
  - name: OpenAI GPT Actions
    url: https://platform.openai.com/docs/actions
    category: Current OpenAI tool-calling pattern (replaces ai-plugin.json)
  - name: Model Context Protocol (MCP)
    url: https://modelcontextprotocol.io/
    license: MIT
    category: Open tool-calling protocol
  - name: MCP servers reference
    url: https://github.com/modelcontextprotocol/servers
    license: MIT
    category: Reference MCP server implementations
  - name: Swagger Editor
    url: https://swagger.io/tools/swagger-editor/
    license: Apache-2.0
    category: Edit the underlying OpenAPI
  - name: Spectral
    url: https://stoplight.io/open-source/spectral
    license: Apache-2.0
    category: Lint the underlying OpenAPI

metrics:
  - name: plugin_tool_call_count
    description: Number of times the model invoked an operation exposed by the manifest.
  - name: plugin_tool_error_rate
    description: Share of tool calls that returned an error.
  - name: plugin_auth_failure_rate
    description: Share of tool calls that failed authentication.
  - name: plugin_user_consent_rate
    description: Share of destructive tool calls confirmed by the user (where confirmation is required).

examples:
  - provider: OpenAI
    url: https://providers.apis.io/providers/openai/
    note: Originator of the ai-plugin.json manifest; now ships GPT Actions.
  - provider: Anthropic
    url: https://providers.apis.io/providers/anthropic/
    note: Defines and ships the Model Context Protocol (MCP), the open alternative to plugin manifests.

related_properties:
  - openapi
  - json-schema
---
