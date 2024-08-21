---
apis-json-apis-properties-support-issues-info:
  description: API Properties Support Issues
  message: >-
    Offering a support using GitHub issues offers an easy way to encourage
    consumers to submit issues and communicate in a self-service way.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(issues|x-issues|Issues)\b
---