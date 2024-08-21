---
apis-json-apis-properties-getting-started-info:
  description: API Properties Getting Started
  message: Has a getting started.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(GettingStarted)\b
---