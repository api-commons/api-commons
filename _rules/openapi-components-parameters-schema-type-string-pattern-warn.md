---
name: OpenAPI Components Parameters Schema Type String Pattern Warn
description: >-
  Parameters that are of the string schema type must have a pattern set, using a
  regex to define the shape of parameter data passed in with a request
message: Parameter Schema Type String Pattern
given:
  - $.components.parameters.[?(@.type=='string')]
severity: warn
tags:
  - OpenAPI
  - Components
  - Parameters
  - Schema  
  - Type
  - Default
  - Security
view_sort: J
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-schema-type-string-pattern-warn:
    description: >-
      Parameters that are of the string schema type must have a pattern set,
      using a regex to define the shape of parameter data passed in with a
      request
    message: Parameter Schema Type String Pattern
    given:
      - $.apis.*.properties.*
      - $.common.*
    severity: warn
    then:
      field: pattern
      function: truthy
slug: openapi-components-parameters-schema-type-string-pattern-warn
---