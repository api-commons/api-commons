---
apis-json-apis-properties-security-info:
  description: API Properties Security
  message: >-
    Offering information regarding the security of an API, making available processes, tests, results, and the other evidence of API security.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(Security|SecurityTesting)\b
---