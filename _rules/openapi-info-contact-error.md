---
openapi-info-contact-error:
  description: Requires contact object.
  message: Contact Object
  severity: error
  given: $.info
  then:
    field: contact
    function: truthy
---