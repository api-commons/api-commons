---
apis-json-apis-properties-management-plans-positive:
  description: API Properties Pricing
  message: Has a pricing page.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(Pricing)\b
---