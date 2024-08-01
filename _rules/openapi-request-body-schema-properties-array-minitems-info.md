---
openapi-request-body-schema-properties-array-minitems-info:
  description: Has schema property array minItems.
  message: Request Body Schema Property Array MinItems
  severity: info
  given: $.paths.*.*.requestBody.content.*.schema.properties.[?(@.type=="array")]
  then:
    - field: minItems
      function: falsy
---