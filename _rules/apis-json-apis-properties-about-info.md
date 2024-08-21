---
apis-json-apis-properties-about-info:
  description: API Properties About
  message: Has an about property.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(about|About)\b
---