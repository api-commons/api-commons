---
name: Authentication
description: Authentication is essential for most public APIs and is often the most common point of friction when it comes to onboarding with an API. This API Commons property is often a human-readable affair, and will need to become something that is machine-readable if we are going to scale things.
image: /images/authentication.png
url: '#'
tags:
  - Authentication
  - Security
  - Keys
aliases:
  - Auth
  - AuthN
  - Identity
yaml_example: |
  - type: Authentication
    url: https://developers.example.com/authentication

standards:
  - name: RFC 7235 — HTTP/1.1 Authentication
    url: https://www.rfc-editor.org/rfc/rfc7235
    kind: IETF
  - name: RFC 9110 — HTTP Semantics
    url: https://www.rfc-editor.org/rfc/rfc9110
    kind: IETF
  - name: RFC 6749 — OAuth 2.0 Authorization Framework
    url: https://www.rfc-editor.org/rfc/rfc6749
    kind: IETF
  - name: OAuth 2.1 (draft)
    url: https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/
    kind: IETF
  - name: RFC 9700 — Best Current Practice for OAuth 2.0 Security
    url: https://www.rfc-editor.org/rfc/rfc9700
    kind: IETF
  - name: RFC 8252 — OAuth 2.0 for Native Apps
    url: https://www.rfc-editor.org/rfc/rfc8252
    kind: IETF
  - name: RFC 8628 — OAuth 2.0 Device Authorization Grant
    url: https://www.rfc-editor.org/rfc/rfc8628
    kind: IETF
  - name: RFC 8414 — OAuth 2.0 Authorization Server Metadata
    url: https://www.rfc-editor.org/rfc/rfc8414
    kind: IETF
  - name: RFC 7519 — JSON Web Token (JWT)
    url: https://www.rfc-editor.org/rfc/rfc7519
    kind: IETF
  - name: RFC 7517 — JSON Web Key (JWK)
    url: https://www.rfc-editor.org/rfc/rfc7517
    kind: IETF
  - name: RFC 7591 — OAuth 2.0 Dynamic Client Registration
    url: https://www.rfc-editor.org/rfc/rfc7591
    kind: IETF
  - name: RFC 8705 — Mutual TLS Client Authentication for OAuth 2.0
    url: https://www.rfc-editor.org/rfc/rfc8705
    kind: IETF
  - name: OpenID Connect Core 1.0
    url: https://openid.net/specs/openid-connect-core-1_0.html
    kind: OpenID Foundation
  - name: OpenID Connect Discovery 1.0
    url: https://openid.net/specs/openid-connect-discovery-1_0.html
    kind: OpenID Foundation
  - name: WebAuthn Level 3
    url: https://www.w3.org/TR/webauthn-3/
    kind: W3C
  - name: FIDO2
    url: https://fidoalliance.org/fido2/
    kind: FIDO Alliance
  - name: SAML 2.0
    url: https://docs.oasis-open.org/security/saml/v2.0/
    kind: OASIS
  - name: SCIM 2.0 — System for Cross-domain Identity Management
    url: https://www.rfc-editor.org/rfc/rfc7644
    kind: IETF

headers:
  - name: WWW-Authenticate
    direction: response
    spec: RFC 9110 §11.6.1
    description: Server challenges the client to authenticate.
  - name: Authorization
    direction: request
    spec: RFC 9110 §11.6.2
    description: Carries client credentials (Basic, Bearer, etc.).
  - name: Proxy-Authenticate
    direction: response
    spec: RFC 9110 §11.7.1
    description: Proxy challenges the client to authenticate.
  - name: Proxy-Authorization
    direction: request
    spec: RFC 9110 §11.7.2
    description: Carries credentials for an HTTP proxy.

status_codes:
  - code: '401'
    name: Unauthorized
    spec: RFC 9110 §15.5.2
    description: Authentication required or failed.
  - code: '403'
    name: Forbidden
    spec: RFC 9110 §15.5.4
    description: Authenticated identity lacks permission.
  - code: '407'
    name: Proxy Authentication Required
    spec: RFC 9110 §15.5.8

well_known:
  - path: /.well-known/openid-configuration
    spec: OpenID Connect Discovery 1.0
    description: OIDC issuer metadata.
  - path: /.well-known/oauth-authorization-server
    spec: RFC 8414
    description: OAuth 2.0 authorization-server metadata.
  - path: /.well-known/oauth-protected-resource
    spec: RFC 9728
    description: OAuth 2.0 protected-resource metadata.
  - path: /.well-known/jwks.json
    spec: RFC 7517 (de facto path)
    description: JSON Web Key Set published by the issuer.

media_types:
  - type: application/jwt
    spec: RFC 7519
  - type: application/jose
    spec: RFC 7515
  - type: application/x-www-form-urlencoded
    note: OAuth 2.0 token endpoint request bodies (RFC 6749 §4.1.3).
  - type: application/json
    note: Token endpoint responses, JWKS payloads.

openapi_expression:
  - field: components.securitySchemes
    spec: OpenAPI 3.x
    types:
      - apiKey
      - http (basic, bearer, digest)
      - oauth2
      - openIdConnect
      - mutualTLS
  - field: security
    spec: OpenAPI 3.x
    description: Operation-level or global requirement referencing a defined securityScheme.

link_relations:
  - rel: authorization_endpoint
    spec: OIDC Discovery (in JSON, not Link header)
  - rel: token_endpoint
    spec: OIDC Discovery
  - rel: jwks_uri
    spec: OIDC Discovery

governance_rules:
  - id: oas-security-defined
    source: Spectral built-in
    description: Operations must reference a defined security scheme.
  - id: oas3-server-not-example.com
    source: Spectral built-in
    description: Server URL must not be a placeholder (auth often tied to base URL).
  - id: oas-tag-description
    source: Spectral built-in
    description: Tags need descriptions — auth tags benefit from explicit scope notes.

risk:
  owasp:
    - 'OWASP API Security Top 10: API2:2023 Broken Authentication'
    - 'OWASP API Security Top 10: API5:2023 Broken Function Level Authorization'
  compliance:
    - GDPR — lawful basis for processing requires authenticated identity for data-subject rights
    - HIPAA 45 CFR §164.312(a) — access controls and unique user identification
    - PCI DSS v4 Req. 8 — identify and authenticate access to system components
    - SOC 2 CC6.1 — logical and physical access controls
    - NIST SP 800-63B — digital identity guidelines
  security_implications: Weak or missing authentication enables enumeration, account takeover, and data exfiltration. Default to short-lived bearer tokens, refresh-token rotation with reuse detection, mTLS for service-to-service, and WebAuthn/FIDO2 for human factors.

tools:
  - name: Auth0
    url: https://auth0.com/
    category: Managed IdP
  - name: Okta
    url: https://www.okta.com/
    category: Managed IdP
  - name: Keycloak
    url: https://www.keycloak.org/
    license: Apache-2.0
    category: Self-hosted IdP
  - name: Ory Hydra / Kratos
    url: https://www.ory.sh/
    license: Apache-2.0
    category: OAuth/OIDC server
  - name: oauth.tools
    url: https://oauth.tools/
    category: Debugger
  - name: jwt.io
    url: https://jwt.io/
    category: Debugger

metrics:
  - name: auth_success_rate
    description: Successful authentications divided by total attempts; baseline for brute-force / credential-stuffing detection.
  - name: token_issuance_p95_ms
    description: 95th-percentile latency of the token endpoint.
  - name: '401_rate'
    description: Share of responses that are 401 Unauthorized; spikes indicate token churn or breakage.
  - name: refresh_token_reuse_detected
    description: Count of detected refresh-token reuse events (RFC 6749 §10.4 / OAuth 2.1 §6.1).
  - name: mfa_enrolment_rate
    description: Fraction of accounts enrolled in a phishing-resistant second factor.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: API keys (publishable / secret / restricted), connected-account headers.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: PATs, fine-grained tokens, OAuth apps, GitHub Apps with JWT-signed assertions.
  - provider: Google
    url: https://providers.apis.io/providers/google/
    note: OAuth 2.0, Application Default Credentials, service-account JWTs.
  - provider: Microsoft Graph
    url: https://providers.apis.io/providers/microsoft-graph/
    note: Microsoft Entra ID (OIDC) with delegated and application permissions.

related_properties:
  - security
  - login
  - signup
  - rate-limits
  - error-codes
---
