---
slug: openapi-schema-properties-type-defined-error
icon: check-square
name: OpenAPI Schema Properties Type Defined
description: >-
  All schema properties must have a type explicitly defined to ensure proper validation, code generation, and documentation. Properties without types are ambiguous and error-prone.
message: Schema properties MUST have a type defined.
given: $..properties.*
severity: error
view_sort: B
tags:
  - OpenAPI
  - Schema
  - Properties
  - Types
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  openapi-schema-properties-type-defined-error:
    description: >-
      All schema properties must have a type explicitly defined to ensure proper validation, code generation, and documentation. Properties without types are ambiguous and error-prone.
    message: Schema properties MUST have a type defined.
    given: $..properties.*
    severity: error
    then:
      field: type
      function: truthy
---
