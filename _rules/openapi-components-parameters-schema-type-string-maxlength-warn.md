---
name: OpenAPI Components Parameters Schema Type String Maxlength Warn
description: >-
  Parameters that are of the string schema type must have their maximum value
  set, defining the shape of parameter data passed in with a request
message: Parameter Schema Type String MaxLength
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
view_sort: I
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-schema-type-string-maxlength-warn:
    description: >-
      Parameters that are of the string schema type must have their maximum
      value set, defining the shape of parameter data passed in with a request
    message: Parameter Schema Type String MaxLength
    given:
      - $.apis.*.properties.*
      - $.common.*
    severity: warn
    then:
      field: maxLength
      function: truthy
slug: openapi-components-parameters-schema-type-string-maxlength-warn
---