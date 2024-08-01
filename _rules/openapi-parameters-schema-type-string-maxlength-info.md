---
openapi-parameters-schema-type-string-maxlength-info:
  description: Has parameter schema type string maxlength.
  message: Parameter Schema Type String MaxLength
  given:
    - $.paths.*.*.parameters.[?(@.type=='string')]
  severity: info
  then:
    field: maxLength
    function: falsy
---