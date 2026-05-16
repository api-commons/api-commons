---
name: Console
description: An interactive web UI for managing API access — issuing and rotating credentials, scoping projects, enabling features, and inspecting usage and billing. The console is the operational surface of an API, distinct from the developer portal (informational) and the marketing website (promotional). For cloud-style providers the console is often the dominant consumer surface and the primary trust boundary.
image: /images/console.png
url: '#'
machineReadable: true
source: commons
tags:
  - Management
  - Credentials
  - Operations
aliases:
  - API Console
  - Developer Console
  - Admin Console
  - Management Console
  - Dashboard
yaml_example: |
  - type: Console
    url: https://console.example.com/

standards:
  - name: OAuth 2.0 (RFC 6749)
    url: https://www.rfc-editor.org/rfc/rfc6749
    kind: IETF
  - name: OAuth 2.1 (draft)
    url: https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/
    kind: IETF (draft)
  - name: OpenID Connect Core 1.0
    url: https://openid.net/specs/openid-connect-core-1_0.html
    kind: OpenID Foundation
  - name: WebAuthn Level 3
    url: https://www.w3.org/TR/webauthn-3/
    kind: W3C
  - name: NIST SP 800-63B (Authentication Assurance)
    url: https://pages.nist.gov/800-63-3/sp800-63b.html
    kind: NIST

risk:
  owasp:
    - 'OWASP API Security Top 10: API2:2023 Broken Authentication — consoles concentrate credential operations and are high-value targets.'
    - 'OWASP API Security Top 10: API5:2023 Broken Function Level Authorization — admin-only console actions must not be reachable by lower-tier roles.'
  security_implications: The console concentrates credential issuance, rotation, and project administration into one surface. Require MFA on every account, enforce session timeouts shorter than the API key's lifetime, audit every privileged action, and never reuse the console session for API calls. Treat the console as the highest-trust tier of the platform.
  compliance:
    - SOC 2 CC6.1 — logical access controls cover the console as a privileged interface.
    - PCI DSS v4 Req. 8 — strong authentication required for console access to cardholder environments.
    - GDPR Art. 32 — appropriate technical measures including MFA on admin surfaces.

tools:
  - name: Auth0
    url: https://auth0.com/
    category: Hosted authentication for consoles
  - name: Clerk
    url: https://clerk.com/
    category: Hosted user management for app/console surfaces
  - name: WorkOS
    url: https://workos.com/
    category: Enterprise SSO/SCIM for consoles
  - name: Casbin
    url: https://casbin.org/
    license: Apache-2.0
    category: Authorization library for fine-grained console permissions

metrics:
  - name: mfa_enrollment_rate
    description: Share of console accounts with MFA enabled — should be 100% for admin roles.
  - name: privileged_action_audit_coverage
    description: Share of privileged console actions that emit an audit-log entry.
  - name: console_session_p95
    description: 95th-percentile console session duration — long sessions are a risk surface.
  - name: key_rotation_rate
    description: Share of issued API keys rotated within the documented policy interval.

examples:
  - provider: AWS
    url: https://aws.amazon.com/console/
    note: Canonical cloud management console covering identity, services, and billing.
  - provider: Google Cloud
    url: https://console.cloud.google.com/
    note: Console for project, API, and credential management across Google Cloud services.
  - provider: Stripe
    url: https://dashboard.stripe.com/
    note: Dashboard for keys, webhooks, events, payments, and billing.
  - provider: Twilio
    url: https://console.twilio.com/
    note: Console for project credentials, phone numbers, and usage.

related_properties:
  - authentication
  - login
  - portal
  - security
  - rate-limits
---
