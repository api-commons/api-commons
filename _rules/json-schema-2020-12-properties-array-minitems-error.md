---
name: JSON Schema Draft 2020-12 Properties Array Minitems Error
description: >-
  Schema properties that are of the type array should have a min items property
  defined
message: Schema Array Properties MUST Have Min Items
given: $.properties[?(@.type=="array")]
severity: error
tags:
  - JSON Schema
  - Schema
  - Properties
  - Types
view_sort: HA
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-array-minitems-error:
    description: >-
      Schema properties that are of the type array should have a min items
      property defined
    message: Schema Array Properties MUST Have Min Items
    severity: error
    given: $.properties[?(@.type=="array")]
    then:
      - field: minItems
        function: truthy
slug: json-schema-2020-12-properties-array-minitems-error
---