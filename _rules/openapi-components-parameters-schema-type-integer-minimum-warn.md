---
name: OpenAPI Components Parameters Schema Type Integer Minimum Warn
description: >-
  Parameters that are of the integer schema type must have their minimum value
  set, defining the shape of parameter data passed in with a request
message: Parameter Schema Type Integer Minimum
given:
  - $.components.parameters.[?(@.type=='integer')]
severity: warn
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
  openapi-components-parameters-schema-type-integer-minimum-warn:
    description: >-
      Parameters that are of the integer schema type must have their minimum
      value set, defining the shape of parameter data passed in with a request
    message: Parameter Schema Type Integer Minimum
    given:
      - $.apis.*.properties.*
      - $.common.*
    severity: warn
    then:
      field: minimum
      function: truthy
slug: openapi-components-parameters-schema-type-integer-minimum-warn
---