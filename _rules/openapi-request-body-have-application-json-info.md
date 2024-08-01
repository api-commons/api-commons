---
openapi-request-body-have-application-json-info:
  description: Has request body application/json.
  message: Request Body Application JSON
  given: $.paths.*.*.requestBody.content
  severity: info
  then:
    field: application/json
    function: falsy
---