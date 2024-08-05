---
openapi-info-license-identifier-cc-by-nc-sa-info:
  description: Has info license identifier.
  message: Info License identifier
  given: $.info.license
  severity: info
  then:
    field: identifier
    function: pattern
    functionOptions:
      match: ^\b(CC-BY-NC-SA-4.0)\b
---