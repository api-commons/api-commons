---
openapi-info-title-upper-case-info:
  description: Has info title upper case.
  message: Info Title Upper Case
  severity: info
  given: $.info.title
  then:
    function: pattern
    functionOptions:
      notMatch: '[A-Z]\w*'
---