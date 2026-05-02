---
name: JSON Schema Draft 2020-12 Properties String Maxlength Error
description: >-
  Schema properties that are of the string type have the max length applied
  defining the shape of the property
message: Schema String Properties MUST Have Maximum Length
given: $properties[?(@.type == 'string')]
severity: error
tags:
  - JSON Schema
  - Schema
  - Properties
  - Types
view_sort: F
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-string-maxlength-error:
    description: >-
      Schema properties that are of the string type have the max length applied
      defining the shape of the property
    message: Schema String Properties MUST Have Maximum Length
    severity: error
    given: $properties[?(@.type == 'string')]
    then:
      field: maxLength
      function: truthy
slug: json-schema-2020-12-properties-string-maxlength-error
---