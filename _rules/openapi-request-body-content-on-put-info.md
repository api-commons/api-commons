---
openapi-request-body-content-on-put-info:
  description: Requires request body content on PUT.
  message: Request Body Content PUT
  given: $.paths.*.put.requestBody
  severity: info
  then:
    field: content
    function: falsy
---