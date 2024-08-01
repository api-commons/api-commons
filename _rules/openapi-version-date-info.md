---
openapi-version-date-info:
  description: Has date versioning.
  message: Date Versioning
  severity: info
  given: $.info.version
  then:
    function: pattern
    functionOptions:
      notMatch: ^([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))?$
---