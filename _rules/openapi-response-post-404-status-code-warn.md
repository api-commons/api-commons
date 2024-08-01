---
openapi-response-post-404-status-code-warn:
  description: Warn 404 status code for POST response.
  message: 404 Status Code for POST Responses
  severity: warn
  given: $.paths.*.post.responses
  then:
    field: '404'
    function: truthy
---