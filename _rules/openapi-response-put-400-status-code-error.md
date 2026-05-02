---
name: OpenAPI Response Put 400 Status Code Error
description: >-
  PUT responses should have a 400 not found HTTP status code, communicating
  nothing was found to consumers
message: PUT Responses MUST Have 400 Status Codes
given: $.paths.*.put.responses
severity: error
tags:
  - OpenAPI
  - Responses
  - PUT
  - 4xx
  - Default
view_sort: B
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-put-400-status-code-error:
    description: >-
      PUT responses should have a 400 not found HTTP status code, communicating
      nothing was found to consumers
    message: PUT Responses MUST Have 400 Status Codes
    severity: error
    given: $.paths.*.put.responses
    then:
      field: '400'
      function: truthy
slug: openapi-response-put-400-status-code-error
---