---
openapi-info-contact-name-error:
  description: Requires contact email.
  message: Contact Name
  given: $.info.contact
  severity: error
  then:
    field: name
    function: truthy
---