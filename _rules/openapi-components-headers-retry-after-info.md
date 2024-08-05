---
openapi-components-headers-retry-after-info:
  description: Require components retry after header.
  message: Components has a retry after header.
  severity: info
  given: $.components.headers
  then:
    field: Retry-After
    function: falsy 
---