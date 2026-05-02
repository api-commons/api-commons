---
name: JSON Schema Draft 2020-12 Properties Array Maxitems Info
description: >-
  Schema properties that are of the type array should have a max items property
  defined
message: Schema Array Properties Have Max Items
given: $.properties[?(@.type=="array")]
severity: info
tags:
  - JSON Schema
  - Schema
  - Properties
  - Types
view_sort: HB
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-array-maxitems-info:
    description: >-
      Schema properties that are of the type array should have a max items
      property defined
    message: Schema Array Properties Have Max Items
    severity: info
    given: $.properties[?(@.type=="array")]
    then:
      - field: maxItems
        function: truthy
slug: json-schema-2020-12-properties-array-maxitems-info
---