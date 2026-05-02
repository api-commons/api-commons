---
name: OpenAPI Components Parameters Description Info
description: >-
  Having a parameters description provides more depth to what a parameter does
  and will be displayed via documentation, and other tooling used across the API
  lifecycle
message: Parameters Have a Description
given: $.components.parameters.*
severity: info
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
  openapi-components-parameters-description-info:
    description: >-
      Having a parameters description provides more depth to what a parameter
      does and will be displayed via documentation, and other tooling used
      across the API lifecycle
    message: Parameters Have a Description
    severity: info
    given: $.components.parameters.*
    then:
      field: description
      function: falsy
slug: openapi-components-parameters-description-info
---