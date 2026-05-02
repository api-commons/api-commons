---
name: OpenAPI Components Parameters Required Error
description: >-
  Providrequiredg an required property for parameters gets explicit about whether a
  parameter is required the path, query, or a header, making it clear to consumers
  where they can configure their request
message: Parameters Required Property MUST Be Set
given: $.components.parameters.*
severity: error
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
  openapi-components-parameters-required-error:
    description: >-
      Providrequiredg an required property for parameters gets explicit about whether a
      parameter is required the path, query, or a header, making it clear to consumers
      where they can configure their request
    message: Parameters Required Property MUST Be Set
    given: $.components.parameters.*
    severity: error
    then:
      field: required
      function: truthy
slug: openapi-components-parameters-required-error
---