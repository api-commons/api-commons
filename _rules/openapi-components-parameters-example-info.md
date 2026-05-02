---
name: OpenAPI Components Parameters Example Info
description: >-
  Parameters must always possess a example to help define the format and shape of
  the parameter, setting expections with consumers about what should be passed
  in
message: Parameters Have Example
given: $.components.parameters.*
severity: info
tags:
  - OpenAPI
  - Components
  - Parameters
  - Example
view_sort: F  
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-example-info:
    description: >-
      Parameters must always possess a example to help define the format and
      shape of the parameter, setting expections with consumers about what
      should be passed in
    message: Parameters Have Example
    severity: info
    given: $.components.parameters.*
    then:
      field: example
      function: falsy
slug: openapi-components-parameters-example-info
---