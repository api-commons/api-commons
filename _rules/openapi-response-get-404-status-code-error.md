---
name: OpenAPI Response Get 404 Status Code Error
description: >-
  GET responses should have a 404 not found HTTP status code, communicating that
  nothing was found to consumers
message: GET Responses MUST Have 404 Status Code
given: $.paths.*.get[?(@.properties)]
severity: error
tags:
  - OpenAPI
  - Responses
  - GET
  - 4xx
  - Default
view_sort: N
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-404-status-code-error:
    description: >-
      GET responses should have a 404 not found HTTP status code, communicating
      that nothing was found to consumers
    message: GET Responses MUST Have 404 Status Code
    severity: error
    given: $.paths.*.get[?(@.properties)]
    then:
      field: '404'
      function: truthy
slug: openapi-response-get-404-status-code-error
---