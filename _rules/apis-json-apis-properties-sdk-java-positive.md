---
apis-json-apis-properties-sdk-java-positive:
  description: API Properties Java Node
  message: >-
    Offering a Java SDK for consumers to use will save them time when it comes
    to onboarding and integrating an API into their applications.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-sdk-java)\b
---