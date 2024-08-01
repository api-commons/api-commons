---
openapi-response-get-200-status-code-error:
  description: Ensures GET operations have a 200 status code response.
  message: A GET operation should have a 200 status code for the response.
  severity: error
  given: $.paths.*.get.responses
  then:
    field: '200'
    function: truthy
---