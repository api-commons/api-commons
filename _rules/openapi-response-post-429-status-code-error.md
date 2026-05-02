---
name: OpenAPI Response Post 429 Status Code Error
description: >-
  POST responses should have a 429 too many requests HTTP status code,
  communicating a consumer has made too may requests
message: POST Responses MUST Have 429 Status Codes
given: $.paths.*.post.responses
severity: error
tags:
  - OpenAPI
  - Responses
  - POST
  - 4xx
view_sort: R
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-429-status-code-error:
    description: >-
      POST responses should have a 429 too many requests HTTP status code,
      communicating a consumer has made too may requests
    message: POST Responses MUST Have 429 Status Codes
    severity: error
    given: $.paths.*.post.responses
    then:
      field: '429'
      function: truthy
slug: openapi-response-post-429-status-code-error
---