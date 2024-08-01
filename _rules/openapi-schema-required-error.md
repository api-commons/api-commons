---
openapi-schema-required-error:
  description: Require schema required.
  message: Schema Required
  severity: error
  given: $.components.schemas.[?(@.type=="object")]
  then:
    field: required
    function: truthy
---