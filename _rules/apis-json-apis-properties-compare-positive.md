---
apis-json-apis-properties-change-compare-positive:
  description: API Properties Change Compare
  message: Has API compare.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(compare|Compare)\b
---