---
apis-json-apis-properties-environments-production-positive:
  description: API Properties Environments Production
  message: >-
    Offering a production environment makes it easy for consumers to access the
    details they need to work with an API in production.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-environment-production)\b
---