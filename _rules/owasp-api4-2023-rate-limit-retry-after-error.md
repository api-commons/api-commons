---
slug: owasp-api4-2023-rate-limit-retry-after-error
icon: clock
name: OWASP API4 2023 Rate Limit Retry After
description: >-
  Define proper rate limiting to avoid attackers overloading the API. Part of
  that involves setting a Retry-After header so well-meaning consumers are
  not polling and potentially exacerbating problems.
message: A 429 response should define a Retry-After header.
given: $..responses[429].headers
severity: error
view_sort: B
tags:
  - OWASP
  - Security
  - Rate Limiting
  - OpenAPI
guidance: Rate Limits
guidanceUrl: https://guidance.apievangelist.com/rate-limits
rule:
  owasp-api4-2023-rate-limit-retry-after-error:
    description: >-
      Define proper rate limiting to avoid attackers overloading the API. Part of
      that involves setting a Retry-After header so well-meaning consumers are
      not polling and potentially exacerbating problems.
    message: A 429 response should define a Retry-After header.
    given: $..responses[429].headers
    severity: error
    then:
      field: Retry-After
      function: truthy
---
