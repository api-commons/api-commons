---
openapi-operations-description-length-error:
  description: Require operation description length 250.
  message: Operation Description Length
  given: $.paths.*[get,post,patch,put,delete]
  then:
    - field: description
      function: length
      functionOptions:
        max: 250
---