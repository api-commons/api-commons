---
name: OpenAPI Paths API
description: >-
  There are very few situations where you actually want the acronym API in the
  path of your API, only when it is a resource.
message: The Word API SHOULD NOT Be in Path
given: $.paths.*~
severity: error
tags:
  - OpenAPI
  - Paths
  - Default
references:
  - name: Doctor
    type: Editor
    url: https://pb33f.io/doctor/
  - name: Spectral
    type: Linter
    url: https://github.com/stoplightio/spectral/blob/develop/packages/rulesets/src/oas/index.ts    
guidance: Naming
guidanceUrl: https://guidance.apievangelist.com/naming
rule:
  openapi-no-api-in-path-error:
    description: >-
      There are very few situations where you actually want the acronym API in the
      path of your API, only when it is a resource.
    message: The Word API SHOULD NOT Be in Path
    severity: error
    given: $.paths.*~
    then:
      function: pattern
      functionOptions:
        match: ^\b(API|api)\b
slug: openapi-paths-apis-error
---