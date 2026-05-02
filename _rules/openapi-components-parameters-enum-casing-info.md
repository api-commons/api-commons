---
name: OpenAPI Components Parameters Enum Casing Info
description: >-
  Keeping parameters enumerator casing consistent across APIs helps reduce
  confusion by consumers, and can keep aligned with services and applications
  putting an API to work
message: Parameters Enums Are Upper Snake Case
given: $.components.parameters.*.enum.*
severity: info
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
  openapi-components-parameters-enum-casing-info:
    description: >-
      Keeping parameters enumerator casing consistent across APIs helps reduce
      confusion by consumers, and can keep aligned with services and
      applications putting an API to work
    message: Parameters Enums Are Upper Snake Case
    severity: info
    given: $.components.parameters.*.enum.*
    then:
      function: pattern
      functionOptions:
        match: ^[A-Z]+(?:_[A-Z]+)*$
slug: openapi-components-parameters-enum-casing-info
---