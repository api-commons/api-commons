---
openapi-schema-properties-string-minlength-error:
  message: Require schema property string minlength.
  description: Schema Property String MinLength
  severity: error
  given: $.components.schemas.*.properties.[?(@.type=="string")]
  then:
    field: minLength
    function: truthy
---