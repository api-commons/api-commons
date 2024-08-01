---
apis-json-apis-image-positive:
  description: Image of APIs
  message: API has an image.
  given: $.apis.*
  severity: info
  then:
    field: image
    function: falsy
---