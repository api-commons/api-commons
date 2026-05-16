---
name: Webhooks
description: Webhooks are a way to communicate between applications by sending data to another application when an event occurs. Webhooks are HTTP-based callback functions that are automated and triggered by an event in a source system, then sent to a destination system, providing event-driven capabilities utilizing simple HTTP "reverse APIs".
image: /images/webhooks.png
url: '#'
machineReadable: false
source: community
tags:
  - Webhooks
  - Event-Driven
aliases:
  - HTTP callbacks
  - Reverse APIs
  - Event notifications

standards:
  - name: Standard Webhooks
    url: https://www.standardwebhooks.com/
    kind: Community / Industry consortium
  - name: OpenAPI 3.1 — webhooks (top-level)
    url: https://spec.openapis.org/oas/v3.1.0#fixed-fields-0
    kind: OpenAPI Initiative
  - name: AsyncAPI 3.0 (suitable for describing webhook channels)
    url: https://www.asyncapi.com/docs/reference/specification/v3.0.0
    kind: AsyncAPI Initiative
  - name: WebSub
    url: https://www.w3.org/TR/websub/
    kind: W3C
  - name: CloudEvents 1.0.2
    url: https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md
    kind: CNCF
  - name: HTTP Signatures (RFC 9421)
    url: https://www.rfc-editor.org/rfc/rfc9421
    kind: IETF
  - name: RFC 9110 — HTTP Semantics
    url: https://www.rfc-editor.org/rfc/rfc9110
    kind: IETF

headers:
  - name: Webhook-Id
    direction: request
    spec: Standard Webhooks
    description: Unique identifier for the delivery; used for idempotency.
  - name: Webhook-Timestamp
    direction: request
    spec: Standard Webhooks
    description: Unix timestamp of the delivery; used in the signature base string.
  - name: Webhook-Signature
    direction: request
    spec: Standard Webhooks
    description: HMAC signature over id.timestamp.payload, base64-encoded.
  - name: Signature
    direction: request
    spec: RFC 9421
    description: HTTP Message Signatures — emerging standard for signed webhook deliveries.
  - name: User-Agent
    direction: request
    spec: RFC 9110
    description: Identifies the sending platform; useful for receiver allowlists.
  - name: Content-Type
    direction: request
    spec: RFC 9110
    description: Typically application/json or application/cloudevents+json.

status_codes:
  - code: '200'
    name: OK
    spec: Convention
    description: Most senders treat any 2xx as successful delivery.
  - code: '410'
    name: Gone
    spec: RFC 9110 §15.5.11
    description: Conventional signal to the sender that the endpoint is permanently disabled.
  - code: '429'
    name: Too Many Requests
    spec: RFC 6585
    description: Backpressure signal; senders should honor Retry-After.

media_types:
  - type: application/json
    note: Default payload format for most webhook providers.
  - type: application/cloudevents+json
    spec: CloudEvents
    note: Standardized event envelope.

openapi_expression:
  - field: webhooks
    spec: OpenAPI 3.1
    description: Top-level map describing incoming webhook operations the API may send to subscribers.
  - field: components.callbacks
    spec: OpenAPI 3.x
    description: Callback objects describing out-of-band requests triggered by an operation.

governance_rules:
  - id: webhook-signed
    source: Convention / Standard Webhooks
    description: Every webhook delivery must carry a verifiable signature.
  - id: webhook-timestamp-verified
    source: Convention / Standard Webhooks
    description: Receivers must reject deliveries older than a tolerance window (e.g. 5 minutes) to prevent replay.
  - id: webhook-idempotent-id
    source: Convention
    description: A stable delivery id must be present so receivers can dedupe retries.
  - id: webhook-retry-policy-documented
    source: Convention
    description: Senders should document retry schedule, max attempts, and dead-lettering.

risk:
  owasp:
    - 'OWASP API Security Top 10: API7:2023 Server Side Request Forgery — outbound webhook URLs can target internal hosts'
    - 'OWASP API Security Top 10: API2:2023 Broken Authentication — unsigned or weakly-signed deliveries are spoofable'
    - 'OWASP API Security Top 10: API8:2023 Security Misconfiguration — receivers often skip TLS verification or signature checks'
  compliance:
    - PCI DSS v4 Req. 4 — encrypt deliveries in transit
    - GDPR Art. 32 — integrity controls on event payloads carrying personal data
    - SOC 2 CC6.7 — protections on data in transmission
  security_implications: Webhooks are an outbound and inbound attack surface. On the sender side, validate destination URLs (block private ranges, enforce TLS, allow only http/https), sign every payload, and rotate signing secrets. On the receiver side, verify signatures and timestamps before doing any work, dedupe on the delivery id, return 2xx fast and process asynchronously, and treat the payload as untrusted input.

tools:
  - name: Svix
    url: https://www.svix.com/
    category: Webhook delivery platform
  - name: Hookdeck
    url: https://hookdeck.com/
    category: Webhook gateway
  - name: ngrok
    url: https://ngrok.com/
    category: Local tunnel for development
  - name: webhook.site
    url: https://webhook.site/
    category: Inspection / debug
  - name: smee.io
    url: https://smee.io/
    category: Webhook proxy
  - name: Standard Webhooks libraries
    url: https://github.com/standard-webhooks/standard-webhooks
    license: MIT
    category: Signing / verification libraries

metrics:
  - name: webhook_delivery_success_rate
    description: Share of deliveries acknowledged with a 2xx on first attempt.
  - name: webhook_delivery_latency_p95
    description: 95th-percentile time from event to acknowledged delivery.
  - name: webhook_retry_rate
    description: Share of deliveries requiring at least one retry.
  - name: webhook_dlq_depth
    description: Number of deliveries currently in the dead-letter queue.
  - name: webhook_signature_failure_rate
    description: Share of inbound deliveries rejected for signature or timestamp failure.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Signed webhooks with Stripe-Signature header and replay-protection timestamp.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: HMAC-SHA256 signatures via X-Hub-Signature-256.
  - provider: Slack
    url: https://providers.apis.io/providers/slack/
    note: Events API with signed payloads and URL verification challenge.
  - provider: Shopify
    url: https://providers.apis.io/providers/shopify/
    note: HMAC-SHA256 signatures via X-Shopify-Hmac-Sha256.

related_properties:
  - asyncapi
  - openapi
  - json-schema
---
