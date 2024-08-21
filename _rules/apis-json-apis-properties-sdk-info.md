---
apis-json-apis-properties-sdk-info:
  description: API Properties SDK
  message: Has an SDK.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(sdk|sdks|SDKs)\b
---