---
openapi-tags-one-error:
  description: Require One Tag
  message: One Tag
  given: $
  severity: error
  then:
    field: tags
    function: length
    functionOptions:
      min: 1
---