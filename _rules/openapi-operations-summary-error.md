---
openapi-operations-summary-error:
  description: Require operation summary.
  message: Operation Summary
  severity: error
  given: $.paths.*[get,post,patch,put,delete]
  then:
    - field: summary
      function: truthy
---