---
openapi-schema-properties-define-number-maximum-error:
  description: Require schema property number minimum.
  message: Schema Property Number Minimum
  severity: error
  given: $.components.schemas.*.properties.[?(@.type=="number")]
  then:
    - field: maximum
      function: defined
---