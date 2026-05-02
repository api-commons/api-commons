---
name: JSON Schema Draft 2020-12 Properties Error
description: >-
  Schema has properties, providing more detail regarding the structure of each
  schema being applied as part of a request or a response
message: Schema MUST Have Properties
given: $[?(@.type=="object")]
severity: error
tags:
  - JSON Schema
  - Schema
  - Properties
view_sort: A
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-error:
    description: >-
      Schema has properties, providing more detail regarding the structure of
      each schema being applied as part of a request or a response
    message: Schema MUST Have Properties
    severity: error
    given: $[?(@.type=="object")]
    then:
      field: properties
      function: truthy
slug: json-schema-2020-12-properties-error
---