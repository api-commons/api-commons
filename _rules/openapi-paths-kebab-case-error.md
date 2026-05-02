---
name: OpenAPI Path Kebab Case
description: >-
  Path segments should be kebab case and not have different casing that could cause other problems.
message: Path Segments MUST Be Kebab Case
given: $.paths.*~
severity: error
tags:
  - OpenAPI
  - Paths
  - Casing
  - Default
references:
  - name: Doctor
    type: Editor
    url: https://pb33f.io/doctor/  
guidance: Naming
guidanceUrl: https://guidance.apievangelist.com/naming
rule:
  openapi-no-api-in-path-error:
    description: >-
      Path segments should be kebab case and not have different casing that could cause other problems.
    message: Path Segments MUST Be Kebab Case
    severity: error
    given: $.paths.*~
    then:
      function: pattern
      functionOptions:
        match: "^(\/|[a-z0-9-.]+|{[a-zA-Z0-9]+})+$"
slug: openapi-paths-query-error
---