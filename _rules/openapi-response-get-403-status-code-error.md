---
name: OpenAPI Response Get 403 Status Code Error
description: >-
  GET responses should have a 403 forbidden HTTP status code, communicating that
  consumers are not allowed to access
message: GET Responses Has 403 Status Code
given: $.paths.*.get.responses
severity: error
tags:
  - OpenAPI
  - Responses
  - GET
  - 4xx
view_sort: L
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-403-status-code-error:
    description: >-
      GET responses should have a 403 forbidden HTTP status code, communicating
      that consumers are not allowed to access
    message: GET Responses Has 403 Status Code
    severity: error
    given: $.paths.*.get.responses
    then:
      field: '403'
      function: truthy
slug: openapi-response-get-403-status-code-error
---