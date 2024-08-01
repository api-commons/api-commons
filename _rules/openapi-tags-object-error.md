---
openapi-tags-object-error:
  description: Require tag object.
  message: Tag Object
  given: $
  severity: error
  then:
    field: tags
    function: truthy
---