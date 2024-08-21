---
apis-json-apis-properties-change-change-log-positive:
  description: API Properties Change Change Log
  message: Has change log.
  severity: info
  given:
    - $.apis.*.properties.*
    - $.common.*
  then:
    - field: type
      function: pattern
      functionOptions:
        notMatch: \b(api-change-log|change-log|Change Log|Changelog|ChangeLog)\b
---