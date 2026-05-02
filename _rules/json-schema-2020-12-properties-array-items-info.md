---
name: JSON Schema Draft 2020-12 Properties Array Items Info
description: >-
  Schema properties that are of the type array must have an items property
  defined
message: Schema Array Properties Has Items
given: $.properties[?(@.type=="array")]
severity: info
tags:
  - JSON Schema
  - Schema
  - Properties
  - Types
view_sort: H
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-array-items-info:
    description: >-
      Schema properties that are of the type array must have an items property
      defined
    message: Schema Array Properties Has Items
    severity: info
    given: $.properties[?(@.type=="array")]
    then:
      field: items
      function: falsy
slug: json-schema-2020-12-properties-array-items-info
---