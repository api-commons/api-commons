---
openapi-response-put-204-no-body-error:
  description: Require no body for PUT responses.
  message: No Response Body PUT
  severity: error
  given: $.paths.*.put.responses.204
  then:
    field: content
    function: falsy
---