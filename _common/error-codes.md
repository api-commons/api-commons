---
name: Error Codes
description: Providing a detailed list of error codes that API consumers can expect when integrating with an API, sharing common HTTP status codes, but also custom errors returned. Having a single page helps communicate errors with consumers, but it also helps producers evaluate how errors are handled across many different APIs.
image: /images/errors.png
url: '#'
machineReadable: false
source: concept
tags:
  - Errors
  - Status
aliases:
  - Errors
  - Problem Details
  - Status Codes
yaml_example: |
  - type: ErrorCodes
    url: https://developers.example.com/errors

standards:
  - name: RFC 9457 — Problem Details for HTTP APIs
    url: https://www.rfc-editor.org/rfc/rfc9457
    kind: IETF
  - name: RFC 7807 — Problem Details for HTTP APIs (obsoleted by RFC 9457)
    url: https://www.rfc-editor.org/rfc/rfc7807
    kind: IETF (historic)
  - name: RFC 9110 — HTTP Semantics (Status Codes §15)
    url: https://www.rfc-editor.org/rfc/rfc9110
    kind: IETF
  - name: RFC 6585 — Additional HTTP Status Codes
    url: https://www.rfc-editor.org/rfc/rfc6585
    kind: IETF
  - name: RFC 8288 — Web Linking
    url: https://www.rfc-editor.org/rfc/rfc8288
    kind: IETF
  - name: gRPC Status Codes
    url: https://grpc.github.io/grpc/core/md_doc_statuscodes.html
    kind: gRPC project
  - name: google.rpc.Status / google.rpc.ErrorInfo
    url: https://cloud.google.com/apis/design/errors
    kind: Vendor guideline
  - name: OpenAPI Specification (Responses Object)
    url: https://spec.openapis.org/oas/latest.html
    kind: OpenAPI Initiative
  - name: JSON:API Errors
    url: https://jsonapi.org/format/#errors
    kind: Community spec

headers:
  - name: Content-Type
    direction: response
    spec: RFC 9110 §8.3
    description: Should be application/problem+json (or +xml) for Problem Details payloads.
  - name: Content-Language
    direction: response
    spec: RFC 9110 §8.5
    description: Optional natural-language tag for localised error detail.

status_codes:
  - code: '400'
    name: Bad Request
    spec: RFC 9110 §15.5.1
  - code: '401'
    name: Unauthorized
    spec: RFC 9110 §15.5.2
  - code: '403'
    name: Forbidden
    spec: RFC 9110 §15.5.4
  - code: '404'
    name: Not Found
    spec: RFC 9110 §15.5.5
  - code: '409'
    name: Conflict
    spec: RFC 9110 §15.5.10
  - code: '422'
    name: Unprocessable Content
    spec: RFC 9110 §15.5.21
  - code: '429'
    name: Too Many Requests
    spec: RFC 6585 §4
  - code: '500'
    name: Internal Server Error
    spec: RFC 9110 §15.6.1
  - code: '503'
    name: Service Unavailable
    spec: RFC 9110 §15.6.4

media_types:
  - type: application/problem+json
    spec: RFC 9457
    note: Default Problem Details payload. Fields include type, title, status, detail, instance.
  - type: application/problem+xml
    spec: RFC 9457
  - type: application/vnd.api+json
    spec: JSON:API
    note: Carries an errors array with id, status, code, title, detail, and source pointers.

openapi_expression:
  - field: responses
    spec: OpenAPI 3.x
    description: Per-operation map of HTTP status codes to Response objects describing error shapes.
  - field: components.responses
    spec: OpenAPI 3.x
    description: Reusable error responses (e.g. NotFound, RateLimited) referenced across operations.
  - field: components.schemas.Problem
    spec: OpenAPI 3.x
    description: Conventional schema name for the RFC 9457 Problem Details object.

link_relations:
  - rel: help
    spec: RFC 8288 / IANA
    note: Often used inside Problem Details "type" or via Link header to point at error documentation.
  - rel: about
    spec: RFC 6903

governance_rules:
  - id: problem-details-*
    source: API Commons Problem Details ruleset (spectral-problem-details-ruleset)
    description: >-
      Sixteen rules checking an OpenAPI's error responses against RFC 9457 — the
      problem+json media type on 4xx/5xx, the five members and their JSON types,
      extension members, and the WWW-Authenticate and Retry-After headers that
      belong with 401 and 429.
  - id: problem-details-status-is-number
    source: API Commons Problem Details ruleset
    description: >-
      `status` declared as a string is the most common problem detail defect, and
      RFC 9457 §3.1 requires a consumer to ignore any member whose type does not
      match — so it fails silently rather than loudly.
  - id: problem-details-allows-extension-members
    source: API Commons Problem Details ruleset
    description: >-
      `additionalProperties: false` forbids the extension members RFC 9457 §3.2
      builds its evolution story on. Emitted by default by several schema
      generators, and invisible in review.
  - id: oas-operation-4xx-response
    source: Spectral built-in
    description: Operations should declare at least one 4xx response.
  - id: oas-default-response
    source: Spectral built-in
    description: A default response covers unspecified error cases.
  - id: naftiko-error-codes
    source: Naftiko Sandbox (error-codes/*.yml)
    description: Checks for problem+json usage and consistent error schemas.

risk:
  owasp:
    - 'OWASP API Security Top 10: API8:2023 Security Misconfiguration'
  compliance:
    - PCI DSS v4 Req. 6.2 — secure error handling without leaking sensitive data
    - SOC 2 CC7.2 — system monitoring of errors and anomalies
  security_implications: Verbose error responses can leak stack traces, internal hostnames, query fragments, or PII. Use Problem Details with stable type URIs, redact sensitive fields, and ensure error bodies do not vary based on existence of resources in ways that enable enumeration.

tools:
  - name: API Commons Problem Details ruleset
    url: https://github.com/api-commons/spectral-problem-details-ruleset
    license: Apache-2.0
    category: Spectral ruleset for RFC 9457
  - name: Problem Details base OpenAPI
    url: https://github.com/api-commons/problem-details-for-http-apis
    license: Apache-2.0
    category: Reusable base
  - name: Spectral
    url: https://github.com/stoplightio/spectral
    license: Apache-2.0
    category: Linter
  - name: zalando/problem (Java)
    url: https://github.com/zalando/problem
    license: MIT
    category: Library
  - name: problem-details (Python)
    url: https://github.com/related-sciences/python-problem-details
    category: Library
  - name: ProblemDetails (.NET)
    url: https://learn.microsoft.com/aspnet/core/web-api/handle-errors
    category: Framework
  - name: oasdiff
    url: https://github.com/oasdiff/oasdiff
    license: Apache-2.0
    category: Breaking-change detector

metrics:
  - name: '4xx_rate'
    description: Share of responses with client-error status codes.
  - name: '5xx_rate'
    description: Share of responses with server-error status codes; SLO-critical.
  - name: problem_json_coverage
    description: Fraction of error responses using application/problem+json.
  - name: top_error_types
    description: Most frequent Problem type URIs; informs documentation and DX work.

examples:
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: Documented error responses with message and documentation_url fields.
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Typed error categories (api_error, card_error, idempotency_error) with codes and decline reasons.
  - provider: Google
    url: https://providers.apis.io/providers/google/
    note: google.rpc.Status with typed details (ErrorInfo, BadRequest, QuotaFailure).
  - provider: Microsoft Graph
    url: https://providers.apis.io/providers/microsoft-graph/
    note: OData-style error envelope with code, message, innerError, and target fields.

related_properties:
  - authentication
  - rate-limits
  - status-page
  - versioning
  - lifecycle
---
