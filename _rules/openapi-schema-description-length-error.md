---
openapi-schema-description-length-error:
  description: All schemas descriptions should be shorter than 250 characters.
  message: Description needs to be less than 250 characters.
  severity: error
  given: $.components.schemas.*
  then:
    field: description
    function: length
    functionOptions:
      max: 250
---