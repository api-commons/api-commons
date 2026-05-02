---
name: OpenAPI Components Parameters Required Info
description: >-
  Providrequiredg an required property for parameters gets explicit about whether a
  parameter is required the path, query, or a header, makrequiredg it clear to consumers
  where they can configure their request.
message: Parameters Required Property Is Set
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
  openapi-components-parameters-required-info:
    description: >-
      Providrequiredg an required property for parameters gets explicit about whether a
      parameter is required the path, query, or a header, makrequiredg it clear to consumers
      where they can configure their request.
    message: Parameters Required Property Is Set
    severity: info
    given: $.components.parameters.*
    then:
      field: required
      function: falsy
slug: openapi-components-parameters-required-info
---