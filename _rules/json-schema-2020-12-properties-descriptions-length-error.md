---
name: JSON Schema Draft 2020-12 Properties Descriptions Length Error
description: >-
  Schema property descriptions should have a length limit applied, applying
  constraints to writing descriptions, and keeping consistent across APIs
message: Schema Properties Description MUST Have 250 Characters
given: $.properties[?(@.type == 'string')]
severity: error
tags:
  - JSON Schema
  - Schema
  - Properties
  - Metadata
view_sort: CA
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-descriptions-length-error:
    description: >-
      Schema property descriptions should have a length limit applied, applying
      constraints to writing descriptions, and keeping consistent across APIs
    message: Schema Properties Description MUST Have 250 Characters
    severity: error
    given: $.properties[?(@.type == 'string')]
    then:
      field: description
      function: length
      functionOptions:
        max: 250
slug: json-schema-2020-12-properties-descriptions-length-error
---