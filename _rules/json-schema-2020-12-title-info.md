---
name: JSON Schema Draft 2020-12 Title Info
description: >-
  JSON Schema objects MUST include a title property that describes the object in plain language while reflecting the object's file name. The title should convey the object's content and purpose, providing clarity on how it is intended to be used.
slug: json-schema-2020-12-title-info
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
view_sort: E
rule:
  json-schema-2020-12-title-info:
    description: JSON Schema objects MUST include a title property that describes the object in plain language while reflecting the object's file name. The title should convey the object's content and purpose, providing clarity on how it is intended to be used.
    given: $
    severity: error
    then:
      field: title
      function: falsy
---