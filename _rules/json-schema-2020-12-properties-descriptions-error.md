---
name: JSON Schema Draft 2020-12 Properties Descriptions Error
description: >-
  Schema properties should have descriptions that provide a narrative of the
  property contains, and how it can be used
message: Schema Properties MUST Have Description
given: $.properties[?(@.type == 'string')]
severity: error
tags:
  - JSON Schema
  - Schema
  - Properties
  - Metadata
view_sort: C
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-descriptions-error:
    description: >-
      Schema properties should have descriptions that provide a narrative of the
      property contains, and how it can be used
    message: Schema Properties MUST Have Description
    severity: error
    given: $.properties[?(@.type == 'string')]
    then:
      field: description
      function: truthy
slug: json-schema-2020-12-properties-descriptions-error
---