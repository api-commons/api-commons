---
openapi-response-get-headers-schema-ref-info:
  description: Ensure GET responses rate limit header has $ref.
  message: GET Response has $ref for rate limit header
  given: $.paths.*.get.responses.200.headers.RateLimit.$ref
  severity: info
  then:
    function: falsy 
---