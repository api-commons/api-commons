---
apis-json-apis-properties-communications-video-positive:
  description: API Properties Use Cases
  message: >-
    Providing a list of use cases for an API, defining the who, what, how, and why of API consumption, helping map to operations.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(UseCases)\b
---