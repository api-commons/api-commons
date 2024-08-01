---
openapi-response-post-400-status-code-warn:
  description: Warn 400 status code for POST response.
  message: 400 Status Code for POST Responses
  severity: warn
  given: $.paths.*.post.responses
  then:
    field: '400'
    function: truthy
---