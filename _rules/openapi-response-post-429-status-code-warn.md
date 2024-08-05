---
openapi-response-post-429-status-code-warn:
  description: Warn 429 status code for POST response.
  message: 429 Status Code for POST Responses
  severity: warn
  given: $.paths.*.post.responses
  then:
    field: "429"
    function: truthy
---