---
openapi-response-description-info:
  description: Ensures GET operations have a 200 status code response.
  message: Response has description
  severity: info
  given: $.paths.*.get.responses.*
  then:
    field: description
    function: falsy
---