---
apis-json-tags-one-negative:
  description: One Tag for APIs.json
  message: There MUST be at least one tag.
  given: $
  severity: error
  then:
    field: tags
    function: length
    functionOptions:
      min: 1
---