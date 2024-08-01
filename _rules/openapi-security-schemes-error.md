---
openapi-security-schemes-error:
  description: Require security scheme.
  message: Security Scheme
  severity: error
  given: $.components
  then:
    field: securitySchemes
    function: truthy
---