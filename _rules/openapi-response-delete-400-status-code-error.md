---
name: OpenAPI Response Delete 400 Status Code Error
description: >-
  DELETE responses should have a 400 not found HTTP status code, communicating
  nothing was found to consumers
message: DELETE Responses MUST Have 400 Status Codes
given: $.paths.*.delete.responses
severity: error
tags:
  - OpenAPI
  - Responses
  - DELETE
  - 4xx
view_sort: B
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-delete-400-status-code-error:
    description: >-
      DELETE responses should have a 400 not found HTTP status code,
      communicating nothing was found to consumers
    message: DELETE Responses MUST Have 400 Status Codes
    severity: error
    given: $.paths.*.delete.responses
    then:
      field: '400'
      function: truthy
slug: openapi-response-delete-400-status-code-error
---