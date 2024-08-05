---
openapi-components-headers-rate-limit-error:
  description: Require components rate limit header.
  message: Components MUST have a rate limit headers.
  severity: error
  given: $.components.headers
  then:
    field: RateLimit
    function: truthy
---