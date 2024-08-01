---
openapi-response-post-404-status-code-info:
  description: Has 404 status code for POST response.
  message: 404 Status Code for POST Responses
  severity: info
  given: $.paths.*.post.responses
  then:
    field: '404'
    function: falsy
---