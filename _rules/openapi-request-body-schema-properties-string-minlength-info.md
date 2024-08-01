---
openapi-request-body-schema-properties-string-minlength-info:
  message: Has schema property string minlength.
  description: Request Body Schema Property String MinLength
  severity: info
  given: $.paths.*.*.requestBody.content.*.schema.properties.[?(@.type=="string")]
  then:
    field: minLength
    function: falsy
---