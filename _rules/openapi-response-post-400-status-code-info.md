---
openapi-response-post-400-status-code-info:
  description: Warn 400 status code for POST response.
  message: 400 Status Code for POST Responses
  severity: info
  given: $.paths.*.post.responses
  then:
    field: '400'
    function: falsy
---