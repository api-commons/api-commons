---
openapi-response-get-headers-schema-ref-warn:
  description: Ensure GET responses rate limit header has $ref.
  message: GET Response MUST have $ref for rate limit header
  given: $.paths.*.get.responses.200.headers.RateLimit.$ref
  severity: warn
  then:
    function: truthy
---