---
apis-json-apis-properties-environments-sandbox-positive:
  description: API Properties Environments Sandbox
  message: Has a sandbox.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-environment-sandbox)\b
---