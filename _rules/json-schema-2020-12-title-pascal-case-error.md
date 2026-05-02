---
name: JSON Schema Draft 2020-12 Title Pascal Case Error
description: >-
  The name of a JSON Schema object should always be in PascalCase to ensure readability and consistency across APIs. Using PascalCase helps maintain uniformity and aligns the object's name with its plain-language title.
slug: json-schema-2020-12-title-pascal-case-error
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
view_sort: EB
rule:
  json-schema-2020-12-title-pascal-case-error:
    description: The name of a JSON Schema object should always be in PascalCase to ensure readability and consistency across APIs. Using PascalCase helps maintain uniformity and aligns the object's name with its plain-language title.
    given: $
    severity: error
    then:
      - field: title
        function: pattern
        functionOptions:
          match: ^[A-Z](([a-z]+[A-Z]?)*)$
      - field: title
        function: pattern
        functionOptions:
          match: ^[A-Z](([a-z0-9]+[A-Z]?)*)$
---