---
name: JSON Schema Draft 2020-12 Description Error
description: >-
  Each JSON Schema object MUST include a description that explains, in plain language, the purpose and function of the object. This description should provide a clear overview of how the object is intended to be used within operations.
slug: json-schema-2020-12-description-error
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
view_sort: F
rule:
  json-schema-2020-12-description-error:
    description: Each JSON Schema object MUST include a description that explains, in plain language, the purpose and function of the object. This description should provide a clear overview of how the object is intended to be used within operations.
    given: $
    severity: error
    then:
      field: description
      function: truthy
---