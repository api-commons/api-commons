---
openapi-schema-properties-string-maxlength-error:
  message: Require schema property string maxlength.
  description: Schema Property String MaxLength
  severity: error
  given: $.components.schemas.*.properties.[?(@.type=="string")]
  then:
    field: maxLength
    function: truthy
---