---
openapi-info-terms-of-service-info:
  description: Has terms of service.
  message: Terms of Service
  severity: info
  given: $.info
  then:
    field: termsOfService
    function: falsy
---