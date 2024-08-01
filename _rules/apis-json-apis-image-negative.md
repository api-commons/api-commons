---
apis-json-apis-image-negative:
  description: Image of APIs
  message: APIs MUST have an image.
  given: $.apis.*
  severity: error
  then:
    field: image
    function: truthy
---