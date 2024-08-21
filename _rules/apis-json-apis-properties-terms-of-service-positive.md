---
apis-json-apis-properties-legal-terms-of-service-positive:
  description: API Properties Terms of Service
  message: >-
    Offering a dedicated terms of service page helps ensure consumers are aware
    of what is expected when it comes to using a service.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-terms-of-service|terms-of-service|Terms of Service|TOS|TermsOfService)\b
---