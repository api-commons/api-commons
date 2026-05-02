---
name: OpenAPI Response Post 403 Status Code Error
description: >-
  POST responses should have a 403 forbidden HTTP status code, communicating
  that consumers are not allowed to access
message: POST Responses Has 403 Status Codes
given: $.paths.*.post.responses
severity: error
tags:
  - OpenAPI
  - Responses
  - POST
  - 4xx
view_sort: N
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-403-status-code-error:
    description: >-
      POST responses should have a 403 forbidden HTTP status code, communicating
      that consumers are not allowed to access
    message: POST Responses Has 403 Status Codes
    severity: error
    given: $.paths.*.post.responses
    then:
      field: '403'
      function: truthy
slug: openapi-response-post-403-status-code-error
---