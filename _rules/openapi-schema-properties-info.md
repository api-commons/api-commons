---
name: OpenAPI Schema Properties Info
description: >-
  Schema has properties, providing more detail regarding the structure of each
  schema being applied as part of a request or a response
message: Schema Have Properties
given: $.components.schemas[?(@.type=="object")]
severity: info
tags:
  - OpenAPI
  - Schema
  - Properties
view_sort: A
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  openapi-schema-properties-info:
    description: >-
      Schema has properties, providing more detail regarding the structure of
      each schema being applied as part of a request or a response
    message: Schema Have Properties
    severity: info
    given: $.components.schemas[?(@.type=="object")]
    then:
      field: properties
      function: falsy
slug: openapi-schema-properties-info
---