---
apis-json-apis-tags-upper-case-error:
  description: Upper Case Tag for API
  message: API Tags Upper Case
  severity: error
  given: $.apis.*.tags.*
  then:
    function: pattern
    functionOptions:
      match: '[A-Z]\w*'
---