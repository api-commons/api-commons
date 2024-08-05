---
openapi-info-license-identifier-cc-by-nc-sa-error:
  description: Require info license identifier.
  message: Info License identifier
  given: $.info.license
  severity: error
  then:
    field: identifier
    function: pattern
    functionOptions:
      match: ^\b(CC-BY-NC-SA-4.0)\b
---