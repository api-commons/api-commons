---
openapi-operations-operation-ids-error:
  description: Require operation id.
  message: Operation ID.
  severity: error
  given: $.paths.*[get,post,patch,put,delete]
  then:
    - field: operationId
      function: truthy
---