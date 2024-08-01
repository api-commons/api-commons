---
apis-json-maintainers-fn-positive:
  description: Maintainers for APIs.json
  message: There is a FN property for maintainers.
  given: $.maintainers.*
  severity: info
  then:
    field: FN
    function: falsy
---