---
name: JSON Schema Draft 2020-12 Properties Enum Info
description: >-
  Schema property has enumerators, providing consistent values chosen by
  consumers when making requests
message: Schema Property Have Enum
given: $.properties.*
severity: info
tags:
  - JSON Schema
  - Schema
  - Properties
  - Enumerators
view_sort: I
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-enum-info:
    description: >-
      Schema property has enumerators, providing consistent values chosen by
      consumers when making requests
    message: Schema Property Have Enum
    severity: info
    given: $.properties.*
    then:
      - field: enum
        function: falsy
slug: json-schema-2020-12-properties-enum-info
---