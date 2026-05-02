---
name: OpenAPI No Api In Path Info
description: >-
  There are very few situations where you actually want the acronym API in the
  path of your API, only when it is a resource.
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
      There are very few situations where you actually want the acronym API in the path of your API, only when it is a resource.
    severity: info
    given: $.paths.*~
    then:
      function: pattern
      functionOptions:
        notMatch: \b(API|api)\b
slug: openapi-paths-api-info
---