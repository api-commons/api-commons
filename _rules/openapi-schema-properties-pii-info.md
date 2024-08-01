---
openapi-schema-properties-pii-info:
  description: Has schema PII.
  message: Schema PII
  severity: info
  given: $.components.schemas.*.properties.*.*
  then:
    field: x-pii
    function: falsy
---