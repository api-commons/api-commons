---
name: OpenAPI Response Get 400 Status Code Error
description: >-
  GET responses should have a 400 not found HTTP status code, communicating
  nothing was found to consumers
message: GET Responses MUST Have 400 Status Codes
given: $.paths.*.get.responses
severity: error
tags:
  - OpenAPI
  - Responses
  - GET
  - 4xx
view_sort: H
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-400-status-code-error:
    description: >-
      GET responses should have a 400 not found HTTP status code, communicating
      nothing was found to consumers
    message: GET Responses MUST Have 400 Status Codes
    severity: error
    given: $.paths.*.get.responses
    then:
      field: '400'
      function: truthy
slug: openapi-response-get-400-status-code-error
---