---
apis-json-apis-contact-email-positive:
  description: Contact email for API
  message: API contact has email.
  given: $.apis.*.contact.*
  severity: info
  then:
    field: email
    function: falsy
---