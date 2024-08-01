---
apis-json-apis-properties-sdk-go-positive:
  description: API Properties SDK Go
  message: >-
    Offering a Go SDK for consumers to use will save them time when it comes to
    onboarding and integrating an API into their applications.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-sdk-go)\b
---