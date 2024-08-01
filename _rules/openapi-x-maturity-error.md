---
openapi-x-maturity-error:
  description: Require x-maturity extension.
  message: Maturity Extension
  severity: hint
  given: $
  then:
    field: x-maturity
    function: falsy
---