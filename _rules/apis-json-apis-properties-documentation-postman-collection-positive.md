---
apis-json-apis-properties-documentation-postman-collection-positive:
  description: API Properties Documentation Postman Collection
  message: Has a Postman Collection.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(PostmanCollection)\b
---