---
name: OpenAPI Response Put 404 Status Code Error
description: >-
  PUT responses should have a 404 not found HTTP status code, communicating that
  nothing was found to consumers
message: PUT Responses MUST Have 404 Status Codes
given: $.paths.*.put.responses
severity: error
tags:
  - OpenAPI
  - Responses
  - PUT
  - 4xx
view_sort: H
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-put-404-status-code-error:
    description: >-
      PUT responses should have a 404 not found HTTP status code, communicating
      that nothing was found to consumers
    message: PUT Responses MUST Have 404 Status Codes
    severity: error
    given: $.paths.*.put.responses
    then:
      field: '404'
      function: truthy
slug: openapi-response-put-404-status-code-error
---