---
openapi-info-contact-name-info:
  description: Has contact name.
  message: Contact Name
  given: $.info.contact
  severity: info
  then:
    field: name
    function: falsy
---