---
openapi-request-body-content-on-put-error:
  description: Requires request body content on PUT.
  message: Request Body Content PUT
  given: $.paths.*.put.requestBody
  severity: error
  then:
    field: content
    function: truthy
---