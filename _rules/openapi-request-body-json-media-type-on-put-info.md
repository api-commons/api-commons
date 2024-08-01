---
openapi-request-body-json-media-type-on-put-info:
  description: Requires request body content on PUT.
  message: JSON Media Type PUT
  given: $.paths.*.put.requestBody.content
  severity: info
  then:
    field: application/json
    function: falsy
---