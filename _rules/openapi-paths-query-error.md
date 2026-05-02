---
name: OpenAPI Path Query
description: >-
  The query delimiter should not be included as part of any API path.
message: The Query Should Not Be Included in API Paths
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
      The query delimiter should not be included as part of any API path.
    message: The Query Should Not Be Included in API Paths
    severity: error
    given: $.paths.*~
    then:
      function: pattern
      functionOptions:
        match: '\\?'
slug: openapi-paths-query-error
---