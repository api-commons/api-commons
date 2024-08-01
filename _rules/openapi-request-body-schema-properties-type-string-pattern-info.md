---
openapi-request-body-schema-properties-type-string-pattern-info:
  description: Has request body request body schema properties type string pattern.
  message: Request Body Schema Properties Type String Pattern
  given:
    - $.paths.*.*.requestBody.content.*.schema.properties.[?(@.type=='string')]
  severity: info
  then:
    field: pattern
    function: falsy
---