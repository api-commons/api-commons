---
openapi-schema-enum-info:
  description: Schema has enum
  message: Schema Enum
  severity: info
  given: $.components.schemas.*
  then:
    - field: enum
      function: falsy
---