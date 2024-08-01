---
openapi-no-api-in-path-info:
  description: Has no api in path.
  message: No API in Path
  severity: info
  given: $.paths.*~
  then:
    function: pattern
    functionOptions:
      notMatch: \b(API|api)\b
---