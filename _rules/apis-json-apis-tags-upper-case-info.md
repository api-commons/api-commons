---
apis-json-apis-tags-upper-case-info:
  description: Upper Case Tag for API
  message: API Tags Upper Case
  severity: info
  given: $.apis.*.tags.*
  then:
    function: pattern
    functionOptions:
      notMatch: '[A-Z]\w*'
---