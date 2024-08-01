---
apis-json-maintainers-negative:
  description: Maintainers for APIs.json
  message: There MUST be a maintainer object.
  given: $
  severity: error
  then:
    field: maintainers
    function: truthy
---