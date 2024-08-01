---
openapi-operations-operation-ids-camel-case-error:
  description: Require operation id camel case.
  message: Operation ID Camel Case
  given: $.paths.*[get,post,patch,put,delete].operationId
  then:
    function: casing
    functionOptions:
      type: camel
  type: style
---