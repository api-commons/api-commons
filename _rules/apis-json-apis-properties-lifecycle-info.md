---
apis-json-apis-properties-lifecycle-info:
  description: API Properties Lifecycle
  message: >-
    Providing an overview of how an API is version, providing details on semantic or date-based lifecycle, helping consumers understand more about change management in place.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(lifecycle|Lifecycle|Life Cycle)\b
---