---
openapi-tags-description-info:
  description: Has tag descriptions.
  message: Tag Descriptions
  given: $.tags[*]
  severity: info
  then:
    field: description
    function: falsy
---