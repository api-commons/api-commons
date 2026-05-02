---
name: JSON Schema Draft 2020-12 Properties Define Number Minimum Error
description: >-
  Schema properties that are of the type number should have a minimum property
  defined
message: Schema Number Properties MUST Have Minimum
given: $.properties[?(@.type=="number")]
severity: error
tags:
  - JSON Schema
  - Schema
  - Properties
  - Types
view_sort: FA
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-define-number-minimum-error:
    description: >-
      Schema properties that are of the type number should have a minimum
      property defined
    message: Schema Number Properties MUST Have Minimum
    severity: error
    given: $.properties[?(@.type=="number")]
    then:
      - field: minimum
        function: defined
slug: json-schema-2020-12-properties-define-number-minimum-error
---