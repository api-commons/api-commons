---
name: JSON Schema Draft 2020-12 Type Info
description: JSON Schema objects should explicitly define their type, ensuring clarity about each object's structure. This allows tools utilizing the schema to accurately validate the object wherever it is applied.
slug: json-schema-2020-12-type-info
engine: Unknown
specification: Unknown
specificationUrl: https://example.com
guidance: API Evangelist
guidanceUrl: https://guidance.apievangelist.com
severity: info
type: Default
tags:
  - JSON Schema
  - Metadata
view_sort: G
rule:
  json-schema-2020-12-type-info:
    description: JSON Schema objects should explicitly define their type, ensuring clarity about each object's structure. This allows tools utilizing the schema to accurately validate the object wherever it is applied.
    given: $
    severity: error
    then:
      field: type
      function: falsy 
---