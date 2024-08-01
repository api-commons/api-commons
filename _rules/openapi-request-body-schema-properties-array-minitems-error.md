---
openapi-request-body-schema-properties-array-minitems-error:
  description: Require request body schema property array minItems.
  message: Request Body Schema Property Array MinItems
  severity: error
  given: $.paths.*.*.requestBody.content.*.schema.properties.[?(@.type=="array")]
  then:
    - field: minItems
      function: truthy
---