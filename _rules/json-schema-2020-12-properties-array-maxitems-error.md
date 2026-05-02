---
name: JSON Schema Draft 2020-12 Properties Array Maxitems Error
description: >-
  Schema properties that are of the type array should have a max items property
  defined
message: Schema Array Properties MUST Have Max Items
given: $.properties[?(@.type=="array")]
severity: error
tags:
  - JSON Schema
  - Schema
  - Properties
  - Types
view_sort: HB
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-array-maxitems-error:
    description: >-
      Schema properties that are of the type array should have a max items
      property defined
    message: Schema Array Properties MUST Have Max Items
    severity: error
    given: $.properties[?(@.type=="array")]
    then:
      - field: maxItems
        function: truthy
slug: json-schema-2020-12-properties-array-maxitems-error
---