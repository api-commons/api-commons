---
openapi-tags-description-error:
  description: Require tag descriptions.
  message: Tag Descriptions
  given: $.tags[*]
  severity: error
  then:
    field: description
    function: truthy
---