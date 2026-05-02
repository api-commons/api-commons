---
name: OpenAPI No Path Trailing Slash Info
description: >-
  It is common to be explicit and consistent about whether or not to have a
  trailing slack on each API path
message: Path Trailing Slash
given: $.paths.*~
severity: info
tags:
  - OpenAPI
  - Paths
  - Default
guidance: Naming
guidanceUrl: https://guidance.apievangelist.com/naming
rule:
  openapi-no-path-trailing-slash-info:
    description: >-
      It is common to be explicit and consistent about whether or not to have a
      trailing slack on each API path
    message: Path Trailing Slash
    severity: info
    given: $.paths.*~
    then:
      function: pattern
      functionOptions:
        match: /$
slug: openapi-no-path-trailing-slash-info
---