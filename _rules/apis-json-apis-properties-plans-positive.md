---
apis-json-apis-properties-management-plans-positive:
  description: API Properties Plans
  message: Has a plans page.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-plans|Plans)\b
---