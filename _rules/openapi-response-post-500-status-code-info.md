---
openapi-response-post-500-status-code-info:
  description: Has 500 status code for POST response.
  message: 500 Status Code for POST Responses
  severity: info
  given: $.paths.*.post.responses
  then:
    field: '500'
    function: falsy
---