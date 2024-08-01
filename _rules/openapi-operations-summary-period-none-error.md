---
openapi-operations-summary-period-none-error:
  description: Require no period on summary.
  message: Operation Summary Period
  severity: error
  given: $.paths[*][*].summary
  then:
    function: pattern
    functionOptions:
      notMatch: \.$
---