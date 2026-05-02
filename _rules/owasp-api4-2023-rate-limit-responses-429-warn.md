---
slug: owasp-api4-2023-rate-limit-responses-429-warn
icon: gauge
name: OWASP API4 2023 Rate Limit Responses 429
description: >-
  A HTTP 429 response signals the API client is making too many requests, and
  will supply information about when to retry so that the client can back off
  calmly without everything breaking. All operations should define a 429
  response.
message: Operation is missing rate limiting response (429).
given: $.paths..responses
severity: warn
view_sort: B
tags:
  - OWASP
  - Security
  - Rate Limiting
  - Responses
  - OpenAPI
guidance: Rate Limits
guidanceUrl: https://guidance.apievangelist.com/rate-limits
rule:
  owasp-api4-2023-rate-limit-responses-429-warn:
    description: >-
      A HTTP 429 response signals the API client is making too many requests, and
      will supply information about when to retry so that the client can back off
      calmly without everything breaking. All operations should define a 429
      response.
    message: Operation is missing rate limiting response (429).
    given: $.paths..responses
    severity: warn
    then:
      field: "429"
      function: truthy
---
