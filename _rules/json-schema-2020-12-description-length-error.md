---
name: JSON Schema Draft 2020-12 Description Length Error
description: >-
  The description for any JSON Schema object should be concise, ensuring it remains easy to read and understand for anyone using or interpreting it. This approach helps keep the schema self-contained while still providing enough context to inform its application wherever it is used.
slug: json-schema-2020-12-description-length-error
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
view_sort: FA
rule:
  json-schema-2020-12-description-length-error:
    description: The description for any JSON Schema object should be concise, ensuring it remains easy to read and understand for anyone using or interpreting it. This approach helps keep the schema self-contained while still providing enough context to inform its application wherever it is used.
    given: $
    severity: error
    then:
      field: description
      function: length
      functionOptions:
        max: 250
---