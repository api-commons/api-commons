---
name: OpenAPI Response Get 429 Status Code Error
description: >-
  GET responses should have a 429 too many requests HTTP status code,
  communicating a consumer has made too may requests
message: GET Responses Has 429 Status Code
given: $.paths.*.get.responses
severity: error
tags:
  - OpenAPI
  - Responses
  - GET
  - 4xx
view_sort: P
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-429-status-code-error:
    description: >-
      GET responses should have a 429 too many requests HTTP status code,
      communicating a consumer has made too may requests
    message: GET Responses Has 429 Status Code
    severity: error
    given: $.paths.*.get.responses
    then:
      field: '429'
      function: truthy
slug: openapi-response-get-429-status-code-error
---