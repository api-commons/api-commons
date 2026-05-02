---
name: JSON Schema Draft 2020-12 ID Source URL Info
description: The $id property in any JSON Schema MUST contain a valid URL pointing to a central registry, repository, or another authoritative source for the object. This URL ensures that the object's source is always accessible and can be used for proper validation.
slug: json-schema-2020-12-id-source-url-info
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
  - Identifiers
view_sort: B
rule:
  json-schema-2020-12-id-source-url-info:
    description: The $id property in any JSON Schema MUST contain a valid URL pointing to a central registry, repository, or another authoritative source for the object. This URL ensures that the object's source is always accessible and can be used for proper validation.
    given: $
    severity: error
    then:
      field: "$id"
      function: pattern
      functionOptions:
        notMatch: \b(example.com)\b
---