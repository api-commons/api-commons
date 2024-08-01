---
openapi-schema-required-info:
  description: Has schema required.
  message: Schema Required
  severity: info
  given: $.components.schemas.[?(@.type=="object")]
  then:
    field: required
    function: falsy
---