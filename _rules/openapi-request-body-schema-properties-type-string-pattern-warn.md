---
openapi-request-body-schema-properties-type-string-pattern-warn:
  description: Warn request body request body schema properties type string pattern.
  message: Request Body Schema Properties Type String Pattern
  given:
    - $.paths.*.*.requestBody.content.*.schema.properties.[?(@.type=='string')]
  severity: warn
  then:
    field: pattern
    function: truthy
---