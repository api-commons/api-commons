---
openapi-operations-summary-period-none-info:
  description: Has no period on summary.
  message: Operation Summary Period
  severity: info
  given: $.paths[*][*].summary
  then:
    function: pattern
    functionOptions:
      match: \.$
---