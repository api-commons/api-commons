---
openapi-operations-summary-info:
  description: Has operation summary.
  message: Operation Summary
  severity: info
  given: $.paths.*[get,post,patch,put,delete]
  then:
    - field: summary
      function: falsy
---