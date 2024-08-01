---
apis-json-maintainers-positive:
  description: Maintainers for APIs.json
  message: There is a maintainer object.
  given: $
  severity: info
  then:
    field: maintainers
    function: falsy
---