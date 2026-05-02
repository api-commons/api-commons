---
name: OpenAPI Info Title Upper Case Error
description: >-
  Having a consistent casing for the title for your API helps provide
  constraints for teams naming the API, but also keep consistent with other APIs
  from across teams
message: Info Title Has First Characters Capitalized
given: $.info.title
severity: error
tags:
  - OpenAPI
  - Metadata
  - Default
  - Documentation
view_sort: BB  
guidance: Naming
guidanceUrl: https://guidance.apievangelist.com/naming
rule:
  openapi-info-title-upper-case-error:
    description: >-
      Having a consistent casing for the title for your API helps provide
      constraints for teams naming the API, but also keep consistent with other
      APIs from across teams
    message: Info Title Has First Characters Capitalized
    severity: error
    given: $.info.title
    then:
      function: pattern
      functionOptions:
        match: '[A-Z]\w*'
slug: openapi-info-title-upper-case-error
---