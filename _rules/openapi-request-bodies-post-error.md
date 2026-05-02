---
name: OpenAPI Request Body On Post Error
description: >-
  POST HTTP methods can have a request body, providing a structured payload for
  configuring each API request
message: POST Requests MUST Have a Body
given: $.paths.*.post
severity: error
tags:
  - OpenAPI
  - Request Bodies
  - POST  
  - Default
view_sort: B
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-body-on-post-error:
    description: >-
      POST HTTP methods can have a request body, providing a structured payload
      for configuring each API request
    message: POST Requests MUST Have a Body
    given: $.paths.*.post
    severity: error
    then:
      field: requestBody
      function: truthy
slug: openapi-request-body-on-post-error
---