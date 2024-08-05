---
  openapi-operations-operation-ids-kebab-case-error:
    description: Require operation id kebab case.
    message: Operation ID Kebab Case
    given: $.paths.*[get,post,patch,put,delete].operationId
    then:
      function: casing
      functionOptions:
        type: kebab
---