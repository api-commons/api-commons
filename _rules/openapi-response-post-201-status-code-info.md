---
openapi-response-post-201-status-code-info:
  description: Has 201 status code for POST responses.
  message: POST 201 Status Code
  severity: info
  given: $.paths[*].post.responses
  then:
    field: '201'
    function: falsy
---