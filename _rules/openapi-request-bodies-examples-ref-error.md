---
name: OpenAPI Request Body Have Examples Ref Error
description: >-
  POST, PUT, and PATCH request bodies should have examples using references to
  centralized component examples, providing one or more examples of what should
  be submitted for different types of requests
message: Request Bodies MUST Use Examples Reference
given: $.paths.*.*.requestBody.content.*.examples
severity: error
tags:
  - OpenAPI
  - Request Bodies
  - Examples  
view_sort: L
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-examples-ref-error:
    description: >-
      POST, PUT, and PATCH request bodies should have examples using references
      to centralized component examples, providing one or more examples of what
      should be submitted for different types of requests
    message: Request Bodies MUST Use Examples Reference
    severity: error
    given: $.paths.*.*.requestBody.content.*.examples
    then:
      field: $ref
      function: falsy
slug: openapi-request-bodies-examples-ref-error
---