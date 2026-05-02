---
name: JSON Schema Draft 2020-12 Properties String Maxlength Info
description: >-
  Schema properties that are of the string type have the max length applied
  defining the shape of the property
message: Schema String Properties Has Maximum Length
given: $properties[?(@.type == 'string')]
severity: info
tags:
  - JSON Schema
  - Schema
  - Properties
  - Types
view_sort: F
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-string-maxlength-info:
    description: >-
      Schema properties that are of the string type have the max length applied
      defining the shape of the property
    message: Schema String Properties Has Maximum Length
    severity: info
    given: $properties[?(@.type == 'string')]
    then:
      field: maxLength
      function: falsy
slug: json-schema-2020-12-properties-string-maxlength-info
---