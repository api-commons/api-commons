---
name: OpenAPI Version In Path Error
description: >-
  The majority of public APIs available on the Web today put the major version
  of the API as part of the path for each API
message: Version in Path
given: $.paths[*]~
severity: error
tags:
  - OpenAPI
  - Versions
  - Paths
guidance: Change Management
guidanceUrl: https://guidance.apievangelist.com/change
rule:
  openapi-version-in-path-error:
    description: >-
      The majority of public APIs available on the Web today put the major
      version of the API as part of the path for each API
    message: Version in Path
    severity: error
    given: $.paths[*]~
    then:
      function: pattern
      functionOptions:
        notMatch: /((?:/)(v|version)?[0-9]{1,3}(?:/)?)/i
slug: openapi-version-in-path-error
---