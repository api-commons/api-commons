---
name: OpenAPI Request Body On Post Info
description: >-
  POST HTTP methods can have a request body, providing a structured payload for
  configuring each API request
message: POST Requests Has a Body
given: $.paths.*.post
severity: info
tags:
  - OpenAPI
  - Request Bodies
  - POST  
  - Default
view_sort: B
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-body-on-post-info:
    description: >-
      POST HTTP methods can have a request body, providing a structured payload
      for configuring each API request
    message: POST Requests Has a Body
    given: $.paths.*.post
    severity: info
    then:
      field: requestBody
      function: falsy
slug: openapi-request-body-on-post-info
---