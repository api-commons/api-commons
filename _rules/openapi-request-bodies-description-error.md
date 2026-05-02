---
name: OpenAPI Request Bodies Description Error
description: >-
  It is helpful to provide a description for request bodies, providing a simple
  explanation of what can be configured as part of the request payload
message: Request Bodies MUST Have a Description
given: $.paths.*.requestBody
severity: error
tags:
  - OpenAPI
  - Request Bodies
  - Metadata  
view_sort: F
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-description-error:
    description: >-
      It is helpful to provide a description for request bodies, providing a
      simple explanation of what can be configured as part of the request
      payload
    message: Request Bodies MUST Have a Description
    severity: error
    given: $.paths.*.requestBody
    then:
      field: description
      function: truthy
slug: openapi-request-bodies-description-error
---