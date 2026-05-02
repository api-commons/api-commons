---
name: OpenAPI Request Body Have Examples Info
description: >-
  POST, PUT, and PATCH request bodies should have examples, providing one or
  more examples of what should be submitted for different types of requests
message: Request Bodies Have Examples
given: $.paths.*.*.requestBody.content.*
severity: info
tags:
  - OpenAPI
  - Request Bodies
  - Examples  
view_sort: K
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-examples-info:
    description: >-
      POST, PUT, and PATCH request bodies should have examples, providing one or
      more examples of what should be submitted for different types of requests
    message: Request Bodies Have Examples
    given: $.paths.*.*.requestBody.content.*
    severity: info
    then:
      field: examples
      function: falsy
slug: openapi-request-bodies-examples-info
---