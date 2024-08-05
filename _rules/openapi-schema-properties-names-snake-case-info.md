---
openapi-schema-properties-names-snake-case-info:
  description: Schema properties are snake case.
  message: Schema property name is snake case.
  severity: info
  given: $.components.schemas.*.properties
  then:
    field: "@key"
    function: pattern
    functionOptions:
      notMatch: "[a-z0-9]+(?:_[a-z0-9]+)*"
---