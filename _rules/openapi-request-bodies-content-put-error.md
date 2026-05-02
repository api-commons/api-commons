---
name: OpenAPI Request Body Content On Put Error
description: >-
  PUT requests with a request body should have content defined, providing more
  detail on what is contained within the API request body
message: Request Body Content PUT
given: $.paths.*.put.requestBody
severity: error
tags:
  - OpenAPI
  - Request Bodies
  - PUT  
view_sort: H
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-content-put-error:
    description: >-
      PUT requests with a request body should have content defined, providing
      more detail on what is contained within the API request body
    message: Request Body Content PUT
    given: $.paths.*.put.requestBody
    severity: error
    then:
      field: content
      function: truthy
slug: openapi-request-bodies-content-put-error
---