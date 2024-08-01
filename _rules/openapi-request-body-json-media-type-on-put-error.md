---
openapi-request-body-json-media-type-on-put-error:
  description: Requires request body content on PUT.
  message: JSON Media Type POSPUTT
  given: $.paths.*.put.requestBody.content
  severity: info
  then:
    field: application/json
    function: falsy
---