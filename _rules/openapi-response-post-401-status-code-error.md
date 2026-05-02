---
name: OpenAPI Response Post 401 Status Code Error
description: >-
  POST responses should have a 401 unauthorized HTTP status code, communicating
  that consumers do not have access
message: POST Responses Has 401 Status Codes
given: $.paths.*.post.responses
severity: error
tags:
  - OpenAPI
  - Responses
  - POST
  - 4xx
view_sort: L
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-401-status-code-error:
    description: >-
      POST responses should have a 401 unauthorized HTTP status code,
      communicating that consumers do not have access
    message: POST Responses Has 401 Status Codes
    severity: error
    given: $.paths.*.post.responses
    then:
      field: '401'
      function: truthy
slug: openapi-response-post-401-status-code-error
---