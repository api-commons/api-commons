---
name: OpenAPI Components Parameters Description Error
description: >-
  Having a parameters description provides more depth to what a parameter does
  and will be displayed via documentation, and other tooling used across the API
  lifecycle
message: Parameters MUST Have a Description
given: $.paths.*.*.parameters.*
tags:
  - OpenAPI
  - Components
  - Parameters
  - Metadata
  - Default
view_sort: E
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-description-error:
    description: >-
      Having a parameters description provides more depth to what a parameter
      does and will be displayed via documentation, and other tooling used
      across the API lifecycle
    message: Parameters MUST Have a Description
    given: $.paths.*.*.parameters.*
    then:
      field: description
      function: truthy
slug: openapi-components-parameters-description-error
---