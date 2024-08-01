---
openapi-info-description-length-error:
  description: Info description length.
  message: Info Description Length
  severity: error
  given: $.info
  then:
    field: description
    function: length
    functionOptions:
      max: 500
---