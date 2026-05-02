---
name: OpenAPI Response Post 403 Status Code Info
description: >-
  POST responses should have a 403 forbidden HTTP status code, communicating
  that consumers are not allowed to access
message: POST Responses MUST Have 403 Status Codes
given: $.paths.*.post.responses
severity: info
tags:
  - OpenAPI
  - Responses
  - POST
  - 4xx
view_sort: N
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-403-status-code-info:
    description: >-
      POST responses should have a 403 forbidden HTTP status code, communicating
      that consumers are not allowed to access
    message: POST Responses MUST Have 403 Status Codes
    severity: info
    given: $.paths.*.post.responses
    then:
      field: '403'
      function: falsy
slug: openapi-response-post-403-status-code-info
---