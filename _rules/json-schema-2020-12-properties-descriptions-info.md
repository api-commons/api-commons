---
name: JSON Schema Draft 2020-12 Properties Descriptions Info
description: >-
  Schema properties should have descriptions that provide a narrative of the
  property contains, and how it can be used
message: Schema Properties Have Description
given: $.properties[?(@.type == 'string')]
severity: info
tags:
  - JSON Schema
  - Schema
  - Properties
  - Metadata
view_sort: C
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-descriptions-info:
    description: >-
      Schema properties should have descriptions that provide a narrative of the
      property contains, and how it can be used
    message: Schema Properties Have Description
    severity: info
    given: $.properties[?(@.type == 'string')]
    then:
      field: description
      function: falsy
slug: json-schema-2020-12-properties-descriptions-info
---