---
name: OpenAPI Request Body On Put Info
description: >-
  PUT HTTP methods can have a request body, providing a structured payload for
  configuring each API request
message: PUT Requests Has a Body
given: $.paths.*.put
severity: info
tags:
  - OpenAPI
  - Request Bodies
  - PUT  
  - Default
view_sort: D
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-put-info:
    description: >-
      PUT HTTP methods can have a request body, providing a structured payload
      for configuring each API request
    message: PUT Requests Has a Body
    given: $.paths.*.put
    severity: info
    then:
      field: requestBody
      function: falsy
slug: openapi-request-bodies-put-info
---