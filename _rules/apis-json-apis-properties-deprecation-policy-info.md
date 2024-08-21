---
apis-json-apis-properties-deprecation-policy-info:
  description: API Properties Deprecation Policy
  message: >-
    Offering a deprecation policy page helping ensure consumers are aware of the deprecation strategy surrounding using an API, and how long it will be available for use.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-deprecation-policy|deprecation-policy|Deprecation|Deprecation Policy|DeprecationPolicy)\b
---