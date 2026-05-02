---
name: OpenAPI Path Declarations Info
description: >-
  There must be a paths property and have paths declared, providing the minimum viable definition for an API.
message: OpenAPI Path Declarations Info
given: $.paths
severity: info
tags:
  - OpenAPI
  - Paths
  - Default
view_sort: A   
guidance: Naming
guidanceUrl: https://guidance.apievangelist.com/naming
rule:
  openapi-parameters-componentized-info:
    description: >-
      There must be a paths property and have paths declared, providing the minimum viable definition for an API.
    message: OpenAPI Path Declarations Info
    severity: info
    resolved: false
    given: $.paths
    then:
      field: '@key'
      function: pattern
      functionOptions:
        notMatch: '{}'
slug: openapi-paths-declarations-info
---