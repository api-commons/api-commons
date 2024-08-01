---
openapi-request-body-schema-properties-define-number-maximum-error:
  description: Require request body schema property number minimum.
  message: Request Body Schema Property Number Minimum
  severity: error
  given: $.paths.*.*.requestBody.content.*.schema.properties.[?(@.type=="number")]
  then:
    - field: maximum
      function: defined
---