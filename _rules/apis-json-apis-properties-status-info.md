---
apis-json-apis-properties-status-info:
  description: API Properties Status
  message: Has an status page.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(x-status|status|Status|StatusPage)\b
---