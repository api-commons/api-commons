---
name: OpenAPI Components Parameters Error
description: >-
  Having a components parameters object allows all parameters used across an API
  to be centralized, allowing for reuse and easier governance of the parameters
  used to configure API requests
message: Components MUST Have a Parameters Property
given: $.components
severity: error
tags:
  - OpenAPI
  - Components
  - Parameters
view_sort: AB  
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-error:
    description: >-
      Having a components parameters object allows all parameters used across an
      API to be centralized, allowing for reuse and easier governance of the
      parameters used to configure API requests
    message: Components MUST Have a Parameters Property
    severity: error
    given: $.components
    then:
      field: parameters
      function: truthy
slug: openapi-components-parameters-error
---