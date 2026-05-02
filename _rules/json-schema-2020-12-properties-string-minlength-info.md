---
name: JSON Schema Draft 2020-12 Properties String Minlength Info
description: >-
  Schema properties that are of the string type have the min length applied
  defining the shape of the property
message: Schema String Properties Has Minimum Length
given: $properties[?(@.type == 'string')]
severity: info
tags:
  - JSON Schema
  - Schema
  - Properties
  - Types
view_sort: E
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-string-minlength-info:
    description: >-
      Schema properties that are of the string type have the min length applied
      defining the shape of the property
    message: Schema String Properties Has Minimum Length
    severity: info
    given: $properties[?(@.type == 'string')]
    then:
      field: minLength
      function: falsy
slug: json-schema-2020-12-properties-string-minlength-info
---