---
apis-json-apis-properties-rules-info:
  description: API Properties Rules
  message: Has a rules page.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-rules|Rules)\b
---