---
name: OpenAPI Components Parameters Schema Type Integer Minimum Info
description: >-
  Parameters that are of the integer schema type must have their minimum value
  set, defining the shape of parameter data passed in with a request
message: Parameter Schema Type Integer Minimum
given:
  - $.components.parameters.[?(@.type=='integer')]
severity: info
tags:
  - OpenAPI
  - Components
  - Parameters
  - Schema  
  - Type
  - Default
  - Security
view_sort: K
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-schema-type-integer-minimum-info:
    description: >-
      Parameters that are of the integer schema type must have their minimum
      value set, defining the shape of parameter data passed in with a request
    message: Parameter Schema Type Integer Minimum
    given:
      - $.apis.*.properties.*
      - $.common.*
    severity: info
    then:
      field: minimum
      function: falsy
slug: openapi-components-parameters-schema-type-integer-minimum-info
---