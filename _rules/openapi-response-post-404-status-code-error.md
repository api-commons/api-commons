---
name: OpenAPI Response Post 404 Status Code Error
description: >-
  POST responses should have a 404 not found HTTP status code, communicating
  that nothing was found to consumers
message: POST Responses Has 404 Status Codes
given: $.paths.*.post.responses
severity: error
tags:
  - OpenAPI
  - Responses
  - POST
  - 4xx
view_sort: P
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-404-status-code-error:
    description: >-
      POST responses should have a 404 not found HTTP status code, communicating
      that nothing was found to consumers
    message: POST Responses Has 404 Status Codes
    severity: error
    given: $.paths.*.post.responses
    then:
      field: '404'
      function: truthy
slug: openapi-response-post-404-status-code-error
---