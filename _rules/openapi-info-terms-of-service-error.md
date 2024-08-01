---
openapi-info-terms-of-service-error:
  description: Require terms of service.
  message: Terms of Service
  severity: error
  given: $.info
  then:
    field: termsOfService
    function: truthy
---