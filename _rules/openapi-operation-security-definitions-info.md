---
openapi-operation-security-definitions-info:
  description: Has operation security definition.
  message: Operation Security Definition
  severity: info
  given: $.paths.*[get,post,patch,put,delete]
  then:
    field: security
    function: falsy
---