---
name: OpenAPI Info Description Script Tag Info
description: >-
  Script tags MUST not be included in the description of an API, keeping descriptions to just the text that is needed, and relying on the rest of the OpenAPI to describe what is possible.
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
  openapi-info-description-script-info:
    description: >-
      Script tags MUST not be included in the description of an API, keeping descriptions to just the text that is needed, and relying on the rest of the OpenAPI to describe what is possible.
    message: Info Description Does Not Have Script Tag
    severity: info
    given: $.info
    then:
      field: description
      function: pattern
      functionOptions:
        match: ^\b(<script)\b
slug: openapi-info-description-script-info
---