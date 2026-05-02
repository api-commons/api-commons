---
name: OpenAPI Request Body Have Examples Ref Info
description: >-
  POST, PUT, and PATCH request bodies should have examples using references to
  centralized component examples, providing one or more examples of what should
  be submitted for different types of requests
message: Request Bodies Use Examples Reference
given: $.paths.*.*.requestBody.content.*.examples
severity: info
tags:
  - OpenAPI
  - Request Bodies
  - Examples  
view_sort: L
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-examples-ref-info:
    description: >-
      POST, PUT, and PATCH request bodies should have examples using references
      to centralized component examples, providing one or more examples of what
      should be submitted for different types of requests
    message: Request Bodies Use Examples Reference
    severity: info
    given: $.paths.*.*.requestBody.content.*.examples
    then:
      field: $ref
      function: truthy
slug: openapi-request-bodies-examples-ref-info
---