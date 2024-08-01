---
openapi-request-body-schema-properties-string-maxlength-info:
  message: Has schema property string maxlength.
  description: Request Body Schema Property String MaxLength
  severity: info
  given: $.paths.*.*.requestBody.content.*.schema.properties.[?(@.type=="string")]
  then:
    field: maxLength
    function: falsy
---