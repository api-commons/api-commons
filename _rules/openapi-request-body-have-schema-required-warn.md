---
openapi-request-body-have-schema-required-warn:
  description: Warn request body schema required.
  message: Request Body Schema Required
  given: $.paths.*.*.requestBody.content.*.schema.*
  severity: warn
  then:
    field: required
    function: truthy
---