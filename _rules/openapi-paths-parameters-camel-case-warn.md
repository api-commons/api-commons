---
slug: openapi-paths-parameters-camel-case-warn
icon: type
name: OpenAPI Path Parameters Camel Case
description: >-
  Path parameters should follow camelCase naming convention for consistency across the API, making parameter names predictable and aligned with common programming conventions.
message: Path parameters SHOULD be camelCase.
given: "$.paths[*].parameters[?(@.in=='path')].name"
severity: warn
view_sort: B
tags:
  - OpenAPI
  - Paths
  - Parameters
  - Casing
guidance: Naming
guidanceUrl: https://guidance.apievangelist.com/naming
rule:
  openapi-paths-parameters-camel-case-warn:
    description: >-
      Path parameters should follow camelCase naming convention for consistency across the API, making parameter names predictable and aligned with common programming conventions.
    message: Path parameters SHOULD be camelCase.
    given: "$.paths[*].parameters[?(@.in=='path')].name"
    severity: warn
    then:
      function: pattern
      functionOptions:
        match: "^[a-z][a-zA-Z0-9]*$"
---
