---
name: OpenAPI Response Put 429 Status Code Error
description: >-
  PUT responses should have a 429 too many requests HTTP status code,
  communicating a consumer has made too may requests
message: PUT Responses MUST Have 429 Status Codes
given: $.paths.*.put.responses
severity: error
tags:
  - OpenAPI
  - Responses
  - PUT
  - 4xx
view_sort: J
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-put-429-status-code-error:
    description: >-
      PUT responses should have a 429 too many requests HTTP status code,
      communicating a consumer has made too may requests
    message: PUT Responses MUST Have 429 Status Codes
    severity: error
    given: $.paths.*.put.responses
    then:
      field: '429'
      function: truthy
slug: openapi-response-put-429-status-code-error
---