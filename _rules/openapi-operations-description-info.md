---
openapi-operations-description-info:
  description: Has operation description.
  message: Operation Description
  severity: info
  given: $.paths.*[get,post,patch,put,delete]
  then:
    - field: description
      function: falsy
---