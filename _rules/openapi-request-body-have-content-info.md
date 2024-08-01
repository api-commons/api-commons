---
openapi-request-body-have-content-info:
  description: Has request body content.
  message: Request Body Content
  given: $.paths.*.*.requestBody
  severity: info
  then:
    field: content
    function: falsy
---