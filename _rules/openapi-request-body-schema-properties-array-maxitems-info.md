---
openapi-request-body-schema-properties-array-maxitems-info:
  description: Has schema property array maxItems.
  message: Request Body Schema Property Array MaxItems
  severity: info
  given: $.paths.*.*.requestBody.content.*.schema.properties.[?(@.type=="array")]
  then:
    - field: maxItems
      function: truthy
---