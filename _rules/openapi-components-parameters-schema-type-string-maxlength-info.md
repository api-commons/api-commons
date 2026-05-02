---
name: OpenAPI Components Parameters Schema Type String Maxlength Info
description: >-
  Parameters that are of the type string schema type must have their maximum
  value set, defining the shape of parameter data passed in with a request
message: Parameter Schema Type String MaxLength
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
view_sort: I 
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-schema-type-string-maxlength-info:
    description: >-
      Parameters that are of the type string schema type must have their maximum
      value set, defining the shape of parameter data passed in with a request
    message: Parameter Schema Type String MaxLength
    given:
      - $.apis.*.properties.*
      - $.common.*
    severity: info
    then:
      field: maxLength
      function: falsy
slug: openapi-components-parameters-schema-type-string-maxlength-info
---