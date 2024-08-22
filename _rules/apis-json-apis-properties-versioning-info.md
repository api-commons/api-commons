---
apis-json-apis-properties-versioning-info:
  description: API Properties Versioning
  message: >-
    Providing an overview of how an API is version, providing details on semantic or date-based versioning, helping consumers understand more about change management in place.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(Versions|Versioning)\b
---