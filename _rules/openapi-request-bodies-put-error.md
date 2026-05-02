---
name: OpenAPI Request Body On Put Error Info
description: >-
  PUT HTTP methods can have a request body, providing a structured payload for
  configuring each API request
message: PUT Requests MUST Have a Body
given: $.paths.*.put
severity: error
tags:
  - OpenAPI
  - Request Bodies
  - PUT  
  - Default
view_sort: D
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-put-error:
    description: >-
      PUT HTTP methods can have a request body, providing a structured payload
      for configuring each API request
    message: PUT Requests MUST Have a Body
    given: $.paths.*.put
    severity: error
    then:
      field: requestBody
      function: truthy
slug: openapi-request-bodies-put-error
---