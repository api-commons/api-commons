---
openapi-tags-name-info:
  description: Has tag name.
  message: Tag Name
  given: $.tags[*]
  severity: info
  then:
    field: name
    function: falsy
---