---
openapi-schema-properties-allowed-number-format-error:
  description: Require schema property number formats.
  message: Schema Property Number Formats
  severity: hint
  given: $.components.schemas.*.properties.[?(@.type=="number")]
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