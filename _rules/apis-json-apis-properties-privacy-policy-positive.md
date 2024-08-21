---
apis-json-apis-properties-legal-privacy-policy-positive:
  description: API Properties Legal Privacy Policy
  message: >-
    Offering a dedicated privacy policy page helps ensure consumers are aware of
    the privacy requirements surrounding using an API.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-privacy-policy|privacy-policy|Privacy|Privacy Policy)\b
---