---
apis-json-apis-properties-support-email-info:
  description: API Properties Email email
  message: >-
    Offering a dedicated email channel for your API makes it very simple for
    consumers to get the support they need when using your API.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(email|Email)\b
---