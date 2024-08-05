---
openapi-response-post-401-status-code-info:
  description: Has 401 status code for POST response.
  message: 401 Status Code for POST Responses
  severity: info
  given: $.paths.*.post.responses
  then:
    field: "401"
    function: falsy
---