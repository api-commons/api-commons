---
name: OpenAPI Response Put 403 Status Code Error
description: >-
  PUT responses should have a 403 forbidden HTTP status code, communicating that
  consumers are not allowed to access
message: PUT Responses MUST Have 403 Status Codes
given: $.paths.*.put.responses
severity: error
tags:
  - OpenAPI
  - Responses
  - PUT
  - 4xx
view_sort: F
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-put-403-status-code-error:
    description: >-
      PUT responses should have a 403 forbidden HTTP status code, communicating
      that consumers are not allowed to access
    message: PUT Responses MUST Have 403 Status Codes
    severity: error
    given: $.paths.*.put.responses
    then:
      field: '403'
      function: truthy
slug: openapi-response-put-403-status-code-error
---