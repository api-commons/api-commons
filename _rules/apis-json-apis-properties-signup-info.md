---
apis-json-apis-properties-signup-info:
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
        notMatch: \b(X-signup|signup|Sign Up|SignUp|Signup)\b
---