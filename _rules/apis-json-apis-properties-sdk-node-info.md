---
apis-json-apis-properties-sdk-node-info:
  description: API Properties SDK Node
  message: >-
    Offering a Node SDK for consumers to use will save them time when it comes
    to onboarding and integrating an API into their applications.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-sdk-node)\b
---