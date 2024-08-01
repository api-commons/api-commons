---
openapi-request-body-schema-properties-allowed-number-format-error:
  description: Require request body schema property number formats.
  message: Request Body Schema Property Number Formats
  severity: hint
  given: $.paths.*.*.requestBody.content.*.schema.properties.[?(@.type=="number")]
  then:
    field: format
    function: enumeration
    functionOptions:
      values:
        - decimal32
        - decimal64
        - float
        - double
        - decimal128
---