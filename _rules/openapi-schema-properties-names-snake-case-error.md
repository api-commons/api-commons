---
openapi-schema-properties-names-snake-case-error:
  description: Schema properties are snake case.
  message: Schema properties names MUST be snake case.
  severity: warn
  given: $.components.schemas.*.properties
  then:
    field: "@key"
    function: pattern
    functionOptions:
      match: "[a-z0-9]+(?:_[a-z0-9]+)*"
---