---
openapi-schema-properties-enum-info:
  description: Has schema property enum.
  message: Schema Property Enum
  severity: info
  given:
    - $.components.schemas.*.properties.*
    - $.components.schemas.*.properties.*.properties.*
    - $.components.schemas.*.properties.*.properties.*.properties.*
  then:
    - field: enum
      function: falsy
---