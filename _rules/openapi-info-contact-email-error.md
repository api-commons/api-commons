---
openapi-info-contact-email-error:
  description: Requires contact email.
  message: Contact Email
  given: $.info.contact
  severity: error
  then:
    field: email
    function: truthy
---