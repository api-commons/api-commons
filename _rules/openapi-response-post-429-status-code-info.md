---
openapi-response-post-429-status-code-info:
  description: Has 429 status code for POST response.
  message: 429 Status Code for POST Responses
  severity: info
  given: $.paths.*.post.responses
  then:
    field: "429"
    function: falsy   
---