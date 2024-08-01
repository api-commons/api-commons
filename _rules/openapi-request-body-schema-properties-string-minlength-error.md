---
openapi-request-body-schema-properties-string-minlength-error:
  message: Require request body schema property string minlength.
  description: Request Body Schema Property String MinLength
  severity: error
  given: $.paths.*.*.requestBody.content.*.schema.properties.[?(@.type=="string")]
  then:
    field: minLength
    function: truthy
---