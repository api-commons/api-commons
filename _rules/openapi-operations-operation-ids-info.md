---
openapi-operations-operation-ids-info:
  description: Has operation id.
  message: Operation ID.
  severity: info
  given: $.paths.*[get,post,patch,put,delete]
  then:
    - field: operationId
      function: falsy
---