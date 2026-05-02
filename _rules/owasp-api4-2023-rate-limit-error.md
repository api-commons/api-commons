---
slug: owasp-api4-2023-rate-limit-error
icon: gauge
name: OWASP API4 2023 Rate Limit
description: >-
  Define proper rate limiting to avoid attackers overloading the API. There
  are many ways to implement rate-limiting, but most of them involve using
  HTTP headers. All 2XX and 4XX responses should define rate limiting headers.
message: All 2XX and 4XX responses should define rate limiting headers.
given: $.paths[*]..responses[?(@property.match(/^(2|4)/))]
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
  owasp-api4-2023-rate-limit-error:
    description: >-
      Define proper rate limiting to avoid attackers overloading the API. There
      are many ways to implement rate-limiting, but most of them involve using
      HTTP headers. All 2XX and 4XX responses should define rate limiting headers.
    message: All 2XX and 4XX responses should define rate limiting headers.
    given: $.paths[*]..responses[?(@property.match(/^(2|4)/))]
    severity: error
    then:
      field: headers
      function: truthy
---
