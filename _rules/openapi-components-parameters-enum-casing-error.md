---
name: OpenAPI Components Parameters Enum Casing Error
description: >-
  Keeping parameters enumerator casing consistent across APIs helps reduce
  confusion by consumers, and can keep aligned with services and applications
  putting an API to work
message: Parameters Enums MUST Must Be Upper Snake Case
given: $.components.parameters.*.enum.*
severity: error
tags:
  - OpenAPI
  - Components
  - Parameters
  - Enumerators  
  - Type
  - Default
view_sort: NA
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-enum-casing-error:
    description: >-
      Keeping parameters enumerator casing consistent across APIs helps reduce
      confusion by consumers, and can keep aligned with services and
      applications putting an API to work
    message: Parameters Enums MUST Must Be Upper Snake Case
    severity: error
    given: $.components.parameters.*.enum.*
    then:
      function: pattern
      functionOptions:
        notMatch: ^[A-Z]+(?:_[A-Z]+)*$
slug: openapi-components-parameters-enum-casing-error
---