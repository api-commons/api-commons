---
name: OpenAPI No Api In Path Info
description: >-
  The query delimiter should not be included as part of any API path.
message: The Query Is Not Included in API Paths  
given: $.paths.*~
severity: info
tags:
  - OpenAPI
  - Paths
  - Default
guidance: Naming
guidanceUrl: https://guidance.apievangelist.com/naming
rule:
  openapi-no-api-in-path-info:
    description: >-
      The query delimiter should not be included as part of any API path.
    message: The Query Is Not Included in API Paths  
    severity: info
    given: $.paths.*~
    then:
      function: pattern
      functionOptions:
        notMatch: '\\?'
slug: openapi-paths-query-info
---