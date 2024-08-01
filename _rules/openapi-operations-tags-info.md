---
openapi-operations-tags-info:
  description: Has operation tags.
  message: Operation Tags
  severity: info
  given: $.paths.*[get,post,patch,put,delete]
  then:
    - field: tags
      function: falsy
---