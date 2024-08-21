---
apis-json-apis-properties-license-info:
  description: API Properties Legal License
  message: >-
    Offering a dedicated licensing page helps ensure consumers are aware of the
    licensing for an API, SDKs, and other supporting resources.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-license|License|license|InterfaceLicense)\b
---