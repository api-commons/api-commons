---
name: OpenAPI Request Body Content On Post Error
description: >-
  POST requests with a request body should have content defined, providing more
  detail on what is contained within the API request body
message: Request Body Content POST
given: $.paths.*.post.requestBody
severity: error
tags:
  - OpenAPI
  - Request Bodies
  - POST  
view_sort: H
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-content-post-error:
    description: >-
      POST requests with a request body should have content defined, providing
      more detail on what is contained within the API request body
    message: Request Body Content POST
    given: $.paths.*.post.requestBody
    severity: error
    then:
      field: content
      function: truthy
slug: openapi-request-bodies-content-post-error
---