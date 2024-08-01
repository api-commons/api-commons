---
openapi-request-body-have-schema-required-info:
  description: Has request body schema required.
  message: Request Body Schema Required
  given: $.paths.*.*.requestBody.content.*.schema.*
  severity: info
  then:
    field: required
    function: truthy
---