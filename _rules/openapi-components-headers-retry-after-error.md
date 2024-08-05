---
openapi-components-headers-retry-after-error:
  description: Require components retry after header.
  message: Components MUST have a retry after headers.
  severity: error
  given: $.components.headers
  then:
    field: Retry-After
    function: truthy
---