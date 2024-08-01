---
apis-json-apis-contact-negative:
  description: Contact for API
  message: API COULD have a contact.
  severity: warn
  given:
    - $.apis.*
  then:
    field: contact
    function: truthy
---