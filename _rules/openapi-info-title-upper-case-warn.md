---
openapi-info-title-upper-case-warn:
  description: Warn info title upper case.
  message: Info Title Upper Case
  severity: warn
  given: $.info.title
  then:
    function: pattern
    functionOptions:
      match: '[A-Z]\w*'
---