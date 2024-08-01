---
openapi-no-api-in-path-error:
  description: Require no api in path.
  message: No API in Path
  severity: error
  given: $.paths.*~
  then:
    function: pattern
    functionOptions:
      match: ^\b(API|api)\b
---