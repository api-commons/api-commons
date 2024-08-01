---
openapi-info-title-length-error:
  description: Info title length is 50.
  message: Info Title Length
  severity: error
  given: $.info
  then:
    field: title
    function: length
    functionOptions:
      max: 50
---