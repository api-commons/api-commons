---
apis-json-image-positive:
  description: Image of APIs.json
  message: There is an image.
  given: $
  severity: info
  then:
    field: image
    function: falsy
---