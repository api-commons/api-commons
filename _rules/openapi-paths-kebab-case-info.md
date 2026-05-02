---
name: OpenAPI Path Kebab Case
description: >-
  The query delimiter should not be included as part of any API path.
message: Path Segments Are Kebab Case
given: $.paths.*~
severity: info
tags:
  - OpenAPI
  - Paths
  - Casing
  - Default
guidance: Naming
guidanceUrl: https://guidance.apievangelist.com/naming
rule:
  openapi-no-api-in-path-info:
    description: >-
      The query delimiter should not be included as part of any API path.
    message: Path Segments Are Kebab Case 
    severity: info
    given: $.paths.*~
    then:
      function: pattern
      functionOptions:
        notMatch: "^(\/|[a-z0-9-.]+|{[a-zA-Z0-9]+})+$"
slug: openapi-paths-query-info
---