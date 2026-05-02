---
name: OpenAPI Response Post 400 Status Code Error
description: >-
  POST responses should have a 400 not found HTTP status code, communicating
  nothing was found to consumers
message: POST Responses Has 400 Status Codes
given: $.paths.*.post.responses
severity: error
tags:
  - OpenAPI
  - Responses
  - POST
  - 4xx
view_sort: J
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-400-status-code-error:
    description: >-
      POST responses should have a 400 not found HTTP status code, communicating
      nothing was found to consumers
    message: POST Responses Has 400 Status Codes
    severity: error
    given: $.paths.*.post.responses
    then:
      field: '400'
      function: truthy
slug: openapi-response-post-400-status-code-error
---