---
apis-json-maintainers-fn-negative:
  description: Maintainers for APIs.json
  message: There MUST be a FN property for maintainers.
  given: $.maintainers.*
  severity: error
  then:
    field: FN
    function: truthy
---