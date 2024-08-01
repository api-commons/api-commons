---
openapi-schema-properties-error:
  description: Require schema properties.
  message: Schema Properties
  severity: error
  given: $.components.schemas.[?(@.type=="object")]
  then:
    field: properties
    function: truthy
---