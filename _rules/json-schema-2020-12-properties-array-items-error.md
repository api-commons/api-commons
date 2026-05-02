---
name: JSON Schema Draft 2020-12 Properties Array Items Error
description: >-
  Schema properties that are of the type array must have an items property
  defined
message: Schema Array Properties MUST Have Items
given: $.properties[?(@.type=="array")]
severity: error
tags:
  - JSON Schema
  - Schema
  - Properties
  - Types
view_sort: H
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-array-items-error:
    description: >-
      Schema properties that are of the type array must have an items property
      defined
    message: Schema Array Properties MUST Have Items
    severity: error
    given: $.properties[?(@.type=="array")]
    then:
      field: items
      function: truthy
slug: json-schema-2020-12-properties-array-items-error
---