---
apis-json-apis-properties-sdk-python-positive:
  description: API Properties SDK Python
  message: >-
    Offering a Python SDK for consumers to use will save them time when it comes
    to onboarding and integrating an API into their applications.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-sdk-python)\b
---