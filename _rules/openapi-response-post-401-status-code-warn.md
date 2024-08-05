---
openapi-response-post-401-status-code-warn:
  description: Warn 401 status code for POST response.
  message: 401 Status Code for POST Responses
  severity: warn
  given: $.paths.*.post.responses
  then:
    field: "401"
    function: truthy
---