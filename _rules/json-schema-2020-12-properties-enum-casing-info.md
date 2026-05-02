---
name: JSON Schema Draft 2020-12 Properties Enum Casing Info
description: >-
  Schema property enumerators are consistent casing, keeping all entries upper
  snake case, and consistent across all APIs
message: Schema Property Enum Are Upper Snake Case
given: $.properties.*.enum.*
severity: error
tags:
  - JSON Schema
  - Schema
  - Properties
  - Enumerators
view_sort: J
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-enum-casing-info:
    description: >-
      Schema property enumerators are consistent casing, keeping all entries
      upper snake case, and consistent across all APIs
    message: Schema Property Enum Are Upper Snake Case
    severity: error
    given: $.properties.*.enum.*
    then:
      function: pattern
      functionOptions:
        notMatch: ^[A-Z]+(?:_[A-Z]+)*$
slug: json-schema-2020-12-properties-enum-casing-info
---