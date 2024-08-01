---
openapi-response-delete-204-no-body-error:
  description: Require no body for DELETE responses.
  message: No Response Body DELETE
  severity: error
  given: $.paths.*.delete.responses.204
  then:
    field: content
    function: falsy
---