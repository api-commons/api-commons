---
name: Rate Limits
description: All APIs should possess rate limits that govern the amount of any digital resource or capability a consumer be able to access, with well-communicated, consistent, and enforced rate limits. Rate limits are what give API producers control over their digital resources, and are a fundamental aspect of how any type of APIs is publicly made available.
image: /images/rate-limits.png
url: '#'
machineReadable: true
source: commons
tags:
  - Rate Limits
  - Usage
  - Constraints
aliases:
  - Throttling
  - Quotas
  - Usage Limits
yaml_example: |
  - name: Rate Limits
    type: RateLimits
    url: https://developers.example.com/rate-limits
    source_date: '2026-08-17'
    data:
      - name: Platform requests
        type: Platform
        limit: 10000
        metric: request
        timeframe: hour
        description: Requests per hour across the whole API for a single account.

standards:
  - name: API Commons Rate Limits schema
    url: https://github.com/api-commons/rate-limits
    kind: API Commons (Apache-2.0)
  - name: RateLimit header fields for HTTP (draft-ietf-httpapi-ratelimit-headers)
    url: https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/
    kind: IETF
  - name: RFC 6585 — Additional HTTP Status Codes (429 Too Many Requests)
    url: https://www.rfc-editor.org/rfc/rfc6585
    kind: IETF
  - name: RFC 9110 — HTTP Semantics (Retry-After §10.2.3)
    url: https://www.rfc-editor.org/rfc/rfc9110
    kind: IETF
  - name: RFC 9111 — HTTP Caching
    url: https://www.rfc-editor.org/rfc/rfc9111
    kind: IETF
  - name: IETF HTTP APIs Working Group
    url: https://datatracker.ietf.org/wg/httpapi/about/
    kind: IETF WG
  - name: X-RateLimit-* (de facto industry convention)
    url: https://datatracker.ietf.org/doc/html/draft-ietf-httpapi-ratelimit-headers#appendix-A
    kind: De facto

headers:
  - name: RateLimit
    direction: response
    spec: draft-ietf-httpapi-ratelimit-headers
    description: Structured field conveying remaining quota and the reset interval for the current policy.
  - name: RateLimit-Policy
    direction: response
    spec: draft-ietf-httpapi-ratelimit-headers
    description: Advertises one or more quota policies (limit and window) that apply to the request.
  - name: Retry-After
    direction: response
    spec: RFC 9110 §10.2.3
    description: Seconds (or HTTP-date) the client should wait before retrying after a 429 or 503.
  - name: X-RateLimit-Limit
    direction: response
    spec: De facto
    description: Maximum number of requests permitted in the current window.
  - name: X-RateLimit-Remaining
    direction: response
    spec: De facto
    description: Requests remaining in the current window.
  - name: X-RateLimit-Reset
    direction: response
    spec: De facto
    description: Time at which the current window resets, usually as a Unix timestamp or seconds remaining.

status_codes:
  - code: '429'
    name: Too Many Requests
    spec: RFC 6585 §4
    description: Client has sent too many requests within a given time window.
  - code: '503'
    name: Service Unavailable
    spec: RFC 9110 §15.6.4
    description: Server-side throttling or overload; pair with Retry-After.

media_types:
  - type: application/problem+json
    spec: RFC 9457
    note: Recommended payload for explaining quota errors.

openapi_expression:
  - field: responses.'429'
    spec: OpenAPI 3.x
    description: Declare a 429 response with headers for RateLimit, RateLimit-Policy, and Retry-After.
  - field: components.headers
    spec: OpenAPI 3.x
    description: Define reusable RateLimit / X-RateLimit-* header objects.
  - field: x-ratelimit
    spec: Vendor extension
    description: Common provider extension for declaring tier-based quotas at the operation or document level.

governance_rules:
  - id: naftiko-rate-limits
    source: Naftiko Sandbox (rate-limits/*.yml)
    description: Rules that check operations declare 429 responses and standard RateLimit headers.
  - id: oas-operation-4xx-response
    source: Spectral built-in
    description: Operations should document client-error responses, including 429.

risk:
  owasp:
    - 'OWASP API Security Top 10: API4:2023 Unrestricted Resource Consumption'
  compliance:
    - SOC 2 CC7.2 — system monitoring for abnormal usage
    - PCI DSS v4 Req. 6.4.2 — protect public-facing applications against attacks
  security_implications: Without enforced rate limits, APIs are vulnerable to credential stuffing, scraping, denial-of-wallet (for metered backends), and DoS. Apply per-key, per-IP, and per-tenant limits; surface quota state via standard headers; degrade gracefully with 429 + Retry-After rather than dropping connections.

tools:
  - name: API Commons Rate Limits schema + validator
    url: https://github.com/api-commons/rate-limits
    license: Apache-2.0
    category: Machine-readable schema
  - name: Kong Rate Limiting
    url: https://docs.konghq.com/hub/kong-inc/rate-limiting/
    category: Gateway plugin
  - name: Envoy Rate Limit Service
    url: https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/other_features/global_rate_limiting
    license: Apache-2.0
    category: Proxy
  - name: Redis Cell / GCRA
    url: https://github.com/brandur/redis-cell
    license: MIT
    category: Algorithm
  - name: NGINX limit_req
    url: https://nginx.org/en/docs/http/ngx_http_limit_req_module.html
    category: Proxy
  - name: Cloudflare Rate Limiting
    url: https://developers.cloudflare.com/waf/rate-limiting-rules/
    category: Edge

metrics:
  - name: '429_rate'
    description: Fraction of responses returning 429; spikes signal under-provisioned quota or abusive clients.
  - name: quota_utilization_p95
    description: 95th-percentile fraction of quota consumed per window, per key.
  - name: throttled_clients_unique
    description: Distinct clients hitting limits in a period; informs tier design.
  - name: retry_after_compliance
    description: Share of retrying clients that honour Retry-After before re-issuing requests.

examples:
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: Primary and secondary rate limits exposed via X-RateLimit-* headers.
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Per-account request limits with 429 responses and exponential backoff guidance.
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: Concurrency and queue-based limits across messaging APIs.
  - provider: Discord
    url: https://providers.apis.io/providers/discord/
    note: Global and per-route buckets surfaced via X-RateLimit-Bucket and reset headers.

related_properties:
  - authentication
  - error-codes
  - status-page
  - plans
  - usage
---
