---
name: OpenAPI Info Description Script Tag Error
description: >-
  Script tags MUST not be included in the description of an API, keeping descriptions to just the text that is needed, and relying on the rest of the OpenAPI to describe what is possible.
message: Info MUST Have Description
given: $.info
severity: error
tags:
  - OpenAPI
  - Metadata
  - Default
  - Documentation
references:
  - name: Doctor
    type: Editor
    url: https://pb33f.io/doctor/
  - name: Spectral
    type: Linter
    url: https://github.com/stoplightio/spectral/blob/develop/packages/rulesets/src/oas/index.ts  
view_sort: C  
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  openapi-info-description-script-error:
    description: >-
      Script tags MUST not be included in the description of an API, keeping descriptions to just the text that is needed, and relying on the rest of the OpenAPI to describe what is possible.
    message: Info Description MUST NOT Have Script Tag
    severity: error
    given: $.info
    then:
      field: description
      function: pattern
      functionOptions:
        notMatch: ^\b(<script)\b
slug: openapi-info-description-script-error
---