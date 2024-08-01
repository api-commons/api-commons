---
openapi-request-body-schema-properties-string-maxlength-error:
  message: Require request body schema property string maxlength.
  description: Request Body Schema Property String MaxLength
  severity: error
  given: $.paths.*.*.requestBody.content.*.schema.properties.[?(@.type=="string")]
  then:
    field: maxLength
    function: truthy
---