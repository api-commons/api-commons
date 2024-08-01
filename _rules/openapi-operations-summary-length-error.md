---
openapi-operations-summary-length-error:
  description: Operation summary length 50.
  message: Operation Summary Length
  given: $.paths.*[get,post,patch,put,delete]
  then:
    - field: summary
      function: length
      functionOptions:
        max: 50
  type: style
---