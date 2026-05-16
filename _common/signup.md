---
name: Sign Up
description: Where users can sign up for access to an API, providing what is needed to onboard in a manual or automated way, reducing friction in putting to work. Sign up or registration can utilize existing standards like OpenAPI or native solutions which help make it as easy as possible for consumers to manually or automatically sign up to use an API.
image: /images/sign-up.png
url: '#'
machineReadable: false
source: concept
tags:
  - Onboarding
  - Sign Up
  - Registration
aliases:
  - Registration
  - Onboarding
  - Account Creation
  - Provisioning
yaml_example: |
  - type: SignUp
    url: https://developers.example.com/signup

standards:
  - name: RFC 7591 — OAuth 2.0 Dynamic Client Registration Protocol
    url: https://www.rfc-editor.org/rfc/rfc7591
    kind: IETF
  - name: RFC 7592 — OAuth 2.0 Dynamic Client Registration Management Protocol
    url: https://www.rfc-editor.org/rfc/rfc7592
    kind: IETF
  - name: RFC 7642 — SCIM Definitions, Overview, Concepts, and Requirements
    url: https://www.rfc-editor.org/rfc/rfc7642
    kind: IETF
  - name: RFC 7643 — SCIM Core Schema
    url: https://www.rfc-editor.org/rfc/rfc7643
    kind: IETF
  - name: RFC 7644 — SCIM Protocol
    url: https://www.rfc-editor.org/rfc/rfc7644
    kind: IETF
  - name: OpenID Connect Dynamic Client Registration 1.0
    url: https://openid.net/specs/openid-connect-registration-1_0.html
    kind: OpenID Foundation
  - name: RFC 6749 — OAuth 2.0 Authorization Framework
    url: https://www.rfc-editor.org/rfc/rfc6749
    kind: IETF
  - name: NIST SP 800-63A — Enrollment and Identity Proofing
    url: https://pages.nist.gov/800-63-3/sp800-63a.html
    kind: NIST
  - name: schema.org RegisterAction
    url: https://schema.org/RegisterAction
    kind: schema.org

headers:
  - name: Authorization
    direction: request
    spec: RFC 9110 §11.6.2
    description: Initial registration access token (RFC 7591 §3) for management endpoints.
  - name: Location
    direction: response
    spec: RFC 9110 §10.2.2
    description: URI of the newly created client / user resource.

status_codes:
  - code: '201'
    name: Created
    spec: RFC 9110 §15.3.2
    description: New client, user, or tenant resource created.
  - code: '400'
    name: Bad Request
    spec: RFC 9110 §15.5.1
    description: Invalid registration payload (RFC 7591 invalid_client_metadata).
  - code: '409'
    name: Conflict
    spec: RFC 9110 §15.5.10
    description: Email / username / client_id already in use.
  - code: '422'
    name: Unprocessable Content
    spec: RFC 9110 §15.5.21
    description: Semantically invalid signup data (e.g., disposable email).

well_known:
  - path: /.well-known/openid-configuration
    spec: OpenID Connect Discovery 1.0
    description: Exposes registration_endpoint for dynamic client registration.
  - path: /.well-known/oauth-authorization-server
    spec: RFC 8414
    description: Exposes registration_endpoint for OAuth 2.0 DCR.

media_types:
  - type: application/json
    note: Default for RFC 7591 / SCIM 2.0 request and response bodies.
  - type: application/scim+json
    spec: RFC 7644 §3.1
    note: Required for SCIM 2.0 protocol exchanges.

openapi_expression:
  - field: components.securitySchemes
    spec: OpenAPI 3.x
    description: Signup endpoints often require an API key / bootstrap token defined here.
  - field: paths./register or /signup
    spec: OpenAPI 3.x
    description: Conventional signup operations exposed as createUser / registerClient.

link_relations:
  - rel: registration_endpoint
    spec: OIDC Discovery / RFC 8414 (metadata key)
  - rel: register
    note: Used informally in HATEOAS payloads pointing to signup forms.

governance_rules:
  - id: oas-security-defined
    source: Spectral built-in
    description: Public signup operations still need a documented security model (e.g., none + CAPTCHA).
  - id: owasp:api3:2023-no-additionalProperties
    source: Vacuum / Spectral OWASP ruleset
    description: Block mass assignment on registration payloads.
  - id: owasp:api4:2023-rate-limit
    source: Vacuum / Spectral OWASP ruleset
    description: Signup endpoints must be rate-limited to deter abuse.

risk:
  owasp:
    - 'OWASP API Security Top 10: API3:2023 Broken Object Property Level Authorization (mass assignment via signup payloads)'
    - 'OWASP API Security Top 10: API4:2023 Unrestricted Resource Consumption (signup as abuse vector)'
  compliance:
    - GDPR Art. 6 / Art. 7 — lawful basis and consent collected at signup
    - GDPR Art. 8 — special protections for children's data
    - CCPA/CPRA — notice at collection
    - NIST SP 800-63A — identity proofing levels (IAL1–IAL3)
    - SOC 2 CC6.2 — registration and provisioning controls
  security_implications: Signup is the favored abuse target for fraud, spam, and free-tier exploitation. Combine email/phone verification, CAPTCHA or device attestation, IP/ASN reputation, rate limits, and risk scoring. Enforce strict allowlist of properties (defense against mass assignment), capture consent records (terms acceptance, timestamp, version), and emit auditable events for downstream provisioning (SCIM CreateUser, RFC 7591 client_created).

tools:
  - name: Stytch
    url: https://stytch.com/
    category: Hosted signup / passwordless
  - name: Clerk
    url: https://clerk.com/
    category: Hosted signup
  - name: WorkOS Directory Sync
    url: https://workos.com/directory-sync
    category: SCIM provisioning
  - name: Okta SCIM
    url: https://developer.okta.com/docs/concepts/scim/
    category: SCIM provisioning
  - name: hCaptcha
    url: https://www.hcaptcha.com/
    category: Abuse prevention
  - name: Have I Been Pwned API
    url: https://haveibeenpwned.com/API/v3
    category: Breached-password screening

metrics:
  - name: signup_conversion_rate
    description: Completed signups divided by signup-page visits.
  - name: signup_to_first_api_call_minutes
    description: Time-to-first-hello-world after account creation.
  - name: email_verification_rate
    description: Share of new accounts that verify their email/phone.
  - name: fraudulent_signup_block_rate
    description: Share of signup attempts blocked by anti-abuse.
  - name: scim_provision_success_rate
    description: Successful SCIM provisioning events / total events.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Self-service signup with test-mode keys before activation.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: User signup plus OAuth App / GitHub App registration flows.
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: Signup grants trial credit and a verified sender number.
  - provider: Slack
    url: https://providers.apis.io/providers/slack/
    note: Workspace creation, app registration, and SCIM provisioning.

related_properties:
  - authentication
  - login
  - security
  - terms-of-service
  - privacy-policy
---
