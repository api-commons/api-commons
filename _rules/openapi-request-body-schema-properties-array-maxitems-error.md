---
openapi-request-body-schema-properties-array-maxitems-error:
  description: Require request body schema property array maxItems.
  message: Request Body Schema Property Array MaxItems
  severity: error
  given: $.paths.*.*.requestBody.content.*.schema.properties.[?(@.type=="array")]
  then:
    - field: maxItems
      function: truthy
---