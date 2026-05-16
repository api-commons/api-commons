---
name: Login
description: Providing what is needed for existing API consumers to login and access their accounts, keys, and other information regarding their API consumption. A login allows any consumer of an API to be able to access the resources they will need to make a decision when it comes to integrating, expanding, or deprecating their usage of an API, providing what consumers will expect.
image: /images/login.png
url: '#'
machineReadable: false
source: concept
tags:
  - Onboarding
  - Accounts
aliases:
  - Sign In
  - SSO
  - Authentication UX
  - Session
yaml_example: |
  - type: Login
    url: https://developers.example.com/login

standards:
  - name: OpenID Connect Core 1.0
    url: https://openid.net/specs/openid-connect-core-1_0.html
    kind: OpenID Foundation
  - name: OpenID Connect Discovery 1.0
    url: https://openid.net/specs/openid-connect-discovery-1_0.html
    kind: OpenID Foundation
  - name: RFC 6749 — OAuth 2.0 Authorization Framework
    url: https://www.rfc-editor.org/rfc/rfc6749
    kind: IETF
  - name: RFC 8252 — OAuth 2.0 for Native Apps
    url: https://www.rfc-editor.org/rfc/rfc8252
    kind: IETF
  - name: RFC 7636 — Proof Key for Code Exchange (PKCE)
    url: https://www.rfc-editor.org/rfc/rfc7636
    kind: IETF
  - name: RFC 8628 — OAuth 2.0 Device Authorization Grant
    url: https://www.rfc-editor.org/rfc/rfc8628
    kind: IETF
  - name: RFC 9700 — Best Current Practice for OAuth 2.0 Security
    url: https://www.rfc-editor.org/rfc/rfc9700
    kind: IETF
  - name: RFC 6265 — HTTP State Management Mechanism (Cookies)
    url: https://www.rfc-editor.org/rfc/rfc6265
    kind: IETF
  - name: WebAuthn Level 3
    url: https://www.w3.org/TR/webauthn-3/
    kind: W3C
  - name: FIDO2 / CTAP
    url: https://fidoalliance.org/fido2/
    kind: FIDO Alliance
  - name: SAML 2.0 Web Browser SSO Profile
    url: https://docs.oasis-open.org/security/saml/v2.0/saml-profiles-2.0-os.pdf
    kind: OASIS
  - name: NIST SP 800-63B — Authentication and Lifecycle Management
    url: https://pages.nist.gov/800-63-3/sp800-63b.html
    kind: NIST
  - name: CAEP — Continuous Access Evaluation Profile
    url: https://openid.net/specs/openid-caep-1_0.html
    kind: OpenID Foundation

headers:
  - name: Authorization
    direction: request
    spec: RFC 9110 §11.6.2
    description: Bearer or session-bound tokens issued at login.
  - name: Set-Cookie
    direction: response
    spec: RFC 6265
    description: Session cookies issued post-login; use Secure, HttpOnly, SameSite.
  - name: Cookie
    direction: request
    spec: RFC 6265
    description: Client returns the session cookie on subsequent requests.
  - name: WWW-Authenticate
    direction: response
    spec: RFC 9110 §11.6.1
    description: Challenge that may redirect users into a login flow.

status_codes:
  - code: '302'
    name: Found
    spec: RFC 9110 §15.4.3
    description: Common redirect to an OIDC/SAML login endpoint.
  - code: '401'
    name: Unauthorized
    spec: RFC 9110 §15.5.2
    description: Session missing or expired; client should re-authenticate.
  - code: '403'
    name: Forbidden
    spec: RFC 9110 §15.5.4
    description: Authenticated but lacking required permission/MFA assurance.

well_known:
  - path: /.well-known/openid-configuration
    spec: OpenID Connect Discovery 1.0
    description: Advertises authorization_endpoint, token_endpoint, jwks_uri, supported scopes/claims.
  - path: /.well-known/oauth-authorization-server
    spec: RFC 8414
    description: OAuth 2.0 authorization-server metadata.
  - path: /.well-known/webfinger
    spec: RFC 7033
    description: Account discovery prior to OIDC login.
  - path: /.well-known/assetlinks.json
    spec: Android App Links
    description: Native-app login deep-link verification.
  - path: /.well-known/apple-app-site-association
    spec: Apple Universal Links
    description: Native-app login deep-link verification.

media_types:
  - type: application/x-www-form-urlencoded
    note: Token endpoint requests (RFC 6749 §3.2).
  - type: application/json
    note: ID Token / userinfo responses.
  - type: application/jwt
    spec: RFC 7519
    note: ID Tokens issued at login (OIDC Core §2).

openapi_expression:
  - field: components.securitySchemes
    spec: OpenAPI 3.x
    types:
      - oauth2
      - openIdConnect
  - field: components.securitySchemes.*.flows.authorizationCode
    spec: OpenAPI 3.x
    description: Defines authorization/token URLs surfaced by a login flow.

link_relations:
  - rel: authorization_endpoint
    spec: OIDC Discovery (metadata key, not Link header)
  - rel: end_session_endpoint
    spec: OpenID Connect RP-Initiated Logout 1.0
  - rel: token_endpoint
    spec: OIDC Discovery

governance_rules:
  - id: owasp:api2:2023-no-http-basic
    source: Vacuum / Spectral OWASP ruleset
    description: Avoid HTTP Basic in interactive login surfaces.
  - id: oas-security-defined
    source: Spectral built-in
    description: Operations behind login must declare a security requirement.

risk:
  owasp:
    - 'OWASP API Security Top 10: API2:2023 Broken Authentication'
    - 'OWASP Top 10 (web): A07:2021 Identification and Authentication Failures'
  compliance:
    - NIST SP 800-63B AAL2/AAL3 — phishing-resistant authenticators
    - PSD2 RTS SCA — strong customer authentication for EU payments
    - GDPR Art. 32 — appropriate technical measures for account access
    - SOC 2 CC6.1 — logical access controls
  security_implications: Login is the highest-value attack surface. Use PKCE for all OAuth clients (RFC 9700), redirect-URI exact matching, anti-CSRF on form posts, phishing-resistant factors (WebAuthn/passkeys), short access-token lifetimes with refresh-token rotation and reuse detection, account-lockout/back-off against credential stuffing, and device/browser fingerprint anomaly checks.

tools:
  - name: Auth0
    url: https://auth0.com/
    category: Hosted login / IdP
  - name: Okta
    url: https://www.okta.com/
    category: Hosted login / IdP
  - name: Clerk
    url: https://clerk.com/
    category: Hosted login (dev-focused)
  - name: WorkOS
    url: https://workos.com/
    category: Enterprise SSO / SAML
  - name: Keycloak
    url: https://www.keycloak.org/
    license: Apache-2.0
    category: Self-hosted IdP
  - name: Hanko / Passage / SimpleWebAuthn
    url: https://simplewebauthn.dev/
    license: MIT
    category: Passkeys / WebAuthn

metrics:
  - name: login_success_rate
    description: Successful logins over total attempts; primary UX and abuse signal.
  - name: mfa_challenge_rate
    description: Fraction of logins that prompt a second factor.
  - name: passkey_adoption_rate
    description: Share of accounts with at least one registered WebAuthn credential.
  - name: account_lockout_events
    description: Count of accounts temporarily locked due to failed attempts.
  - name: session_duration_p50
    description: Median active-session duration; informs idle-timeout policy.

examples:
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: Password + TOTP/WebAuthn, OAuth, SSO for organizations, passkeys.
  - provider: Google
    url: https://providers.apis.io/providers/google/
    note: OIDC issuer with discovery, Sign-In with Google, passkeys.
  - provider: Microsoft Graph
    url: https://providers.apis.io/providers/microsoft-graph/
    note: Entra ID OIDC, conditional access, FIDO2.
  - provider: Slack
    url: https://providers.apis.io/providers/slack/
    note: Workspace login, Sign in with Slack (OIDC), enterprise SSO.

related_properties:
  - authentication
  - signup
  - security
  - terms-of-service
  - privacy-policy
---
