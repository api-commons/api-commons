---
openapi-request-body-schema-properties-enum-casing-info:
  description: Has schema property enum casing.
  message: Request Body Schema Property Enum Casing
  severity: error
  given: $.paths.*.*.requestBody.content.*.schema.properties.*.enum.*
  then:
    function: pattern
    functionOptions:
      notMatch: ^[A-Z]+(?:_[A-Z]+)*$
---