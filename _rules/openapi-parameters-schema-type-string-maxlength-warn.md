---
openapi-parameters-schema-type-string-maxlength-warn:
  description: Warn parameter schema type string maxlength.
  message: Parameter Schema Type String MaxLength
  given:
    - $.paths.*.*.parameters.[?(@.type=='string')]
  severity: warn
  then:
    field: maxLength
    function: truthy
---