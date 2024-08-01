---
apis-json-apis-contact-fn-negative:
  description: Contact FN for API
  message: API contact COULD have FN.
  given: $.apis.*.contact.*
  severity: error
  then:
    field: FN
    function: truthy
---