---
openapi-operations-description-error:
  description: Require operation description.
  message: Operation Description
  severity: error
  given: $.paths.*[get,post,patch,put,delete]
  then:
    - field: description
      function: truthy
---