---
apis-json-maintainers-email-positive:
  description: Maintainers Email
  message: There is a email property for maintainers.
  given: $.maintainers.*
  severity: info
  then:
    field: email
    function: falsy
---