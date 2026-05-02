---
name: OpenAPI Components Parameters Schema Type Info
description: >-
  Parameters must always have their schema type defined, being precise about
  what type of data can be inputted and used to configure an API request
message: Parameter Schema Type
given: $.components.parameters.*.schema
severity: info
tags:
  - OpenAPI
  - Components
  - Parameters
  - Schema
  - Type
  - Default
view_sort: G  
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-schema-type-info:
    description: >-
      Parameters must always have their schema type defined, being precise about
      what type of data can be inputted and used to configure an API request
    message: Parameter Schema Type
    severity: info
    given: $.components.parameters.*.schema
    then:
      field: type
      function: falsy
slug: openapi-components-parameters-schema-type-info
---