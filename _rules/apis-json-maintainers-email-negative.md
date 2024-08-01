---
apis-json-maintainers-email-negative:
  description: Maintainers Email
  message: There MUST be an email property for maintainers.
  given: $.maintainers.*
  severity: error
  then:
    field: email
    function: truthy
---