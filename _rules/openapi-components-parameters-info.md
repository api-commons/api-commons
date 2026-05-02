---
name: OpenAPI Components Parameters Info
description: >-
  Having a components parameters object allows all parameters used across an API
  to be centralized, allowing for reuse and easier governance of the parameters
  used to configure API requests
message: Components Have a Parameters Property
given: $.components
severity: info
tags:
  - OpenAPI
  - Components
  - Parameters
  - Metadata
  - Default
view_sort: AB  
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-info:
    description: >-
      Having a components parameters object allows all parameters used across an
      API to be centralized, allowing for reuse and easier governance of the
      parameters used to configure API requests
    message: Components Have a Parameters Property
    severity: info
    given: $.components
    then:
      field: parameters
      function: falsy
slug: openapi-components-parameters-info
---