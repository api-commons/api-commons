---
openapi-request-body-schema-properties-allowed-integer-format-error:
  description: Requires integer properties to have a format of int32 or int64.
  message: Type format should be be int32 or int64.
  severity: hint
  given: $.paths.*.*.requestBody.content.*.schema.properties.[?(@.type=="integer")]
  then:
    field: format
    function: enumeration
    functionOptions:
      values:
        - int32
        - int64
---