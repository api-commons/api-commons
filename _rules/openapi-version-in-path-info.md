---
openapi-version-in-path-info:
  description: Has no version in path.
  message: Version in Path
  severity: error
  given: $.paths[*]~
  then:
    function: pattern
    functionOptions:
      match: /((?:/)(v|version)?[0-9]{1,3}(?:/)?)/i
---