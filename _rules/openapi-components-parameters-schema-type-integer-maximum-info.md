---
name: OpenAPI Components Parameters Schema Type Integer Maximum Info
description: >-
  Parameters that are of the integer schema type must have their maximum value
  set, defining the shape of parameter data passed in with a request
message: Parameter Schema Type Integer Maximum
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
view_sort: L
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-schema-type-integer-maximum-info:
    description: >-
      Parameters that are of the integer schema type must have their maximum
      value set, defining the shape of parameter data passed in with a request
    message: Parameter Schema Type Integer Maximum
    given:
      - $.apis.*.properties.*
      - $.common.*
    severity: info
    then:
      field: maximum
      function: falsy
slug: openapi-components-parameters-schema-type-integer-maximum-info
---