---
name: OpenAPI Path Declarations Error
description: >-
  There must be a paths property and have paths declared, providing the minimum viable definition for an API.
message: OpenAPI Path Declarations Error
given: $.paths
severity: error
tags:
  - OpenAPI
  - Paths
  - Default
view_sort: A  
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
  openapi-paths-declarations-error:
    description: >-
      There must be a paths property and have paths declared, providing the minimum viable definition for an API.
    message: OpenAPI Path Declarations Error
    severity: error
    resolved: false
    given: $.paths
    then:
      field: '@key'
      function: pattern
      functionOptions:
        notMatch: '{}'
slug: openapi-paths-declarations-error
---