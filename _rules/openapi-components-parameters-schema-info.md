---
name: OpenAPI Components Parameters Schema Info
description: >-
  Parameters must always possess a schema to help define the format and shape of
  the parameter, setting expections with consumers about what should be passed
  in
message: Parameters Have Schema
given: $.components.parameters.*
severity: info
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
  openapi-components-parameters-schema-info:
    description: >-
      Parameters must always possess a schema to help define the format and
      shape of the parameter, setting expections with consumers about what
      should be passed in
    message: Parameters Have Schema
    severity: info
    given: $.components.parameters.*
    then:
      field: schema
      function: falsy
slug: openapi-components-parameters-schema-info
---