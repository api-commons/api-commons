---
name: JSON Schema Draft 2020-12 Properties String Minlength Error
description: >-
  Schema properties that are of the string type have the min length applied
  defining the shape of the property
message: Schema String Properties MUST Have Minimum Length
given: $properties[?(@.type == 'string')]
severity: error
tags:
  - JSON Schema
  - Schema
  - Properties
  - Types
view_sort: E
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-string-minlength-error:
    description: >-
      Schema properties that are of the string type have the min length applied
      defining the shape of the property
    message: Schema String Properties MUST Have Minimum Length
    severity: error
    given: $properties[?(@.type == 'string')]
    then:
      field: minLength
      function: truthy
slug: json-schema-2020-12-properties-string-minlength-error
---