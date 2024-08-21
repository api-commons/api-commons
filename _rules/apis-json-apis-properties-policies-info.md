---
apis-json-apis-properties-policies-info:
  description: API Properties Policies
  message: Has a policies page.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-policies|Policies)\b
---