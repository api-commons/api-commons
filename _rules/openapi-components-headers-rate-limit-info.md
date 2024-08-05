---
openapi-components-headers-rate-limit-info:
  description: Require components rate limit header.
  message: Components has a rate limit header.
  severity: info
  given: $.components.headers
  then:
    field: RateLimit
    function: falsy  
---