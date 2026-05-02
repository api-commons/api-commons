---
name: OpenAPI Components Parameters Schema Type Error
description: >-
  Parameters must always have their schema type defined, being precise about
  what type of data can be inputted and used to configure an API request
message: Parameter Schema Type
given: $.components.parameters.*.schema
severity: error
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
  openapi-components-parameters-schema-type-error:
    description: >-
      Parameters must always have their schema type defined, being precise about
      what type of data can be inputted and used to configure an API request
    message: Parameter Schema Type
    given: $.components.parameters.*.schema
    severity: error
    then:
      field: type
      function: truthy
slug: openapi-components-parameters-schema-type-error
---