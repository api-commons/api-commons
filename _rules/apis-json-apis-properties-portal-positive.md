---
apis-json-apis-properties-portal-positive:
  description: API Properties Portal
  message: Has a portal
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-developer-portal|developer-portal|portal|Portal|Portals)\b
---