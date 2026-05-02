---
name: OpenAPI Components Parameters Schema Type String Minlength Info
description: >-
  Parameters that are of the string schema type must have their minimum value
  set, defining the shape of parameter data passed in with a request
message: Parameter Schema Type String MinLength
given:
  - $.components.parameters.[?(@.type=='string')]
severity: info
tags:
  - OpenAPI
  - Components
  - Parameters
  - Schema
  - Type
  - Default
  - Security
view_sort: H
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-schema-type-string-minlength-info:
    description: >-
      Parameters that are of the string schema type must have their minimum
      value set, defining the shape of parameter data passed in with a request
    message: Parameter Schema Type String MinLength
    given:
      - $.apis.*.properties.*
      - $.common.*
    severity: info
    then:
      field: minLength
      function: falsy
slug: openapi-components-parameters-schema-type-string-minlength-info
---