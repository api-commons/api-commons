---
name: Sandbox
description: An isolated environment that mirrors the production API but operates on non-real data, so consumers can integrate, test, and demo without financial, reputational, or compliance consequences. Sandboxes are essential for any API that moves money, sends messages, mutates real-world state, or is subject to per-call cost — and increasingly expected even for read-only APIs as a low-friction way to evaluate.
image: /images/sandbox.png
url: '#'
machineReadable: true
source: commons
tags:
  - Onboarding
  - Testing
  - Environments
aliases:
  - Sandbox Environment
  - Test Environment
  - Sandbox Mode
  - Test Mode
  - Staging
yaml_example: |
  - type: Sandbox
    url: https://sandbox.example.com/

standards:
  - name: OpenAPI Specification 3.1
    url: https://spec.openapis.org/oas/v3.1.0
    kind: OpenAPI Initiative
  - name: RFC 2606 — Reserved Top Level DNS Names
    url: https://www.rfc-editor.org/rfc/rfc2606
    kind: IETF
  - name: PSD2 Regulatory Technical Standards (sandbox requirement)
    url: https://www.eba.europa.eu/regulation-and-policy/payment-services-and-electronic-money
    kind: Regulatory (EBA)

openapi_expression:
  - field: servers
    spec: OpenAPI 3.x
    description: Sandbox base URLs are declared alongside production via the servers array.
  - field: servers[].description
    spec: OpenAPI 3.x
    description: Used to distinguish "Sandbox" from "Production" server entries.
  - field: servers[].variables
    spec: OpenAPI 3.x
    description: Templating across environments without duplicating server entries.

risk:
  security_implications: Sandbox credentials leaking is low-impact per call, but sandbox environments routinely allow attackers to enumerate production endpoint shapes, error messages, and rate-limit behavior. Keep sandbox infrastructure logically and operationally separate from production, and never accept production credentials in sandbox.
  compliance:
    - PSD2 (EU) — open-banking APIs are required to expose a sandbox.
    - Open Banking UK — equivalent sandbox mandate for regulated providers.
    - PCI DSS — sandbox card data must use test PANs only, never real cardholder data.

tools:
  - name: Prism
    url: https://stoplight.io/open-source/prism
    license: Apache-2.0
    category: Mock server generated from OpenAPI
  - name: Postman Mock Server
    url: https://learning.postman.com/docs/designing-and-developing-your-api/mocking-data/setting-up-mock/
    category: Hosted mocks
  - name: WireMock
    url: https://wiremock.org/
    license: Apache-2.0
    category: HTTP mock and recorder
  - name: Mockoon
    url: https://mockoon.com/
    license: MIT
    category: Desktop mock server

metrics:
  - name: sandbox_signup_to_first_call
    description: Time from sandbox key issuance to first 2xx response.
  - name: sandbox_to_production_conversion
    description: Share of sandbox accounts that promote to production credentials.
  - name: sandbox_parity_drift
    description: Count of endpoints or fields present in production but missing in sandbox.

examples:
  - provider: Stripe
    url: https://stripe.com/docs/testing
    note: Test mode using test API keys with deterministic test card numbers.
  - provider: Plaid
    url: https://plaid.com/docs/sandbox/
    note: Sandbox environment with synthetic financial-institution data.
  - provider: PayPal
    url: https://developer.paypal.com/tools/sandbox/
    note: Sandbox accounts for buyer and seller flows.
  - provider: Adyen
    url: https://docs.adyen.com/development-resources/test-cards/
    note: Test environment with deterministic card behavior and webhooks.

related_properties:
  - authentication
  - getting-started
  - rate-limits
  - portal
---
