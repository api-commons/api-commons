---
apis-json-apis-tags-one-negative:
  description: One Tag for API
  message: >-
    Having at least one tag for your APIs helps ensure that it will be more
    discoverable.
  given: $.apis.*
  severity: error
  then:
    field: tags
    function: length
    functionOptions:
      min: 1
---