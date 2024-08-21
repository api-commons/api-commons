---
apis-json-apis-properties-rate-limits-info:
  description: API Properties Rate Limits
  message: Offers details regarding rate limits in place against an API as well as the wider platform around it, helping consumers understand the limitations of API integration.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(rate-limits|RateLimits|Rate Limits)\b
---