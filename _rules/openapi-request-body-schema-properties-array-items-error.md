---
openapi-request-body-schema-properties-array-items-error:
  description: Require request body schema property array items.
  message: Request Body Schema Property Array Items
  severity: error
  given: $.paths.*.*.requestBody.content.*.schema.properties.[?(@.type=="array")]
  then:
    field: items
    function: truthy
---