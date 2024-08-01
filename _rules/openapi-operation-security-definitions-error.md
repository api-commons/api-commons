---
openapi-operation-security-definitions-error:
  description: Require operation security definition.
  message: Operation Security Definition
  severity: error
  given: $.paths.*[get,post,patch,put,delete]
  then:
    field: security
    function: truthy
---