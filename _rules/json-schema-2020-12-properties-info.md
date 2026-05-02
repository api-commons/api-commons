---
name: JSON Schema Draft 2020-12 Properties Info
description: >-
  Schema has properties, providing more detail regarding the structure of each
  schema being applied as part of a request or a response
message: Schema Have Properties
given: $[?(@.type=="object")]
severity: info
tags:
  - JSON Schema
  - Schema
  - Properties
view_sort: A
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-info:
    description: >-
      Schema has properties, providing more detail regarding the structure of
      each schema being applied as part of a request or a response
    message: Schema Have Properties
    severity: info
    given: $[?(@.type=="object")]
    then:
      field: properties
      function: falsy
slug: json-schema-2020-12-properties-info
---