---
apis-json-apis-properties-authentication-info:
  description: API Properties Authentication
  message: Has authentication.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(Authentication)\b
---