---
name: OpenAPI Request Body Content On Post Info
description: >-
  POST requests with a request body should have content defined, providing more
  detail on what is contained within the API request body
message: Request Body Content POST
given: $.paths.*.post.requestBody
severity: info
tags:
  - OpenAPI
  - Request Bodies
  - POST  
view_sort: H
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-content-post-info:
    description: >-
      POST requests with a request body should have content defined, providing
      more detail on what is contained within the API request body
    message: Request Body Content POST
    given: $.paths.*.post.requestBody
    severity: info
    then:
      field: content
      function: falsy
slug: openapi-request-bodies-content-post-info
---