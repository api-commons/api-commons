---
openapi-tags-name-error:
  description: Require tag name.
  message: Tag Name
  given: $.tags[*]
  severity: error
  then:
    field: name
    function: truthy
---