---
apis-json-apis-properties-management-signup-positive:
  description: API Properties Management Signup
  message: Has a sign up.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(X-signup|signup|Sign Up)\b
---