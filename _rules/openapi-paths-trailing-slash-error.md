---
name: OpenAPI No Path Trailing Slash Error
description: >-
  It is common to be explicit and consistent about whether or not to have a
  trailing slack on each API path
message: Path Trailing Slash
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
  openapi-no-path-trailing-slash-error:
    description: >-
      It is common to be explicit and consistent about whether or not to have a
      trailing slack on each API path
    message: Path Trailing Slash
    severity: error
    given: $.paths.*~
    then:
      function: pattern
      functionOptions:
        notMatch: /$
slug: openapi-no-path-trailing-slash-error
---