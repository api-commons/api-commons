---
openapi-operations-tags-one-error:
  description: Has one operation tags.
  message: One Operation Tags
  given: $.paths.*[get,post,patch,put,delete]
  severity: error
  then:
    field: tags
    function: length
    functionOptions:
      min: 1
---