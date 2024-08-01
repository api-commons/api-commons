---
apis-json-tags-upper-case-info:
  description: Upper Case Tag for APIs/json
  message: Tags Upper Case
  severity: info
  given: $.tags.*
  then:
    function: pattern
    functionOptions:
      notMatch: '[A-Z]\w*'
---