---
slug: openapi-response-ratelimit-headers-error
icon: gauge
name: OpenAPI Response RateLimit Headers
description: >-
  API responses must include the standard rate limit header trio (ratelimit-limit, ratelimit-remaining, ratelimit-reset) to inform consumers of their current usage against rate limits.
message: Responses MUST include ratelimit-limit, ratelimit-remaining, and ratelimit-reset headers.
given: $..responses[?(@property.match(/^2/))].headers
severity: error
view_sort: B
tags:
  - OpenAPI
  - Responses
  - Rate Limiting
  - Headers
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-ratelimit-headers-error:
    description: >-
      API responses must include the standard rate limit header trio (ratelimit-limit, ratelimit-remaining, ratelimit-reset) to inform consumers of their current usage against rate limits.
    message: Responses MUST include ratelimit-limit, ratelimit-remaining, and ratelimit-reset headers.
    given: $..responses[?(@property.match(/^2/))].headers
    severity: error
    then:
      - field: ratelimit-limit
        function: truthy
      - field: ratelimit-remaining
        function: truthy
      - field: ratelimit-reset
        function: truthy
---
