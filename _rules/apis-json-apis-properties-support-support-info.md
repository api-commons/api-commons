---
apis-json-apis-properties-support-support-info:
  description: API Properties Support Support
  message: >-
    Offering a formal support page and channel helps make it easy for consumers
    to find the help they need with putting aPIs to work.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(support|Support)\b
---