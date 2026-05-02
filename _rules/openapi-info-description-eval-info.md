---
name: OpenAPI Info Description Eval Tag Info
description: >-
  Eval functions MUST not be included in the description of an API, keeping descriptions to just the text that is needed, and relying on the rest of the OpenAPI to describe what is possible.
message: Info MUST Have Description
given: $.info
severity: info
tags:
  - OpenAPI
  - Metadata  
  - Default
  - Documentation
view_sort: C  
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  openapi-info-description-eval-info:
    description: >-
      Eval functions MUST not be included in the description of an API, keeping descriptions to just the text that is needed, and relying on the rest of the OpenAPI to describe what is possible.
    message: Info Description Does Not Have Eval Tag
    severity: info
    given: $.info
    then:
      field: description
      function: pattern
      functionOptions:
        match: ^\b(<eval)\b
slug: openapi-info-description-eval-info
---