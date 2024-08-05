---
openapi-response-description-error:
  description: Ensures responses have description.
  message: Responses MUST have descriptions.
  severity: error
  given: $.paths.*.get.responses.*
  then:
    field: description
    function: truthy
---