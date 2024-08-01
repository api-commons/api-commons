---
openapi-response-post-201-status-code-error:
  description: Require 201 status code for POST responses.
  message: POST 201 Status Code
  severity: error
  given: $.paths[*].post.responses
  then:
    field: '201'
    function: truthy
---