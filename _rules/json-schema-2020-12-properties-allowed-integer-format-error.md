---
name: JSON Schema Draft 2020-12 Properties Allowed Integer Format Error
description: >-
  Schema integer properties should have a format property with int32 or int64
  applied
message: Type Format MUST Be int32 or int64.
given: $.properties[?(@.type=="integer")]
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
  json-schema-2020-12-properties-allowed-integer-format-error:
    description: >-
      Schema integer properties should have a format property with int32 or
      int64 applied
    message: Type Format MUST Be int32 or int64.
    severity: hint
    given: $.properties[?(@.type=="integer")]
    then:
      field: format
      function: enumeration
      functionOptions:
        values:
          - int32
          - int64
slug: json-schema-2020-12-properties-allowed-integer-format-error
---