---
openapi-schema-properties-string-maxlength-info:
  message: Has schema property string maxlength.
  description: Schema Property String MaxLength
  severity: info
  given: $.components.schemas.*.properties.[?(@.type=="string")]
  then:
    field: maxLength
    function: falsy
---