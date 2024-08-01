---
openapi-request-body-have-content-error:
  description: Require request body content.
  message: Request Body Content
  given: $.paths.*.*.requestBody
  severity: error
  then:
    field: content
    function: truthy
---