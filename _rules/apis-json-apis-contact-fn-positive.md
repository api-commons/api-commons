---
apis-json-apis-contact-fn-positive:
  description: Contact FN for API
  message: API contact has FN.
  given: $.apis.*.contact.*
  severity: info
  then:
    field: FN
    function: falsy
---