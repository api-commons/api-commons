---
name: JSON Schema Draft 2020-12 Properties Array Minitems Info
description: >-
  Schema properties that are of the type array should have a min items property
  defined
message: Schema Array Properties Have Min Items
given: $.properties[?(@.type=="array")]
severity: info
tags:
  - JSON Schema
  - Schema
  - Properties
  - Types
view_sort: HA
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-array-minitems-info:
    description: >-
      Schema properties that are of the type array should have a min items
      property defined
    message: Schema Array Properties Have Min Items
    severity: info
    given: $.properties[?(@.type=="array")]
    then:
      - field: minItems
        function: falsy
slug: json-schema-2020-12-properties-array-minitems-info
---