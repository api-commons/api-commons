---
name: OpenAPI Components Parameters Schema Error
description: >-
  Parameters must always possess a schema to help define the format and shape of
  the parameter, setting expections with consumers about what should be passed
  in
message: Parameters MUST Have Schema
given: $.components.parameters.*
tags:
  - OpenAPI
  - Components
  - Parameters
  - Schema
  - Default
view_sort: F  
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-schema-error:
    description: >-
      Parameters must always possess a schema to help define the format and
      shape of the parameter, setting expections with consumers about what
      should be passed in
    message: Parameters MUST Have Schema
    given: $.components.parameters.*
    then:
      field: schema
      function: truthy
slug: openapi-components-parameters-schema-error
---