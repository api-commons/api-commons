---
apis-json-apis-contact-email-negative:
  description: Contact email for API
  message: API contact COULD have email.
  given: $.apis.*.contact.*
  severity: error
  then:
    field: email
    function: truthy
---