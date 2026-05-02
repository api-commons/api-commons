---
name: OpenAPI Request Body Have Examples Error
description: >-
  POST, PUT, and PATCH request bodies should have examples, providing one or
  more examples of what should be submitted for different types of requests
message: Request Bodies MUST Have Examples
given: $.paths.*.*.requestBody.content.*
severity: error
tags:
  - OpenAPI
  - Request Bodies
  - Examples  
view_sort: K
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-examples-error:
    description: >-
      POST, PUT, and PATCH request bodies should have examples, providing one or
      more examples of what should be submitted for different types of requests
    message: Request Bodies MUST Have Examples
    given: $.paths.*.*.requestBody.content.*
    severity: error
    then:
      field: examples
      function: truthy
slug: openapi-request-bodies-examples-error
---