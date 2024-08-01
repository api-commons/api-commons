---
apis-json-apis-contact-positive:
  description: Contact for API
  message: API has a contact.
  severity: info
  given:
    - $.apis.*
  then:
    field: contact
    function: falsy
---