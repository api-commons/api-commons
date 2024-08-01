---
openapi-security-schemes-info:
  description: Has security scheme.
  message: Security Scheme
  severity: info
  given: $.components
  then:
    field: securitySchemes
    function: falsy
---