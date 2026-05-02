---
name: JSON Schema Draft 2020-12 Schema Info
description: JSON Schema objects should always include the $schema property to explicitly indicate which version of the specification is being used. This property is essential for tooling and should consistently reference the latest version to ensure compatibility and up-to-date functionality.
slug: json-schema-2020-12-schema-info
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
  - Changes
view_sort: C
rule:
  json-schema-2020-12-schema-info:
    description: JSON Schema objects should always include the $schema property to explicitly indicate which version of the specification is being used. This property is essential for tooling and should consistently reference the latest version to ensure compatibility and up-to-date functionality.
    given: $
    severity: error
    then:
      field: "$schema"
      function: falsy  
---