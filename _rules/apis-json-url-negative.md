---
apis-json-url-negative:
  description: URL for APIs.json
  message: There MUST be a URL.
  given: $
  severity: error
  then:
    field: url
    function: truthy
---