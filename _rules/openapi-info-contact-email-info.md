---
openapi-info-contact-email-info:
  description: Has contact email.
  message: Contact Email
  given: $.info.contact
  severity: info
  then:
    field: email
    function: falsy
---