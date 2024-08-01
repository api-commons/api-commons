---
openapi-operations-x-maturity-hint:
  description: Warn x-maturity.
  message: X-Maturity
  severity: hint
  given: $.paths.*[get,post,patch,put,delete]
  then:
    - field: x-maturity
      function: falsy
---