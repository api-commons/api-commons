---
name: OpenAPI Components Parameters In Info
description: >-
  Providing an in property for parameters gets explicit about whether a
  parameter is in the path, query, or a header, making it clear to consumers
  where they can configure their request
message: Parameters In Property Is Set
given: $.components.parameters.*
severity: info
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
  openapi-components-parameters-in-info:
    description: >-
      Providing an in property for parameters gets explicit about whether a
      parameter is in the path, query, or a header, making it clear to consumers
      where they can configure their request
    message: Parameters In Property Is Set
    severity: info
    given: $.components.parameters.*
    then:
      field: in
      function: falsy
slug: openapi-components-parameters-in-info
---