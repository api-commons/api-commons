---
apis-json-apis-properties-management-plans-positive:
  description: API Properties Management Plans
  message: Has a plans page.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-plans)\b
---