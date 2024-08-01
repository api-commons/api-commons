---
openapi-parameters-schema-type-string-minlength-info:
  description: Has parameter schema type string minlength.
  message: Parameter Schema Type String MinLength
  given:
    - $.paths.*.*.parameters.[?(@.type=='string')]
  severity: info
  then:
    field: minLength
    function: falsy
---