---
apis-json-apis-properties-performance-positive:
  description: API Properties Performance
  message: >-
    Offering information regarding the performance of an API, making available processes, tests, results, and the other evidence of API performance.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(Performance|PerformanceTesting)\b
---