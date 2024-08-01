---
openapi-parameters-schema-type-string-minlength-warn:
  description: Warn parameter schema type string minlength.
  message: Parameter Schema Type String MinLength
  given:
    - $.paths.*.*.parameters.[?(@.type=='string')]
  severity: warn
  then:
    field: minLength
    function: truthy
---