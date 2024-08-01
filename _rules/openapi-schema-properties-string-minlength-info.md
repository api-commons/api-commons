---
openapi-schema-properties-string-minlength-info:
  message: Has schema property string minlength.
  description: Schema Property String MinLength
  severity: info
  given: $.components.schemas.*.properties.[?(@.type=="string")]
  then:
    field: minLength
    function: falsy
---