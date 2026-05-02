---
name: OpenAPI Components Parameters Example Error
description: >-
  Parameters must always possess a example to help define the format and shape of
  the parameter, setting expections with consumers about what should be passed
  in
message: Parameters MUST Have Example
given: $.components.parameters.*
tags:
  - OpenAPI
  - Components
  - Parameters
  - Example
view_sort: F  
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-example-error:
    description: >-
      Parameters must always possess a example to help define the format and
      shape of the parameter, setting expections with consumers about what
      should be passed in
    message: Parameters MUST Have Example
    given: $.components.parameters.*
    then:
      field: example
      function: truthy
slug: openapi-components-parameters-example-error
---