---
openapi-operations-tags-error:
  description: Require operation tags.
  message: Operation Tags
  severity: error
  given: $.paths.*[get,post,patch,put,delete]
  then:
    - field: tags
      function: truthy
---