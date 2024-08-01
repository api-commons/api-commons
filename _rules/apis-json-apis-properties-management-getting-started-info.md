---
apis-json-apis-properties-management-getting-started-info:
  description: API Properties Management Getting Started
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