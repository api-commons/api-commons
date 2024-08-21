---
apis-json-apis-properties-postman-collection-info:
  description: API Properties Postman Collection
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