---
name: OpenAPI Components Parameters In Error
description: >-
  Providing an in property for parameters gets explicit about whether a
  parameter is in the path, query, or a header, making it clear to consumers
  where they can configure their request
message: Parameters In Property MUST Be Set
given: $.components.parameters.*
tags:
  - OpenAPI
  - Components
  - Parameters
  - Metadata
  - Default
view_sort: C
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-in-error:
    description: >-
      Providing an in property for parameters gets explicit about whether a
      parameter is in the path, query, or a header, making it clear to consumers
      where they can configure their request
    message: Parameters In Property MUST Be Set
    given: $.components.parameters.*
    then:
      field: in
      function: truthy
slug: openapi-components-parameters-in-error
---