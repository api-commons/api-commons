---
openapi-request-body-schema-properties-enum-casing-error:
  description: Require request body schema property enum casing.
  message: Request Body Schema Property Enum Casing
  severity: error
  given: $.paths.*.*.requestBody.content.*.schema.properties.*.enum.*
  then:
    function: pattern
    functionOptions:
      match: ^[A-Z]+(?:_[A-Z]+)*$
---