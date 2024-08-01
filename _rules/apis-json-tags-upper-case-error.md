---
apis-json-tags-upper-case-error:
  description: Upper Case Tag for APIs/json
  message: Tags Upper Case
  severity: error
  given: $.tags.*
  then:
    function: pattern
    functionOptions:
      match: '[A-Z]\w*'
---