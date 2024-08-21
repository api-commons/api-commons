---
apis-json-apis-properties-documentation-info:
  description: API Properties Documentation
  message: There is a documentation property.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(documentation|Documentation)\b
---