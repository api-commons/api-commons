---
name: AsyncAPI
description: AsyncAPI allows you to describe the surface area of event-driven APIs in a machine-readable way, providing a way of defining the protocol, channels, topics, messages, and the schema that are being published and subscribed to. AsyncAPI is a sister specification to the OpenAPI specification, sharing some common properties, as well as support of JSON Schema, but AsyncAPI provides a wider number of protocols than OpenAPI is designed to cover.
image: /images/asyncapi.png
url: https://www.asyncapi.com/en
machineReadable: true
source: community
tags:
  - Event-Driven
  - Messages
aliases:
  - AsyncAPI Specification
  - AAI

standards:
  - name: AsyncAPI Specification 3.0.0
    url: https://www.asyncapi.com/docs/reference/specification/v3.0.0
    kind: AsyncAPI Initiative (Linux Foundation)
  - name: AsyncAPI Specification 2.6.0
    url: https://www.asyncapi.com/docs/reference/specification/v2.6.0
    kind: AsyncAPI Initiative (Linux Foundation)
  - name: AsyncAPI Bindings
    url: https://github.com/asyncapi/bindings
    kind: AsyncAPI Initiative
  - name: JSON Schema Draft 07 (default schema format)
    url: https://json-schema.org/draft-07/schema
    kind: IETF (JSON Schema WG)
  - name: CloudEvents 1.0.2
    url: https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md
    kind: CNCF
  - name: MQTT 5.0
    url: https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html
    kind: OASIS
  - name: AMQP 1.0
    url: https://docs.oasis-open.org/amqp/core/v1.0/amqp-core-overview-v1.0.html
    kind: OASIS

media_types:
  - type: application/vnd.aai.asyncapi
    note: IANA-registered for AsyncAPI in YAML.
  - type: application/vnd.aai.asyncapi+json
    note: IANA-registered for AsyncAPI in JSON.
  - type: application/cloudevents+json
    spec: CloudEvents
    note: Common event envelope referenced from AsyncAPI messages.

openapi_expression:
  - field: asyncapi
    spec: AsyncAPI 3.x
    description: Version string at the root of every document.
  - field: info
    spec: AsyncAPI 3.x
  - field: servers
    spec: AsyncAPI 3.x
    description: Broker endpoints and protocol metadata.
  - field: channels
    spec: AsyncAPI 3.x
    description: Addressable paths/topics where messages are exchanged.
  - field: operations
    spec: AsyncAPI 3.x
    description: Send/receive actions bound to a channel (new shape in 3.0).
  - field: components.messages
    spec: AsyncAPI 3.x
  - field: components.schemas
    spec: AsyncAPI 3.x
  - field: components.messageBindings
    spec: AsyncAPI Bindings
    description: Protocol-specific metadata (Kafka, AMQP, MQTT, WebSocket, etc.).

governance_rules:
  - id: asyncapi2-schema
    source: Spectral built-in (asyncapi rulesets)
    description: Document must validate against the AsyncAPI schema.
  - id: asyncapi-operation-operationId
    source: Spectral built-in
    description: Every operation should have a unique operationId.
  - id: asyncapi-message-name
    source: Spectral built-in
    description: Messages should have a name.
  - id: asyncapi-channel-no-trailing-slash
    source: Spectral built-in
    description: Channel addresses should not end with a trailing slash.

risk:
  owasp:
    - 'OWASP API Security Top 10: API8:2023 Security Misconfiguration — broker auth, ACLs, and TLS are easy to misconfigure'
    - 'OWASP API Security Top 10: API9:2023 Improper Inventory Management — undocumented topics become shadow event surface'
  compliance:
    - SOC 2 CC6.1 — logical access to brokers and topics
    - GDPR — event payloads frequently carry personal data; lineage and retention need to be tracked
  security_implications: Event-driven systems leak through topics, not URLs. Document every published/subscribed topic, schema-validate payloads at the broker boundary, enforce per-topic ACLs, and pin schema versions to avoid poison-message replay.

tools:
  - name: AsyncAPI Studio
    url: https://studio.asyncapi.com/
    license: Apache-2.0
    category: Editor
  - name: AsyncAPI Generator
    url: https://github.com/asyncapi/generator
    license: Apache-2.0
    category: Codegen / Docs
  - name: AsyncAPI CLI
    url: https://github.com/asyncapi/cli
    license: Apache-2.0
    category: CLI
  - name: Microcks
    url: https://microcks.io/
    license: Apache-2.0
    category: Mock / contract test
  - name: Spectral (with asyncapi ruleset)
    url: https://stoplight.io/open-source/spectral
    license: Apache-2.0
    category: Linter
  - name: Modelina
    url: https://github.com/asyncapi/modelina
    license: Apache-2.0
    category: Schema-to-model codegen

metrics:
  - name: asyncapi_coverage
    description: Share of produced/consumed topics described in an AsyncAPI document.
  - name: asyncapi_schema_violations
    description: Count of messages rejected at the broker boundary for schema mismatch.
  - name: asyncapi_breaking_changes
    description: Count of breaking changes detected between AsyncAPI versions.
  - name: broker_topic_inventory_delta
    description: Difference between topics in the broker and topics described in AsyncAPI.

examples:
  - provider: Slack
    url: https://providers.apis.io/providers/slack/
    note: Events API surface lends itself to AsyncAPI modeling for channel/message events.
  - provider: Salesforce
    url: https://providers.apis.io/providers/salesforce/
    note: Platform Events and CDC streams are described with AsyncAPI by some teams.
  - provider: Adyen
    url: https://providers.apis.io/providers/adyen/
    note: Publishes AsyncAPI for webhook event payloads.

related_properties:
  - openapi
  - json-schema
  - webhooks
---
