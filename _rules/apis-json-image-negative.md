---
apis-json-image-negative:
  description: Image of APIs.json
  message: There MUST be an image.
  given: $
  severity: error
  then:
    field: image
    function: truthy
---