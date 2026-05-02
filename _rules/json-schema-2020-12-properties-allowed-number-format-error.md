---
name: JSON Schema Draft 2020-12 Properties Allowed Number Format Error
description: >-
  Schema integer properties should have a format property with int32 or int64
  applied
message: Schema Properties MUST Have Format
given: $.properties[?(@.type=="number")]
severity: hint
tags:
  - JSON Schema
  - Schema
  - Properties
  - Types
view_sort: G
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-allowed-number-format-error:
    description: >-
      Schema integer properties should have a format property with int32 or
      int64 applied
    message: Schema Properties MUST Have Format
    severity: hint
    given: $.properties[?(@.type=="number")]
    then:
      field: format
      function: enumeration
      functionOptions:
        values:
          - decimal32
          - decimal64
          - float
          - double
          - decimal128
slug: json-schema-2020-12-properties-allowed-number-format-error
---