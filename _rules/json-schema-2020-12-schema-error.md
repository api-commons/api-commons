---
name: JSON Schema Draft 2020-12 Schema Error
description: JSON Schema objects should always include the $schema property to explicitly indicate which version of the specification is being used. This property is essential for tooling and should consistently reference the latest version to ensure compatibility and up-to-date functionality.
slug: json-schema-2020-12-schema-error
engine: Unknown
specification: Unknown
specificationUrl: https://example.com
guidance: API Evangelist
guidanceUrl: https://guidance.apievangelist.com
severity: error
type: Default
tags:
  - JSON Schema
  - Metadata
  - Changes
view_sort: C
rule:
  json-schema-2020-12-schema-error:
    description: JSON Schema objects should always include the $schema property to explicitly indicate which version of the specification is being used. This property is essential for tooling and should consistently reference the latest version to ensure compatibility and up-to-date functionality.
    given: $
    severity: error
    then:
      field: "$schema"
      function: truthy
---